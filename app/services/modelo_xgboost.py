import joblib
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.io as pio

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)
from xgboost import XGBRegressor

from app.services.ingenieria import preparar_datos_modelo


def entrenar_modelo():

    X_train, X_test, y_train, y_test, columnas = preparar_datos_modelo()

    modelo = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        random_state=42
    )

    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)

    mae = mean_absolute_error(y_test, predicciones)
    rmse = mean_squared_error(y_test, predicciones) ** 0.5
    r2 = r2_score(y_test, predicciones)

    importancia = sorted(
        zip(columnas, modelo.feature_importances_),
        key=lambda x: x[1],
        reverse=True
    )

    return modelo, mae, rmse, r2, importancia


def generar_grafico_importancia(importancia):
    df_importancia = pd.DataFrame(
        importancia[:10],
        columns=["Variable", "Importancia"]
    )

    grafico = px.bar(
        df_importancia,
        x="Importancia",
        y="Variable",
        orientation="h",
        title="Variables más importantes del modelo XGBoost",
        labels={
            "Importancia": "Importancia",
            "Variable": "Variable"
        }
    )

    grafico.update_layout(
        yaxis=dict(autorange="reversed")
    )

    return pio.to_html(grafico, full_html=False)


def generar_insights(mae, r2, importancia):

    insights = []

    insights.append(
        f"El modelo logró explicar aproximadamente el {r2 * 100:.0f}% de la variabilidad de las interacciones."
    )

    insights.append(
        f"La variable con mayor influencia fue '{importancia[0][0]}'."
    )

    insights.append(
        f"El error absoluto medio fue de {mae:.2f} interacciones por publicación."
    )

    insights.append(
        "El alcance de una publicación influye significativamente en la cantidad de interacciones obtenidas."
    )

    insights.append(
        "El modelo XGBoost permite estimar el impacto esperado de una publicación a partir de sus métricas de rendimiento."
    )

    return insights


def guardar_modelo(modelo):

    carpeta = Path(__file__).resolve().parents[2] / "models"
    carpeta.mkdir(exist_ok=True)

    ruta = carpeta / "xgboost_model.pkl"

    joblib.dump(modelo, ruta)

    return ruta


if __name__ == "__main__":

    modelo, mae, rmse, r2, importancia = entrenar_modelo()
    ruta = guardar_modelo(modelo)

    print("\nMODELO ENTRENADO")
    print("=" * 60)

    print(f"MAE : {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R²  : {r2:.4f}")

    print("\nTOP 10 VARIABLES")

    for nombre, valor in importancia[:10]:
        print(f"{nombre:65} {valor:.4f}")

    print(f"\nModelo guardado en:\n{ruta}")