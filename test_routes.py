import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Credenciais do usuário
USERNAME = "admin"
PASSWORD = "admin"

def get_basic_auth_header():
    return {
        "Authorization": f"Basic {USERNAME}:{PASSWORD}"
    }

def test_get_producao_without_auth():
    response = client.get("/producao")
    assert response.status_code == 401

def test_get_producao_with_auth():
    response = client.get("/producao", auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

def test_get_processamento_without_auth():
    response = client.get("/processamento")
    assert response.status_code == 401

def test_get_processamento_with_auth():
    response = client.get("/processamento", auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

def test_get_comercializacao_without_auth():
    response = client.get("/comercializacao")
    assert response.status_code == 401

def test_get_comercializacao_with_auth():
    response = client.get("/comercializacao", auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

def test_get_importacao_without_auth():
    response = client.get("/importacao")
    assert response.status_code == 401

def test_get_importacao_with_auth():
    response = client.get("/importacao", auth=(USERNAME, PASSWORD))
    assert response.status_code == 200

def test_get_exportacao_without_auth():
    response = client.get("/exportacao")
    assert response.status_code == 401

def test_get_exportacao_with_auth():
    response = client.get("/exportacao", auth=(USERNAME, PASSWORD))
    assert response.status_code == 200
