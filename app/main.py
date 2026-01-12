from fastapi import FastAPI
from app.api.v1 import auth, users
app = FastAPI(title="FastAPI Base")

app.include_router(auth.router)
app.include_router(users.router)