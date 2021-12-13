import os 

class Settings:
    JWT_SECRET = os.environ["JWT_SECRET"]
    JWT_ALGORITHM = os.environ["JWT_ALGORITHM"]

settings = Settings()