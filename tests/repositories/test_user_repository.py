import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.repositories.user import UserRepository
from app.models.user import Base

# In-memory SQLite, volledig los van main test.db
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_user(db_session):
    repo = UserRepository(db_session)
    user = repo.create("test@example.com", "secret123")
    assert user.id is not None
    assert user.email == "test@example.com"

def test_get_by_email(db_session):
    repo = UserRepository(db_session)
    repo.create("a@b.com", "pass")
    user = repo.get_by_email("a@b.com")
    assert user is not None
    assert user.email == "a@b.com"

def test_get_nonexistent_user(db_session):
    repo = UserRepository(db_session)
    user = repo.get_by_email("notfound@example.com")
    assert user is None
