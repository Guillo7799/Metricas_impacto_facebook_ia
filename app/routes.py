from flask import Blueprint, render_template
from app.services.facebook_analysis import obtener_metricas_dashboard

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    datos = obtener_metricas_dashboard()
    print(datos)  # temporal para revisar en consola
    return render_template("dashboard.html", **datos)