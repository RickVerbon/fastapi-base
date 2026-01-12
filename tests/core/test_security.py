from datetime import timedelta, datetime, timezone

from jose import jwt

from app.config import settings
from app.core.security import create_access_token
from app.core.security import hash_password, verify_password

password = "s3cret!"


def test_hash_password():
    hashed = hash_password(password)

    assert isinstance(hashed, (str, bytes))
    assert hashed != password


def test_verify_password():
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True
    assert verify_password("wrongpassword", hashed) is False


def test_create_access_token():
    data = {"sub": "user_id"}
    expires_delta = timedelta(minutes=15)

    token = create_access_token(data, expires_delta)
    decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    assert decoded["sub"] == "user_id"
    assert "exp" in decoded

    exp_time = datetime.fromtimestamp(decoded["exp"], tz=timezone.utc)
    expected_exp_time = datetime.now(timezone.utc) + expires_delta

    assert abs((exp_time - expected_exp_time).total_seconds()) < 5  # Allow small time difference
