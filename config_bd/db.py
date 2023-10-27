from sqlalchemy import create_engine,MetaData

DATABASE_URL = "postgresql://postgres:septiembre9@localhost:5432/Camisetas"

engine=create_engine(DATABASE_URL)

conn=engine.connect()

meta = MetaData()

