from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import sqlite3
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db()
        with conn:
            conn.execute('''
                CREATE TABLE items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            ''')
        conn.close()

@app.on_event("startup")
async def startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def read_items(request: Request):
    conn = get_db()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "items": items})

@app.post("/add_or_update", response_class=RedirectResponse)
async def add_or_update_item(request: Request, id: int = Form(None), name: str = Form(...)):
    conn = get_db()
    if id:
        with conn:
            conn.execute('UPDATE items SET name = ? WHERE id = ?', (name, id))
    else:
        with conn:
            conn.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.close()
    return RedirectResponse(url="/", status_code=303)

@app.get("/edit/{item_id}", response_class=HTMLResponse)
async def edit_item(request: Request, item_id: int):
    conn = get_db()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (item_id,)).fetchone()
    conn.close()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    items = get_all_items()
    return templates.TemplateResponse("index.html", {"request": request, "item": item, "items": items})

@app.post("/delete/{item_id}", response_class=RedirectResponse)
async def delete_item(item_id: int):
    conn = get_db()
    with conn:
        conn.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.close()
    return RedirectResponse(url="/", status_code=303)

def get_all_items():
    conn = get_db()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return items

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
