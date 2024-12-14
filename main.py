from fastapi import FastAPI, Depends, HTTPException, Path
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi import Request
from pydantic import BaseModel
from sqlalchemy.orm import Session
import crud
import models
import schemas
import auth, sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.orm import declarative_base
from fastapi.openapi.models import OAuthFlowClientCredentials
from database import SessionLocal, engine
import models
import schemas
import crud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI()

# Set up templates
templates = Jinja2Templates(directory="templates")

# Create tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes for Todo CRUD Operations

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/todos/")
async def read_todos(db: Session = Depends(get_db)):
    # Query the 'todos' table in the database
    todos = db.query(models.ToDo).all()  # Fetching all records from the ToDo table
    # Convert the list of SQLAlchemy objects to a list of dictionaries (you can use Pydantic schemas if needed)
    todo_list = [todo.as_dict() for todo in todos]  # Assuming you have a method like as_dict() or you can use a schema

    # Return the data as a JSON response
    return JSONResponse(content={"todos": todo_list})

@app.post("/todos/")
async def create_todo(todo: schemas.ToDoCreate, db: Session = Depends(get_db)):
    db_todo = crud.create_todo(db, todo)
    return {"message": "Todo item created successfully", "todo": db_todo}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: schemas.ToDoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"message": "Todo item updated successfully", "todo": db_todo}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {"message": "Todo item deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5050)
