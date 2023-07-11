import uvicorn

from fastapi import FastAPI
from app.infraestructure.controlador import routers


app = FastAPI()


app.include_router(routers.router)


if __name__ == "__main__":

    uvicorn.run(app, host="localhost", port=8080)
