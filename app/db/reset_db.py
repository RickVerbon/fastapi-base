from app.db.session import engine
from app.db.base import Base


def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_db()
    print("Database reset completed.")