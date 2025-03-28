from sqlalchemy.orm import Session
from app.models import Post
from app.schemas.user import PostCreate

def create_post(db: Session, post: PostCreate, user_id: int) -> Post:
    db_post = Post(**post.dict(), user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_post(db: Session, post_id: int) -> Post:
    return db.query(Post).filter(Post.id == post_id).first()

def get_post(db: Session, skip: int = 0, limit: int = 10) -> list[Post]:
    return db.query(Post).offset(skip).limit(limit).all()

def update_post(db: Session, post_id: int, post: PostCreate) -> Post:
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db_post.title = post.title
        db_post.content = post.content
        db.commit()
        db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int) -> Post:
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
    return db_post