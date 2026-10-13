# MiniCore - Comisiones de Vendedores

Aplicación web desarrollada con Flask y SQLite que calcula la comisión de cada vendedor según el total de sus ventas en un rango de fechas. El proyecto está organizado con el patrón Modelo-Vista-Controlador (MVC).

Aplicación en línea: https://minicore-rg8n.onrender.com

## Índice

- [Descripción del proyecto](#descripción-del-proyecto)
- [Estado del proyecto](#estado-del-proyecto)
- [Características](#características)
- [Demostración](#demostración)
- [Acceso al proyecto](#acceso-al-proyecto)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Base de datos](#base-de-datos)
- [Despliegue](#despliegue)
- [Desarrollador](#desarrollador)

## Descripción del proyecto

El sistema resuelve un problema común en empresas de ventas: calcular cuánto se le debe pagar a cada vendedor por comisiones en un periodo determinado.

El usuario selecciona una fecha de inicio y una fecha de fin. La aplicación suma las ventas de cada vendedor dentro de ese rango y, según el total alcanzado, le aplica un porcentaje de comisión definido en las reglas del negocio. El resultado se muestra en una tabla con el total vendido, el porcentaje aplicado y la comisión de cada vendedor.

## Estado del proyecto

Proyecto terminado y desplegado. Desarrollado como trabajo académico para la materia de Ingeniería Web.

## Características

- Filtro de ventas por rango de fechas.
- Cálculo automático de la comisión de cada vendedor según su total vendido.
- Reglas de comisión por tramos, leídas desde la base de datos y visibles en la página.
- Validación: la fecha de fin no puede ser menor a la fecha de inicio.
- Fila de totales con la suma de ventas y de comisiones del periodo.
- Datos de ejemplo cargados automáticamente al iniciar la aplicación.
- Interfaz adaptable a computadora y celular.

### Reglas de comisión

| Total vendido desde | Comisión |
|---|---|
| $500 | 4% |
| $1,000 | 7% |
| $2,000 | 10% |
| $3,000 | 13% |

Si el total vendido no llega a $500, el vendedor no recibe comisión. A cada vendedor se le aplica la regla con el monto mínimo más alto que alcance.

## Demostración

Los datos de ejemplo contienen ventas entre agosto y octubre de 2026. Algunos rangos para probar en https://minicore-rg8n.onrender.com:

| Desde | Hasta | Qué se observa | Total comisiones |
|---|---|---|---|
| 01/08/2026 | 31/08/2026 | Un vendedor no alcanza el mínimo y queda en 0% | $408.50 |
| 01/08/2026 | 31/10/2026 | Al sumar tres meses, la mayoría alcanza el 13% | $2,380.30 |
| 31/10/2026 | 01/08/2026 | Se muestra el mensaje de error de fechas | - |

## Acceso al proyecto

### En línea

https://minicore-rg8n.onrender.com

El servicio usa el plan gratuito de Render: si no recibe visitas durante un tiempo se suspende, y la primera carga puede tardar alrededor de un minuto.

### En local

Requisitos: Python 3.9 o superior, pip y Git.

1. Clonar el repositorio:
```
   git clone https://github.com/Alejo2442/MiniCore.git
   cd MiniCore
```
2. Instalar las dependencias:
```
   pip install -r requirements.txt
```
3. Ejecutar la aplicación:
```
   python app.py
```
4. Abrir en el navegador: http://127.0.0.1:5000

La base de datos `ventas.db` ya viene incluida. Si se elimina, la aplicación la vuelve a crear automáticamente a partir de `datos.sql`.

## Tecnologías utilizadas

- **Python**: lenguaje principal.
- **Flask**: framework web para las rutas, el controlador y las plantillas.
- **Jinja2**: motor de plantillas de Flask para generar el HTML con los datos.
- **SQLite**: base de datos guardada en un solo archivo, usada mediante la librería `sqlite3` de Python.
- **HTML y CSS**: interfaz de usuario.
- **Gunicorn**: servidor de producción usado en el despliegue.
- **Render**: plataforma donde está publicada la aplicación.

## Estructura del proyecto

```
MiniCore/
├── app.py
├── datos.sql
├── ventas.db
├── requirements.txt
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

- **Modelo** (`models/`): conexión a SQLite y consultas a las tablas.
  - `database.py`: conecta con la base y la crea desde `datos.sql` si no existe.
  - `venta.py`: suma las ventas de cada vendedor dentro del rango de fechas.
  - `regla.py`: obtiene las reglas de comisión y determina el porcentaje que corresponde a un total.
- **Vista** (`templates/` y `static/`): página que ve el usuario y sus estilos.
- **Controlador** (`controllers/comision_controller.py`): recibe las fechas, valida, usa los modelos, calcula las comisiones y envía los resultados a la vista.
- **`app.py`**: crea la aplicación Flask, registra el controlador y prepara la base de datos.

## Base de datos

La base tiene tres tablas relacionadas:

| Tabla | Campos | Descripción |
|---|---|---|
| `vendedores` | id, nombre | Vendedores de la empresa |
| `reglas` | id, monto_minimo, porcentaje | Tramos de comisión |
| `ventas` | id, vendedor_id, fecha, monto | Cada venta realizada; `vendedor_id` es clave foránea hacia `vendedores` |

## Despliegue

La aplicación está desplegada en Render como Web Service, conectada a este repositorio de GitHub.

| Configuración | Valor |
|---|---|
| Lenguaje | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Plan | Free |

En local se usa el servidor de desarrollo de Flask (`python app.py`). En producción se usa Gunicorn, un servidor WSGI preparado para atender varias peticiones de forma estable. Cada cambio que se sube a la rama `main` vuelve a desplegarse automáticamente.

## Desarrollador

**Alejo2442**
Ingeniería de Software - Universidad de Las Américas (UDLA)
Materia: Ingeniería Web
GitHub: https://github.com/Alejo2442
