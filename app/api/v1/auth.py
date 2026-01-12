from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.security import verify_password, create_access_token
from app.core.types import DbSession
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: DbSession):
    repo = UserRepository(db)
    if repo.get_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = repo.create(user.email, user.password)
    return {"id": user.id, "email": user.email}

@router.post("/login")
def login(db: DbSession, form_data: OAuth2PasswordRequestForm = Depends()):
    repo = UserRepository(db)
    user = repo.get_by_email(form_data.username)

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    token = create_access_token({"sub": user.email})

    return {"access_token": token, "token_type": "bearer"}
