import pandas as pd
import plotly.express as px
import plotly.io as pio

from app.services.preparacion import cargar_dataset, limpiar_dataset


def obtener_dataset_limpio():
    df = cargar_dataset()
    df = limpiar_dataset(df)
    return df


def generar_resumen_eda(df):
    resumen = {
        "total_registros": len(df),
        "total_columnas": len(df.columns),
        "promedio_interacciones": round(df["Total Interactions"].mean(), 2),
        "max_interacciones": int(df["Total Interactions"].max()),
        "tipo_mas_frecuente": df["Type"].mode()[0],
        "promedio_alcance": round(df["Lifetime Post Total Reach"].mean(), 2),
    }

    return resumen


def generar_graficos_eda():
    df = obtener_dataset_limpio()

    grafico_tipos = px.bar(
        df.groupby("Type")["Total Interactions"].mean().reset_index(),
        x="Type",
        y="Total Interactions",
        title="Promedio de interacciones por tipo de publicación"
    )

    grafico_paid = px.bar(
        df.groupby("Paid")["Total Interactions"].mean().reset_index(),
        x="Paid",
        y="Total Interactions",
        title="Promedio de interacciones: pagadas vs orgánicas"
    )

    grafico_hora = px.line(
        df.groupby("Post Hour")["Total Interactions"].mean().reset_index(),
        x="Post Hour",
        y="Total Interactions",
        title="Promedio de interacciones por hora de publicación"
    )

    grafico_dia = px.bar(
        df.groupby("Post Weekday")["Total Interactions"].mean().reset_index(),
        x="Post Weekday",
        y="Total Interactions",
        title="Promedio de interacciones por día de la semana"
    )

    columnas_numericas = df.select_dtypes(include=["int64", "float64"])

    correlaciones = (
        columnas_numericas
        .corr()["Total Interactions"]
        .sort_values(ascending=False)
        .reset_index()
    )

    correlaciones.columns = ["Variable", "Correlacion"]

    grafico_correlacion = px.bar(
        correlaciones.head(10),
        x="Variable",
        y="Correlacion",
        title="Variables más relacionadas con Total Interactions"
    )

    resumen = generar_resumen_eda(df)

    return {
        "resumen": resumen,
        "correlaciones": correlaciones,
        "grafico_tipos_html": pio.to_html(grafico_tipos, full_html=False),
        "grafico_paid_html": pio.to_html(grafico_paid, full_html=False),
        "grafico_hora_html": pio.to_html(grafico_hora, full_html=False),
        "grafico_dia_html": pio.to_html(grafico_dia, full_html=False),
        "grafico_correlacion_html": pio.to_html(grafico_correlacion, full_html=False),
    }


if __name__ == "__main__":
    resultados = generar_graficos_eda()

    print("\nFASE 2 - EXPLORACIÓN DE DATOS")
    print("=" * 60)

    print("\nResumen general:")
    for clave, valor in resultados["resumen"].items():
        print(f"{clave}: {valor}")

    print("\nCorrelaciones principales con Total Interactions:")
    print(resultados["correlaciones"].head(10))