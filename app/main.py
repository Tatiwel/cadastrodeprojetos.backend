from fastapi import FastAPI
from app.api.routes import router
from app.db.session import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Cria tabelas se não existirem

app.include_router(router)
