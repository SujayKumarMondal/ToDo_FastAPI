from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer)
    username = Column(String, ForeignKey("users.username"))  # Add this line to store the username
    category = Column(String)
    name = Column(String)
    text = Column(String)

    user = relationship("User", back_populates="todos")
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# User model with relationship to ToDo
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)  # Change email to username
    
    # Relationship to ToDo model
    todos = relationship("ToDo", back_populates="user")
