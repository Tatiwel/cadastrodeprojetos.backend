# Cria um cliente de teste para simular requisições HTTP

def test_create_project(client):             # <-- usa client da fixture
    payload = {
        "name": "Projeto Teste",
        "description": "Esse é um projeto de teste",
        "status": "Ativo"
    }
    response = client.post("/projects", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == payload["name"]
    assert data["description"] == payload["description"]
    assert data["status"] == payload["status"]
    assert "id" in data
