from fastapi import APIRouter, Depends, FastAPI
from typing import Union
 
import auth.jwt_auth as auth
from users.schema import Token, User, UserLogin, userOut
import users.services as user_services

router = APIRouter()


@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/me/")
async def read_me(current_user: dict= Depends(auth.get_current_user)):
    return current_user
  

@router.post('/create_user/', response_model=userOut)
async def create_new_user(user: User, current_user: dict = Depends(auth.get_current_user)):
    user = await user_services.create_user(user)
    return user

@router.post('/login/', response_model=Token)
async def login(user: UserLogin):
    user = await user_services.user_login(user)
    return user

@router.get('/all_user/')
async def get_users(current_user: dict = Depends(auth.get_current_user)):
    users = await user_services.get_all_user()
    return users
