from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: EmailStr) -> User | None:
        return self.db.query(User).filter(User.email == email).first()

    def create(self, email: EmailStr, password: str) -> User:
        user = User(email=str(email), hashed_password=hash_password(password))
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
