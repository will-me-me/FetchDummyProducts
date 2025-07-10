from typing import Union
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import products.routes as routes
import users.routes as user_routes
import todos.routes as todo_routes

app = FastAPI(
    title="FastAPI PlayGround",
    description="A playground for FastAPI features and functionalities.",
    version="0.1.0",
    
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(routes.router, tags=["products"])
app.include_router(user_routes.router, tags=["users"] )
app.include_router(todo_routes.router, tags=["todos"])

