from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import Crop_recommendation



app = FastAPI()
app.include_router(Crop_recommendation.router)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # quién puede hacer peticiones
    allow_credentials=True,
    allow_methods=["*"],             # permite todos los métodos: GET, POST, PUT, DELETE
    allow_headers=["*"],             # permite todas las cabeceras
)

@app.get("/")
def read_root():
    return {"Helo": "World"}


