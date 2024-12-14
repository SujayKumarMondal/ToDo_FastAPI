from fastapi import HTTPException
from sqlalchemy.orm import Session
import models
import schemas

# Get all todos
def get_todos(db: Session):
    return db.query(models.ToDo).all()

def create_user(db: Session, username: str):
    # Check if the user already exists
    db_user = db.query(models.User).filter(models.User.username == username).first()

    if db_user:
        return db_user

    # # If not, create a new user
    db_user = models.User(username=username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

# Create a new todo
def create_todo(db: Session, todo: schemas.ToDoCreate):
    # Directly create a new ToDo entry using the data provided in the request
    db_todo = models.ToDo(
        category=todo.category,
        username=todo.username,  # Using the provided username directly
        name=todo.name,
        text=todo.text
    )

    # Add the todo to the session and commit it to the database
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)  # Refresh to get the created ToDo object with an ID

    return db_todo

# Update a todo
def update_todo(db: Session, todo_id: int, todo: schemas.ToDoUpdate):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db_todo.username = todo.username
        db_todo.category = todo.category
        db_todo.name = todo.name
        db_todo.text = todo.text
        db.commit()
        db.refresh(db_todo)
        return db_todo
    return None

# Delete a todo
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return db_todo
    return None
