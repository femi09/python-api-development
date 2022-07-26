from typing import Optional
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime


class Post(BaseModel):
    title: str
    content: str
    published: bool = True


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password:str

        
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email:EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class PostResponse(PostBase):
    id:int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    
    class Config:
        orm_mode = True
        
class PostVoteResponse(BaseModel):
    Post: PostResponse
    votes: int
    
    class Config:
        orm_mode = True
    
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str] = None
    
class Vote(BaseModel):
    post_id:int
    dir: conint(le=1)