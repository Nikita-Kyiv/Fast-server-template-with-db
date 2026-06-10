import pytest

@pytest.mark.asyncio
async def test_create_example(async_client):
    response = await async_client.post("/example", data={"example_field": "test value"})
    assert response.status_code == 200
    data = response.json()
    assert data["example_field"] == "test value"