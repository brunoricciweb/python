from fastapi.testclient import TestClient
from main import app, products

client = TestClient(app)



def test_get_productos():
    response = client.get('/productos')
    
    print('la respuesta es:', response.json())
    assert response.json() == [{'id': 1, 'nombre': 'Yerba sin palo', 'categoria': 'alimentos', 'precio': 1234.55}, {'id': 2, 'nombre': 'Queso cremoso', 'categoria': 'lacteos', 'precio': 3566.0}]



