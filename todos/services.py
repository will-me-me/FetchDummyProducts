from bson import ObjectId
from fastapi import Depends
from db import db
from todos.schema import Todo, TodoCreate
import auth.jwt_auth as auth
from typing import List


async def create_todo(todo: TodoCreate, current_user: dict) -> Todo:
    print(f"creating todo for user: {current_user}")
    todo_data = todo.model_dump()
    todo_data['user_id'] = current_user['_id']
    todo_data['completed'] = False  # Default value for completed
    print(f"todo data before inserting into db: {todo_data}")

    todo = db.todos.insert_one(todo_data)
    if not todo.acknowledged:
        raise Exception("Todo creation failed")
    todo_data['_id'] = str(todo.inserted_id)  # Convert ObjectId to string
    todo = Todo(**todo_data)
    print(f"Todo created: {todo}")
    return todo


async def get_current_user_todos(current_user: dict):
    print(current_user)
    user_id = current_user["_id"]
    todos = db.todos.find({"_id": ObjectId(user_id)})
    todo_list = [Todo(**{**todo, '_id': str(todo['_id'])}) for todo in todos]
    print(f"Retrieved todos for user {user_id}: {todo_list}")
    return todo_list





   