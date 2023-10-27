from fastapi import APIRouter
from config_bd.db import conn
from modelos.modelo_usuario import usuario #tabla
from esquemas.esquema_usuario import Usuario
from cryptography.fernet import Fernet # Cifrar contraseña

key=Fernet.generate_key()
f=Fernet(key)

usuarios = APIRouter()

@usuarios.get("/usuarios")
def hola():
    return "Hola mundo"

@usuarios.get("/usuarios")
def mostrar_usuario():
    return conn.execute(usuario.select()).fetchall()

@usuarios.post("/usuarios")
def registrar_usuario( user : Usuario):
    nuevo_usuario = {"numero_documento": user.numero_documento ,"tipo_documento":user.tipo_documento,
    "nombre": user.nombre,"apellido":user.apellido,"email":user.email,"celular":user.celular,
    "direccion":user.direccion}
    nuevo_usuario["contraseña"] = f.encrypt(user.contraseña.encode("utf-8"))
    resultado = conn.execute(usuario.insert().values( nuevo_usuario))
    print(resultado)
    return "hola mundo 2 "

