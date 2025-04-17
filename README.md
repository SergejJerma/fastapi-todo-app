# FastAPI To-Do App
This is a simple To-Do app API built using FastAPI. It allows users to perform CRUD (Create, Read, Update, Delete) operations on to-do items. The app uses FastAPI as the web framework and can be extended or integrated with any frontend or database (for now, to-do items are stored in-memory storage).
## Features
- Create a new to-do item
- Read a list of all to-do items
- Read a specific to-do item by its ID
- Update an existing to-do item by ID
- Delete a to-do item by ID
## Requirements
- Python 3.12.0 or higher
- FastAPI
- Pydantic (for data validation)
- Uvicorn (for serving the app)
## REST API
- GET: http://127.0.0.1:8000/todos
- POST: http://127.0.0.1:8000/todos
- PUT: http://127.0.0.1:8000/todos/{todo_id}
- DELETE: http://127.0.0.1:8000/todos/{todo_id}
A request body sample
{
    "id": 1,
    "title": "Learn Python",
    "description": "create API"
}
