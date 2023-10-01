import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "title,description,status_code", [
        ("HTML Project", "somedescription", 201),
        ("Another Project", None, 409),
        (None, "somedescription", 201),
    ]
)
async def test_create_project(title, description, status_code, ac: AsyncClient):
    response = await ac.post('/projects', json={
        "title": title,
        "description": description,
    })

    assert response.status_code == status_code
    