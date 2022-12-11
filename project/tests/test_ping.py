# project/tests/test_ping.py


from app import main


def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    data = response.json()
    assert data["environment"]
    assert data["ping"]
    assert data["testing"]
    assert data["instance_id"]
