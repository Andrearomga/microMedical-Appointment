from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DBUSER')
db_password = os.getenv('DBPASS')
db_url = os.getenv('DBURL')
db_name = os.getenv('DBNAME')

# Imprimir valores para depuración
print(f"DB User: {db_user}")
print(f"DB Password: {db_password}")
print(f"DB URL: {db_url}")
print(f"DB Name: {db_name}")

if not db_user or not db_password or not db_url or not db_name:
    raise ValueError("Una o más variables de entorno no están definidas.")

Base = declarative_base()

DATABASE_URL = f'mysql+pymysql://{db_user}:{db_password}@{db_url}/{db_name}'
print(f"Database URL: {DATABASE_URL}")

try:
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    session_local = sessionmaker(bind=engine)
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
