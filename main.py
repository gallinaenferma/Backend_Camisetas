from fastapi import FastAPI
from rutas.ruta_usuario import usuarios
from rutas.ruta_estampa import estampas
from rutas.ruta_camiseta import camisetas
from rutas.ruta_camiseta_estampada import camisetas_estampadas 

app = FastAPI()

#Rutas
app.include_router(usuarios)
app.include_router(estampas)
app.include_router(camisetas)
app.include_router(camisetas_estampadas)