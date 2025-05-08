from fastapi import FastAPI
from app.api.routes import api_router
from app.db.session import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Cria tabelas se não existirem

# Inclui as rotas da API
app.include_router(api_router)

# Endpoint de teste
@app.get("/")
def read_root():
    return {"Hello": "API está ativa no ambiente;"}
