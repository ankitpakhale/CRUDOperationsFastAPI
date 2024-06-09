# FastAPI CRUD Application with SQLite

This is a simple FastAPI application that performs basic CRUD (Create, Read, Update, Delete) operations using an SQLite database. The application allows users to add, update, and delete items, with all operations managed through a web interface.

### Prerequisites

- Python 3.x
- Requirements (`pip install -r requirements.txt`)

### Setting Up a Virtual Environment

#### On Linux

1. **Install virtualenv**:
    ```bash
    pip install virtualenv
    ```

2. **Create a virtual environment**:
    ```bash
    virtualenv .venv
    ```

3. **Activate the virtual environment**:
    ```bash
    . .venv/bin/activate
    ```

4. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

#### On Windows

1. **Install virtualenv**:
    ```bash
    pip install virtualenv
    ```

2. **Create a virtual environment**:
    ```bash
    virtualenv .venv
    ```

3. **Activate the virtual environment**:
    ```bash
    .venv\Scripts\activate
    ```

4. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

### Project Structure

```
CRUDOperationsFastAPI/
├── main.py
└── templates/
    └── index.html
├── .gitignore
├── readme.md
└── requirements.txt
```

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ankitpakhale/CRUDOperationsFastAPI.git
    cd CRUDOperationsFastAPI
    ```

2. **Create and activate a virtual environment** (see above instructions).

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python3 main.py
    ```

5. **Access the application**:
    Open your browser and navigate to `http://127.0.0.1:8000/`.

### Application Workflow

#### 1. Initialize Database

The database is initialized automatically when the application runs for the first time. It creates a file named `database.db` with a table `items` containing `id` and `name` columns.

#### 2. Main Page (`/`)

- **Route**: `/`
- **Method**: GET
- **Description**: Displays a list of all items and a form to add or update items.
- **Template**: `index.html`

#### 3. Add or Update Item (`/add_or_update`)

- **Route**: `/add_or_update`
- **Method**: POST
- **Description**: Handles both adding new items and updating existing items based on the form input.
- **Form Fields**:
  - `id`: Hidden field for the item ID (used for updating)
  - `name`: Text field for the item name
- **Redirects**: Redirects to the main page (`/`) after the operation.

#### 4. Edit Item (`/edit/{item_id}`)

- **Route**: `/edit/{item_id}`
- **Method**: GET
- **Description**: Fetches the item to be edited and pre-fills the form with the item's current name.
- **Template**: `index.html` (with the form pre-filled)

#### 5. Delete Item (`/delete/{item_id}`)

- **Route**: `/delete/{item_id}`
- **Method**: POST
- **Description**: Deletes the specified item from the database.
- **Redirects**: Redirects to the main page (`/`) after deletion.

### Known Bugs

1. **Simultaneous Edits**: If two users try to edit the same item at the same time, the latest update will overwrite the previous one without any warning or merge conflict resolution.

2. **Form Pre-fill Issue**: If a user navigates to the edit page but does not submit the form, the form remains pre-filled with the item's data, which might be confusing if the user navigates back to the main page and then to the edit form again.

3. **No Confirmation for Deletion**: The application does not ask for confirmation before deleting an item. A user might accidentally delete an item without any warning.

4. **No Input Validation**: The application does not perform any validation on the input data (e.g., ensuring the name is not empty or checking for duplicates).

5. **Database Locking**: Under high concurrency, SQLite might experience database locking issues since it is a single-file database not designed for high write throughput. Consider using a more robust database system like PostgreSQL or MySQL for production applications.

### Usage

1. **View Items**: Visit the main page to see a list of all items.
2. **Add Item**: Use the form on the main page to add a new item. Enter the item name and click "Add Item".
3. **Edit Item**: Click the "Edit" link next to an item to load its details into the form. Update the name and click "Update Item".
4. **Delete Item**: Click the "Delete" button next to an item to remove it from the list.

### Conclusion

This simple FastAPI application demonstrates basic CRUD operations using an SQLite database. It covers initializing the database, performing create, read, update, and delete operations, and managing the application state with proper redirections and context management.