from fastapi import FastAPI

from app.projects.router import router as projects_router
from app.profiles.router import router_profiles, auth_router


app = FastAPI()


app.include_router(projects_router)
app.include_router(router_profiles)
app.include_router(auth_router)