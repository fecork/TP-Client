import uvicorn

from fastapi import FastAPI
from app.infraestructure.controlador import routers
from app.infraestructure.adapter.openai_start import login_openai

app = FastAPI()

app.include_router(routers.router)
login_openai()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=3000)
