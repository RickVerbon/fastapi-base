import re
from datetime import datetime

from pydantic import BaseModel, EmailStr, field_validator


class UserCreate(BaseModel):
    email: EmailStr
    password: str


    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value) < 12:
            raise ValueError("Password must be at least 12 characters long")

        if value.isdigit():
            raise ValueError("Password cannot be entirely numeric")

        if not re.search(r"[A-Za-z]", value):
            raise ValueError("Password must contain at least one letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain at least one digit")

        return value


    @field_validator('password')
    @classmethod
    def password_not_contains_email(cls, password: str, values) -> str:
        email = values.data.get("email")
        if email and email.split('@')[0].lower() in password:
            raise ValueError("Password cannot contain parts of the email address")

        return password


class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    created_at: datetime

    class ConfigDict:
        from_attributes = True