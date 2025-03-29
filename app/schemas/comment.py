from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str

class Comment(BaseModel):
    id: int
    content: str
    post_id: int
    user_id: int
    
    class Config:
        from_attribures = True