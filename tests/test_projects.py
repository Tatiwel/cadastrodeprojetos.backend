import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_projects():
    response = client.get("/projects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_count_project_status():
    response = client.get("/projects/projects-status")
    assert response.status_code == 200
    assert "Ativo" in response.json()
    assert "Pausado" in response.json()
    assert "Finalizado" in response.json()

def test_get_project():
    response = client.get("/projects/1")
    if response.status_code == 404:
        assert response.json()["detail"] == "Projeto não encontrado"
    else:
        assert response.status_code == 200
        assert "id" in response.json()

def test_create_project():
    new_project = {
        "name": "Novo Projeto",
        "description": "Descrição do projeto",
        "status": "Ativo"
    }
    response = client.post("/projects/", json=new_project)
    assert response.status_code == 200
    assert response.json()["name"] == new_project["name"]

def test_update_project():
    update_data = {
        "name": "Projeto Atualizado",
        "description": "Descrição atualizada",
        "status": "Pausado"
    }
    response = client.put("/projects/1", json=update_data)
    if response.status_code == 404:
        assert response.json()["detail"] == "Projeto não encontrado"
    else:
        assert response.status_code == 200
        assert response.json()["name"] == update_data["name"]

def test_delete_project():
    response = client.delete("/projects/1")
    if response.status_code == 404:
        assert response.json()["detail"] == "Projeto não encontrado"
    else:
        assert response.status_code == 200
        assert response.json()["ok"] == True
