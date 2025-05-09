import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient
from app.main import app
from app.db.session import Base, get_db

# 1) Engine de teste em memória
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 2) Sessão de teste
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# 3) Fixture para criar/dropar tabelas e prover sessão
@pytest.fixture(scope="session")
def db():
    # Cria todas as tabelas no DB em memória
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

# 4) Fixture para o TestClient com override de get_db
@pytest.fixture(scope="module")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client
    # opcional: limpar overrides
    app.dependency_overrides.clear()
