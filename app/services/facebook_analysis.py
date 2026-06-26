import pandas as pd
import plotly.express as px
import plotly.io as pio


def cargar_datos():
    df = pd.read_csv("data/dataset_Facebook.csv", sep=";")

    df["interacciones"] = (
        df["reacciones"] +
        df["comentarios"] +
        df["compartidos"] +
        df["clics"]
    )

    df["engagement"] = (df["interacciones"] / df["alcance"]) * 100

    df["nivel_impacto"] = pd.cut(
        df["engagement"],
        bins=[0, 20, 28, 100],
        labels=["Bajo", "Medio", "Alto"]
    )

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

    grafico_productos = px.bar(
        df.groupby("producto")["interacciones"].sum().reset_index(),
        x="producto",
        y="interacciones",
        title="Interacciones por producto"
    )

    grafico_impacto = px.pie(
        df,
        names="nivel_impacto",
        title="Distribución de publicaciones por nivel de impacto"
    )

    top_publicaciones = df.sort_values(
        by="engagement",
        ascending=False
    ).head(5)

    recomendacion = generar_recomendacion(df)

    return {
        "total_publicaciones": total_publicaciones,
        "alcance_total": alcance_total,
        "engagement_promedio": engagement_promedio,
        "mejor_publicacion": mejor_publicacion,
        "grafico_productos_html": pio.to_html(grafico_productos, full_html=False),
        "grafico_impacto_html": pio.to_html(grafico_impacto, full_html=False),
        "top_publicaciones": top_publicaciones.to_dict(orient="records"),
        "recomendacion": recomendacion
    }


def generar_recomendacion(df):
    mejor_tipo = (
        df.groupby("tipo_contenido")["engagement"]
        .mean()
        .sort_values(ascending=False)
        .index[0]
    )

    mejor_producto = (
        df.groupby("producto")["engagement"]
        .mean()
        .sort_values(ascending=False)
        .index[0]
    )

    return (
        f"El tipo de contenido con mejor rendimiento es '{mejor_tipo}'. "
        f"El producto con mayor impacto promedio es '{mejor_producto}'. "
        "Se recomienda priorizar este tipo de publicación en futuras campañas."
    )