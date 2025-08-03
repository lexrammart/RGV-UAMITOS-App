def obtener_registro_por_campo(tabla, campo, valor, connect_func):
    try:
        conexion = connect_func()
        cursor = conexion.cursor()
        query = f"SELECT * FROM {tabla} WHERE {campo} = %s"
        cursor.execute(query, (valor,))
        fila = cursor.fetchone()

        if fila is None:
            return None

        # Obtener nombres de columnas
        columnas = [desc[0] for desc in cursor.description]
        resultado = dict(zip(columnas, fila))

        cursor.close()
        conexion.close()
        return resultado

    except Exception as e:
        print("Error al obtener el registro:", e)
        return None


def insertar_registro(nombre_tabla, datos_dict, conexion_func):
    try:
        conexion = conexion_func()
        cursor = conexion.cursor()

        columnas = ", ".join(datos_dict.keys())
        placeholders = ", ".join(["%s"] * len(datos_dict))
        valores = tuple(datos_dict.values())

        query = f"INSERT INTO {nombre_tabla} ({columnas}) VALUES ({placeholders})"
        cursor.execute(query, valores)
        conexion.commit()

        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"❌ Error al insertar en {nombre_tabla}:", e)
        return False


def actualizar_campo(
    tabla, campo_objetivo, nuevo_valor, campo_condicion, valor_condicion, connect_func
):
    try:
        conexion = connect_func()
        cursor = conexion.cursor()
        query = f"UPDATE {tabla} SET {campo_objetivo} = %s WHERE {campo_condicion} = %s"
        cursor.execute(query, (nuevo_valor, valor_condicion))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("Error al actualizar campo:", e)
        return False


def actualizar_campos(
    tabla, campos_valores, campo_condicion, valor_condicion, connect_func
):
    try:
        conexion = connect_func()
        cursor = conexion.cursor()

        sets = ", ".join(f"{campo} = %s" for campo in campos_valores.keys())
        valores = list(campos_valores.values()) + [valor_condicion]

        query = f"UPDATE {tabla} SET {sets} WHERE {campo_condicion} = %s"
        cursor.execute(query, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("❌ Error al actualizar campos:", e)
        return False
