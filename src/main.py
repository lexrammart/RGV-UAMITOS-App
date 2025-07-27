import os
from login import login
from db_usuario import inicializar_bd

# Crear la carpeta databases si no existe
db_dir = os.path.join(os.path.dirname(__file__), "..", "database")
os.makedirs(db_dir, exist_ok=True)

if __name__ == "__main__":
    inicializar_bd("usuarios.db")
    login()
