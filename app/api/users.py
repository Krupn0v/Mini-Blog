from fastapi import Depends, APIRouter
from app.api.auth import get_current_user
from app.schemas.user import User


router = APIRouter(prefix="/users", tags=["users"])

@router.get("/id", response_model=User)
def read_users_id(current_user: User = Depends(get_current_user)):
    return current_user