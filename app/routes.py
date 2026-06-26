from flask import Blueprint, render_template
from app.services.facebook_analysis import obtener_metricas_dashboard

main = Blueprint("main", __name__)

@main.route("/")
def dashboard():
    datos = obtener_metricas_dashboard()
    return render_template("dashboard.html", **datos)