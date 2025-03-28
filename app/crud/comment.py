from sqlalchemy.orm import Session
from app.models import Comment
from app.schemas.user import CommentCreate

def create_comment(db: Session, comment: CommentCreate, user_id: int) -> Comment:
    db_comment = Comment(**comment.dict(), user_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comment(db: Session, comment_id: int) -> Comment:
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comment(db: Session, skip: int = 0, limit: int = 10) -> list[Comment]:
    return db.query(Comment).offset(skip).limit(limit).all()

def update_comment(db: Session, comment_id: int, comment: CommentCreate) -> Comment:
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        db_comment.content = comment.content
        db.commit()
        db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int) -> Comment:
    db_comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment