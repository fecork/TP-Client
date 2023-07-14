import json
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from app.main import app

client = TestClient(app)


def test_query_cognitive():
    request_data = {"question": "control FAN"}
    response = client.post(
        "/generate/chat", data=json.dumps(jsonable_encoder(request_data))
    )
    assert response.status_code == 200
