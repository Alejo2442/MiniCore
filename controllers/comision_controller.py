from flask import Blueprint, render_template, request
from models.venta import total_por_vendedor
from models.regla import obtener_reglas, obtener_porcentaje

comision_bp = Blueprint("comisiones", __name__)


@comision_bp.route("/")
def index():
    inicio = request.args.get("inicio", "")
    fin = request.args.get("fin", "")
    reglas = obtener_reglas()
    resultados = []
    error = ""

    if inicio and fin:
        if fin < inicio:
            error = "La fecha de fin no puede ser menor a la fecha de inicio."
        else:
            for nombre, total in total_por_vendedor(inicio, fin):
                porcentaje = obtener_porcentaje(total, reglas)
                resultados.append({
                    "vendedor": nombre,
                    "total": total,
                    "porcentaje": porcentaje,
                    "comision": total * porcentaje / 100,
                })

    return render_template(
        "index.html",
        inicio=inicio,
        fin=fin,
        resultados=resultados,
        error=error,
        reglas=reglas,
    )
