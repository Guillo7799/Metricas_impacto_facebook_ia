from pathlib import Path
import pandas as pd


def cargar_dataset():
    ruta = Path(__file__).resolve().parents[2] / "data" / "dataset_Facebook.csv"

    print("Ruta buscada:")
    print(ruta)

    print("\n¿Existe el archivo?")
    print(ruta.exists())

    print("\nTamaño del archivo:")
    print(ruta.stat().st_size if ruta.exists() else "No existe")

    df = pd.read_csv(
        ruta,
        sep=";",
        encoding="latin-1"
    )

    return df

def limpiar_dataset(df):

    print("\nIniciando limpieza de datos...")

    # Eliminar registros con valores nulos
    df = df.dropna()

    print(f"Registros después de limpieza: {len(df)}")

    return df


if __name__ == "__main__":
    try:
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

        print("\nPRIMERAS FILAS")
        print("=" * 60)
        print(df.head())
        print("\nESTADÍSTICAS")
        print("=" * 60)
        print(df.describe())

        print("\nTIPOS DE PUBLICACIÓN")
        print("=" * 60)
        print(df["Type"].value_counts())

        print("\nPUBLICACIONES PAGADAS")
        print("=" * 60)
        print(df["Paid"].value_counts())

    except Exception as e:
        print("\nERROR DETECTADO:")
        print(type(e).__name__)
        print(e)