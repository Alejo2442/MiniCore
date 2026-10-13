from models.database import conectar


def obtener_reglas():
    conexion = conectar()
    reglas = conexion.execute(
        "SELECT monto_minimo, porcentaje FROM reglas ORDER BY monto_minimo"
    ).fetchall()
    conexion.close()
    return reglas


def obtener_porcentaje(total, reglas):
    porcentaje = 0
    for monto_minimo, porcentaje_regla in reglas:
        if total >= monto_minimo:
            porcentaje = porcentaje_regla
    return porcentaje
