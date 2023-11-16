from fastapi import FastAPI
from rutas.ruta_usuario import usuarios
from rutas.ruta_estampa import estampax
from rutas.ruta_camiseta import camisetas
from rutas.ruta_camiseta_estampada import camisetas_estampadas 
from rutas.ruta_carrito import carritos

app = FastAPI()

#Rutas
app.include_router(usuarios)
app.include_router(estampax)
app.include_router(camisetas)
app.include_router(camisetas_estampadas)
app.include_router(carritos)