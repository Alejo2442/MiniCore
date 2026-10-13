from models.database import conectar


def total_por_vendedor(inicio, fin):
    conexion = conectar()
    totales = conexion.execute(
        """
        SELECT vendedores.nombre, COALESCE(SUM(ventas.monto), 0)
        FROM vendedores
        LEFT JOIN ventas
            ON ventas.vendedor_id = vendedores.id
            AND ventas.fecha BETWEEN ? AND ?
        GROUP BY vendedores.id
        ORDER BY vendedores.nombre
        """,
        (inicio, fin),
    ).fetchall()
    conexion.close()
    return totales
