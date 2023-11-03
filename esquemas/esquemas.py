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

class Estampa(BaseModel):
    codigo_estampa:int
    nombre_estampa:str
    categoria_estampa:str
    autor_estampa:str
    imagen_estampa:str

class Camiseta(BaseModel):
    codigo_camiseta:int
    talla_camiseta:str
    color_camiseta:str
    genero_camiseta:str
    #imagen_estampa:str





