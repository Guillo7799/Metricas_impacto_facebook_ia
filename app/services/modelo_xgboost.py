import joblib
from pathlib import Path
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

    rmse = mean_squared_error(
        y_test,
        predicciones
    ) ** 0.5

    r2 = r2_score(
        y_test,
        predicciones
    )

    importancia = sorted(
        zip(columnas, modelo.feature_importances_),
        key=lambda x: x[1],
        reverse=True
    )

    return modelo, mae, rmse, r2, importancia

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