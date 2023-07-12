import json
from app import app

def test_get_all_musicas():
    response = app.test_client().get('/musicas')
    res = json.loads(response.data.decode('utf-8')).get("Musicas")
    assert type(res) is list
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert type(res[2]) is dict
    assert res[0]["nome"] == "Wish You Were Here"
    assert res[1]["ano"] == 1986
    assert res[2]["artista"] == "Pharrell Williams"
    assert response.status_code == 200
    
