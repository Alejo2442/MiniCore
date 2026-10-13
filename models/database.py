import os
import sqlite3

CARPETA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DATOS = os.path.join(CARPETA, "ventas.db")
SCRIPT_DATOS = os.path.join(CARPETA, "datos.sql")


def conectar():
    return sqlite3.connect(BASE_DATOS)


def crear_base():
    if not os.path.exists(BASE_DATOS):
        with open(SCRIPT_DATOS, encoding="utf-8") as archivo:
            conexion = conectar()
            conexion.executescript(archivo.read())
            conexion.close()
