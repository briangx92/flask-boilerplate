from flask_boilerplate import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_index(client):
    response = client.get('/')
    assert response.data == b'This is a flask-boilerplate project, not to be used in production.'

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello World!'

    response = client.get('/hello?name="Jim"')
    assert response.data == b'Hello Jim!'
