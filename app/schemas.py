from datetime import datetime
from pydantic import BaseModel, EmailStr

#********************Post Schemas************

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
        
#*************************User Schemas***********************

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    # Allow Pydantic to create this model from ORM objects (read attributes directly instead of dict)
    class Config:
        from_attributes = True

  

