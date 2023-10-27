from fastapi import FastAPI
from rutas.ruta_usuario import usuarios

app = FastAPI()

#Rutas
app.include_router(usuarios)