from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Verifica se está rodando no Docker (usando variável padrão ou fallback)
env_file = os.getenv("ENV_FILE", ".env.development")
load_dotenv(dotenv_path=env_file)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
