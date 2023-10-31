from fastapi import APIRouter,Response,status
from config_bd.db import conn 
from modelos.modelo_tablas import estampa #Tabla usuario

estampas = APIRouter()


@estampas.get("/estampas", tags=["Estampa"])
def inicio():
    return "Hola Inicio"