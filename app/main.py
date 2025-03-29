from fastapi import FastAPI
from app.database import init_db
from app.models import user, post, comment

app = FastAPI(title="Mini Blog API")

from app.api import auth, users
app.include_router(auth.router)
app.include_router(users.router)


@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to Mini Blog API"}
