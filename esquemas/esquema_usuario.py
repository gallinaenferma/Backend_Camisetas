from pydantic import BaseModel

class Usuario(BaseModel):
    numero_documento:int
    tipo_documento:str
    nombre:str
    apellido:str
    email:str
    contraseña:str
    celular:str
    direccion:str



