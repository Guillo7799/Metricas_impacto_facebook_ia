from pathlib import Path
import pandas as pd


def cargar_dataset():
    ruta = Path(__file__).resolve().parents[2] / "data" / "dataset_Facebook.csv"

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    df = pd.read_csv(
        ruta,
        sep=";",
        encoding="latin-1"
    )

    return df


def limpiar_dataset(df):

    print("\nIniciando limpieza de datos...")

    registros_originales = len(df)

    df = df.dropna()

    registros_finales = len(df)

    print(f"Registros originales : {registros_originales}")
    print(f"Registros eliminados : {registros_originales - registros_finales}")
    print(f"Registros finales    : {registros_finales}")

    return df


def ejecutar_preparacion():

    df = cargar_dataset()
    df = limpiar_dataset(df)

    print("\n" + "=" * 60)
    print("DIMENSIONES")
    print("=" * 60)
    print(df.shape)

    print("\nCOLUMNAS")
    print("=" * 60)
    print(df.columns.tolist())

    print("\nTIPOS")
    print("=" * 60)
    print(df.dtypes)

    print("\nVALORES NULOS")
    print("=" * 60)
    print(df.isnull().sum())

    print("\nESTADÍSTICAS")
    print("=" * 60)
    print(df.describe())

    print("\nTIPOS DE PUBLICACIÓN")
    print("=" * 60)
    print(df["Type"].value_counts())

    print("\nPUBLICACIONES PAGADAS")
    print("=" * 60)
    print(df["Paid"].value_counts())

    print("\nPRIMERAS FILAS")
    print("=" * 60)
    print(df.head())

    return df


if __name__ == "__main__":
    try:
        ejecutar_preparacion()
    except Exception as e:
        print("\nERROR DETECTADO:")
        print(type(e).__name__)
        print(e)