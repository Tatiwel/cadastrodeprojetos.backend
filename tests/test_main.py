from fastapi.testclient import TestClient
from app.main import app

# Cria um cliente de teste para simular requisições HTTP
client = TestClient(app)

def test_create_project():
    # Dados que serão enviados no corpo da requisição POST
    project_data = {
        "name": "Projeto Teste",
        "description": "Esse é um projeto de teste",
        "status": "ativo"
    }

    # Envia uma requisição POST para a API
    response = client.post("/projects", json=project_data)

    # Verifica se a resposta foi bem-sucedida (status 200)
    assert response.status_code == 200

    # Verifica se os dados recebidos na resposta são os esperados
    response_data = response.json()
    assert response_data["name"] == project_data["name"]
    assert response_data["description"] == project_data["description"]
    assert response_data["status"] == project_data["status"]
    assert "id" in response_data  # Verifica se o ID foi gerado
