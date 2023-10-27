from sqlalchemy import Table,Column,Integer,String
from config_bd.db import meta,engine


usuario = Table("usuario",meta,
Column("numero_documento",Integer,primary_key=True),
Column("tipo_documento",String),
Column("nombre",String),
Column("apellido",String),
Column("email",String),
Column("contraseña",String),
Column("celular",String),
Column("direccion",String),

)
meta.create_all(engine)


