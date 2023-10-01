import asyncio
import json
import pytest
from httpx import AsyncClient
from sqlalchemy import insert

from app.config import settings
from app.projects.models import Project
from app.projects.problems.models import Problem
from app.profiles.models import Profile
from app.database import engine, Base, async_session_maker
from app.main import app as fastapi_app


@pytest.fixture(scope='session', autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f'app/tests/mock_{model}.json', encoding='utf-8') as file:
            return json.load(file)
        
    projects = open_mock_json('projects')
    problems = open_mock_json('problems')
    profiles = open_mock_json('profiles')

    async with async_session_maker() as session:
        for Model, values in [
            (Project, projects),
            (Problem, problems),
            (Profile, profiles)
        ]:
            query = insert(Model).values(values)
            await session.execute(query)

        await session.commit()


@pytest.fixture(scope='session')
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='function')
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope='session')
async def authenticated_ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        await ac.post('/auth/login', json={
            'email': 'test@test.com',
            'password': 'test1234'
        })
        assert ac.cookies['access_token']
        yield ac