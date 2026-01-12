from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./dev.db"
    APP_NAME: str = "FastAPI Base"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
