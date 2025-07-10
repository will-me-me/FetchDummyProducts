from typing import Optional, Union
from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr, field_validator
import re

class User(BaseModel):
    name : Union[str, None] = None
    email: Union[EmailStr, None] = None
    password: Union[str, None] = None
    confirm_password: Union[str, None] = None

    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str) -> str:
        if value is None or len(value) < 8:
            raise ValueError("password must be at least 8 characters long")
        if not re.search(r'[A-Z]', value):
            raise ValueError('Password must contain at least one uppercase letter')
        
        if not re.search(r'[a-z]', value):
            raise ValueError('Password must contain at least one lowercase letter')
        
        if not re.search(r'\d', value):
            raise ValueError('Password must contain at least one digit')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError('Password must contain at least one special character')
        
        return value


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "john doe",
                    "email": "jd@gmail.com",
                    "password": "password123",
                    "confirm_password": "password123",
                }
            ]
        }
    }

class userOut(BaseModel):
    id: str = Field(default_factory=lambda: str(ObjectId()))
    name: Union[str, None] = None
    email: Union[str, None] = None

    
    class Config:
        allow_population_by_field_name = True

    
        

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
    # expires_in: int
    user: userOut

class TokenData(BaseModel):
    email: Optional[EmailStr] = None





