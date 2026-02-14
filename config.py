import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/income_survey")
    DB_NAME = os.getenv("DB_NAME", "income_survey")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME", "responses")
