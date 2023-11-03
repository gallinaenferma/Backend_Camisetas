from fastapi import FastAPI
from rutas.ruta_usuario import usuarios
from rutas.ruta_estampa import estampas
from rutas.ruta_camiseta import camisetas

app = FastAPI()

#Rutas
app.include_router(usuarios)
app.include_router(estampas)
app.include_router(camisetas)