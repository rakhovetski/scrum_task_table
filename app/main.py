from fastapi import FastAPI

from app.projects.router import router as projects_router


app = FastAPI()


app.include_router(projects_router)