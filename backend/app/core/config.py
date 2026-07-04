from pydantic import BaseModel


class Settings(BaseModel):
    DATABASE_URL: str = (
        "postgresql://cardvalue_user:cardvalue_password@localhost:5432/cardvalue_db"
    )


settings = Settings()