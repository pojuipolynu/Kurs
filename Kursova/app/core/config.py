from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class AppConfig(BaseSettings):
    PORT: int = 8000
    HOST: str = '0.0.0.0'
    RELOAD: bool = True
    ORIGINS: List[str] = ["http://localhost", "http://127.0.0.1:8000", "http://localhost:3000"]
    DB_USER: str = 'postgres'  
    DB_PASSWORD: str = 'password' 
    DB_HOST: str = 'postgres'
    DB_PORT: int = 5432
    DB_NAME: str = 'app_db'  
    
    # model_config = SettingsConfigDict(env_file=".env", env_prefix='APP_')

    @property
    def POSTGRES_URL(self):
        return f"postgresql+asyncpg://app_db_a0ue_user:FBxcnzlDIo7T8xtFLG1dMeBkJgIsjfqq@dpg-ctm8k6lds78s73caj700-a.oregon-postgres.render.com/app_db_a0ue"

settings = AppConfig()
