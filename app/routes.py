from flask import Blueprint, render_template

from app.services.exploracion import generar_graficos_eda
from app.services.modelo_xgboost import (
    entrenar_modelo,
    generar_insights,
    generar_grafico_importancia
)

main = Blueprint("main", __name__)


@main.route("/")
def dashboard():
    eda = generar_graficos_eda()

    _, mae, rmse, r2, importancia = entrenar_modelo()

    insights = generar_insights(mae, r2, importancia)
    grafico_importancia = generar_grafico_importancia(importancia)

    return render_template(
        "dashboard.html",
        resumen=eda["resumen"],
        grafico_tipos=eda["grafico_tipos_html"],
        grafico_paid=eda["grafico_paid_html"],
        grafico_hora=eda["grafico_hora_html"],
        grafico_dia=eda["grafico_dia_html"],
        grafico_correlacion=eda["grafico_correlacion_html"],
        grafico_importancia=grafico_importancia,
        mae=round(mae, 2),
        rmse=round(rmse, 2),
        r2=round(r2, 4),
        insights=insights
    )