from login import login
from db_connection import connect_db  # insertar_usuarios_temporales


def main():
    connection = connect_db()
    if connection:
        print("La base de datos está lista")

    login()
    # insertar_usuarios_temporales()


if __name__ == "__main__":
    main()
