from fastapi import FastAPI
from app.database import init_db
from app.models import user, post, comment

app = FastAPI(title="Mini Blog API")

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to Mini Blog API"}
