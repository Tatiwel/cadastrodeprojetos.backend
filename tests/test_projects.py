def test_get_nonexistent_project(client):
    response = client.get("/projects/42")
    assert response.status_code == 404
