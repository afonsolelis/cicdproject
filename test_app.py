import pytest
from app import app

@pytest.fixture
# Arrange
def cliente():
    app.testing = True
    return app.test_client()

# Act e Assert
def test_soma_valida(cliente):
    resposta = cliente.get('/soma?a=10&b=5')
    json_data = resposta.get_json()
    assert resposta.status_code == 200
    assert json_data['resultado'] == 15

def test_soma_invalida(cliente):
    # Act
    resposta = cliente.get('/soma?a=ij&b=5')
    # Arrange
    json_data = resposta.get_json()
    # Assert
    assert resposta.status_code == 500
    assert 'erro' in json_data
