import pandas as pd
import plotly.express as px
import plotly.io as pio


def cargar_datos():
    df = pd.read_csv("data/publicaciones_facebook.csv")

    df["interacciones"] = (
        df["reacciones"] +
        df["comentarios"] +
        df["compartidos"] +
        df["clics"]
    )

    df["engagement"] = (df["interacciones"] / df["alcance"]) * 100

    return df


def obtener_metricas_dashboard():
    df = cargar_datos()

    total_publicaciones = len(df)
    alcance_total = int(df["alcance"].sum())
    engagement_promedio = round(df["engagement"].mean(), 2)

    mejor_publicacion = df.sort_values(
        by="engagement",
        ascending=False
    ).iloc[0]

    interacciones_por_producto = (
        df.groupby("producto")["interacciones"]
        .sum()
        .reset_index()
    )

    grafico_productos = px.bar(
        interacciones_por_producto,
        x="producto",
        y="interacciones",
        title="Interacciones por producto"
    )

    grafico_tipos = px.pie(
        df,
        names="tipo_contenido",
        values="interacciones",
        title="Impacto por tipo de contenido"
    )

    return {
        "total_publicaciones": total_publicaciones,
        "alcance_total": alcance_total,
        "engagement_promedio": engagement_promedio,
        "mejor_publicacion": mejor_publicacion,
        "grafico_productos_html": pio.to_html(grafico_productos, full_html=False),
        "grafico_tipos_html": pio.to_html(grafico_tipos, full_html=False),
        "top_publicaciones": df.sort_values(
            by="engagement",
            ascending=False
        ).head(5).to_dict(orient="records")
    }