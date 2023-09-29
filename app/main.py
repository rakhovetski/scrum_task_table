from fastapi import FastAPI


from app.projects.problems.router import router as problems_router
from app.projects.router import router as projects_router


app = FastAPI()


app.include_router(projects_router)
# app.include_router(problems_router)