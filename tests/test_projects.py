import pytest
from fastapi.testclient import TestClient
from app.main import app
import json

client = TestClient(app)

@pytest.fixture
def sample_data():
    new_project = {
        "name": "Teste",
        "description": "Descrição do projeto de teste",
        "status": "Ativo"
    }

    # Cria o projeto no banco de dados
    response = client.post("/projects/", json=new_project)
    print("\nA saída de sample_data foi 200!: ",  json.dumps(response.json(), indent=4, ensure_ascii=False))
    assert response.status_code == 200
    return response.json()

def test_create_project(sample_data):
    response = client.post("/projects/", json=sample_data)
    if response.status_code == 422:
        assert response.json()["detail"] == "Erro de validação"
    else:
        assert response.status_code == 200
        assert response.json()["name"] == sample_data["name"]
        assert response.json()["description"] == sample_data["description"]
        assert response.json()["status"] == sample_data["status"]
        print("\nSaída test_create_project: ",  json.dumps(response.json(), indent=4, ensure_ascii=False))

def test_list_projects():
    response = client.get("/projects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print("\nSaída test_list_projects:", json.dumps(response.json(), indent=4, ensure_ascii=False))

def test_count_project_status():
    response = client.get("/projects/projects-status")
    assert response.status_code == 200
    assert "Ativo" in response.json()
    assert "Pausado" in response.json()
    assert "Finalizado" in response.json()
    print("\nSaída test_count_project_status: ", response.json())

def test_get_project():
    response = client.get("/projects/000")
    if response.status_code == 404:
        assert response.json()["detail"] == "Projeto não encontrado"
    else:
        assert response.status_code == 200
        assert "id" in response.json()
    print("\nSaída test_get_project: ", response.json())

def test_update_project(sample_data):
    update_data = {
        "name": "Projeto Atualizado - Teste",
        "description": "Descrição atualizada do projeto de teste",
        "status": "Pausado"
    }
    response = client.put(f"/projects/{sample_data['id']}", json=update_data)
    if response.status_code == 404:
        assert response.json()["detail"] == "Projeto não encontrado"
    else:
        assert response.status_code == 200
        assert response.json()["name"] == update_data["name"]
        assert response.json()["description"] == update_data["description"]
        assert response.json()["status"] == update_data["status"]
        print("\nSaída test_update_project: ", json.dumps(response.json(), indent=4, ensure_ascii=False))

def test_delete_project(sample_data):
    response = client.delete(f"/projects/{sample_data['id']}")
    if response.status_code == 404:
        assert response.json()["detail"] == "Projeto não encontrado"
    else:
        assert response.status_code == 200
        assert response.json()["ok"] == True
        print("\nSaída test_delete_project: ", json.dumps(response.json(), indent=4, ensure_ascii=False))
