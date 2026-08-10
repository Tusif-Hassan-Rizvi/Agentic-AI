from urllib.parse import quote_plus
from pydantic_settings import Base, SettingsConfigDict


class Settings(Base):
    
    PROJECT_NAME: str = "Expense Tracker API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    # Database Settings (Loaded from .env)
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str    
 
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")    

    @property
    def DATABASE_URL(self) -> str:
        encoded_password = quote_plus(self.DB_PASSWORD)
        return f"postgresql+psycopg2://{self.DB_USER}:{encoded_password}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

