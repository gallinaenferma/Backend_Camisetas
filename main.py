from fastapi import FastAPI
from rutas.ruta_usuario import usuarios
from rutas.ruta_estampa import estampas

app = FastAPI()

#Rutas
app.include_router(usuarios)
app.include_router(estampas)