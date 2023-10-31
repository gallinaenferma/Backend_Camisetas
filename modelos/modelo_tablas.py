from sqlalchemy import Table,Column,Integer,String,BINARY
from config_bd.db import meta,engine


usuario = Table("usuario",meta,
Column("numero_documento",Integer,primary_key=True),
Column("tipo_documento",String),
Column("nombre",String),
Column("apellido",String),
Column("email",String),
Column("contraseña",String),
Column("celular",String),
Column("direccion",String)
)

estampa = Table("estampa",meta,
Column("codigo_estampa",Integer,primary_key=True),
Column("nombre_estampa",String),
Column("categoria_estampa",String),
Column("autor_estampa",String),
Column("imagen_estampa",String) #COLUMNA NO CREADA EN EL GESTOR BD
)


meta.create_all(engine)


