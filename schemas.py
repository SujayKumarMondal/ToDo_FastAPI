from pydantic import BaseModel

class ToDoBase(BaseModel):
    username: str
    category: str
    name: str
    text: str

class ToDoCreate(BaseModel):
    username: str  # Change user_email to username
    category: str
    name: str
    text: str

class ToDoUpdate(BaseModel):
    username: str
    category: str
    name: str
    text: str

# This will return the data after being inserted
class ToDo(ToDoBase):
    id: int
    username: str  # Change user_email to username

    class Config:
        orm_mode = True
