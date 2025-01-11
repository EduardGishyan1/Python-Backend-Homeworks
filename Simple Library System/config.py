from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE:str
    COLLECTION:str
    MONGO_URI:str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Settings()