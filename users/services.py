from typing import List
from passlib.context import CryptContext
import auth.jwt_auth as jwt_auth
from db import db
from bson import ObjectId
from users.schema import Token, User, UserLogin, userOut
from fastapi import File, HTTPException, status
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

async def hash_password(password: str) -> str:
    return pwd_context.hash(password)

async def password_match(password: str, comfirm_password: str) -> bool:
    return password == comfirm_password


async def create_user(user: User) -> userOut:
    existing_user  = await get_user_by_username(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email Already Exists")
    
    if await password_match(user.password, user.confirm_password) is False:
        raise ValueError("Passwords do not match")
    user_data = user.dict()
    user_data.pop("confirm_password")
    user_data['_id'] = ObjectId()
    user_data['password'] = await hash_password(user.password)
    user = db.users.insert_one(user_data)
    if not user.acknowledged:
        raise Exception("User creation failed")
    print(f"user created: {user_data['_id']}")
    user_data['_id'] = str(user_data['_id'])  # Convert ObjectId to string
    return userOut(**user_data)


async def get_all_user() -> List[userOut]:
    users = db.users.find()
    return [userOut(**{**user, '_id': str(user['_id'])}) for user in users]

async def authenticate_user(user: UserLogin) -> userOut:
    email = user.email
    user_data = await get_user_by_username(email)
    print(f"user data: {user_data}")
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    if not await verify_password(user.password, user_data['password']):
        raise HTTPException(status_code=401, detail="Incorrect password")
    user_data['_id'] = str(user_data['_id'])  # Convert ObjectId to string
    return userOut(**user_data)

async def user_login(user: UserLogin) -> Token:
    authenticated_user = await authenticate_user(user)
    print(f"authenticated users: {authenticated_user}")
    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print("user authenticated succesfully")
    access_token = await jwt_auth.create_access_token(data={"sub": authenticated_user.email})
    print(f"access token created: {access_token}")
    user_response = authenticated_user
    token = Token(
        access_token=access_token,
        token_type="bearer",
        # expires_in=1800,  # 30 minutes
        user=user_response
    )
    return token
    

async def get_user_by_username(email: str):
    """Get user from database by username"""
    return db.users.find_one({"email": email})
    


