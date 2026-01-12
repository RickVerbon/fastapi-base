import pytest
from pydantic import EmailStr

from app.schemas.user import UserCreate

email: EmailStr = "test@gmail.com"

def test_valid_password():
    user = UserCreate(
        email=email,
        password="StrongPass123"
    )

    assert user.password == "StrongPass123"


def test_password_too_short():
    with pytest.raises(ValueError, match="at least 12"):
        UserCreate(
            email=email,
            password="Short1"
        )

def test_password_contains_email():
    with pytest.raises(ValueError, match="email"):
        UserCreate(
            email=email,
            password="test1223213213131"
        )

def test_password_only_digit():
    with pytest.raises(ValueError, match="numeric"):
        UserCreate(
            email=email,
            password="21313131232131231"
        )

def test_password_no_digit():
    with pytest.raises(ValueError, match="digit"):
        UserCreate(
            email=email,
            password="NoDigitsHere!"
        )

def test_password_no_letter():
    with pytest.raises(ValueError, match="letter"):
        UserCreate(
            email=email,
            password="12345678!@@!90123"
        )