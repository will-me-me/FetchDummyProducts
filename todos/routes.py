from todos.schema import Todo, TodoCreate
import todos.services as todo_services
from fastapi import APIRouter, Depends, FastAPI
import auth.jwt_auth as auth


router = APIRouter()

@router.get("/")
async def read_todo_root():
    return{
        "message": "welcome to the  todo app"
    }

@router.post("/create_todo/",  response_model=Todo)
async def  create_todo(todo: TodoCreate, current_user: dict = Depends(auth.get_current_user)):
    todo  = await todo_services.create_todo(todo, current_user)
    return todo

@router.get("/my_todos/")
async def get_mytodos(current_user: dict = Depends(auth.get_current_user)):
    todos  = await todo_services.get_current_user_todos(current_user)
    return todos
