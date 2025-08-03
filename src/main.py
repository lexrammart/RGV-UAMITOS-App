from login import login
from db_connection import connect_db  # , insertar_usuarios_iniciales


def main():
    connection = connect_db()
    if connection:
        print("La base de datos está lista")

    # insertar_usuarios_iniciales()
    login()


if __name__ == "__main__":
    main()
