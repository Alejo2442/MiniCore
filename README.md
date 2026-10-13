# MiniCore - Comisiones de Vendedores

Aplicación en Flask y SQLite, organizada con el patrón MVC, que calcula la comisión de cada vendedor según lo que vendió en un rango de fechas.

## Cómo funciona

1. El usuario elige una fecha de inicio y una de fin.
2. Se suman las ventas de cada vendedor dentro de ese rango.
3. Al total se le aplica el porcentaje de la regla con el monto mínimo más alto que alcance.
4. Se muestra una tabla con el total vendido, el porcentaje y la comisión de cada vendedor.

## Reglas de comisión

| Total vendido desde | Porcentaje |
|---|---|
| $500 | 4% |
| $1,000 | 7% |
| $2,000 | 10% |
| $3,000 | 13% |

Menos de $500 no recibe comisión.

## Estructura (MVC)

```
MiniCore/
├── app.py
├── datos.sql
├── ventas.db
├── models/
│   ├── database.py
│   ├── venta.py
│   └── regla.py
├── controllers/
│   └── comision_controller.py
├── templates/
│   └── index.html
└── static/
    └── style.css
```

- Modelo (`models/`): conexión a SQLite y consultas a las tablas.
- Vista (`templates/` y `static/`): página que ve el usuario.
- Controlador (`controllers/`): recibe las fechas, usa los modelos, calcula las comisiones y envía los resultados a la vista.
- `app.py`: crea la aplicación Flask y registra el controlador.

## Ejecutar en local

```
pip install -r requirements.txt
python app.py
```

Abrir http://127.0.0.1:5000. Los datos van de agosto a octubre de 2026.
