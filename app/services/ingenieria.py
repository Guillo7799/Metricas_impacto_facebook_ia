from sklearn.model_selection import train_test_split
from app.services.preparacion import cargar_dataset, limpiar_dataset

def preparar_datos_modelo():
    df = cargar_dataset()
    df = limpiar_dataset(df)

    variable_objetivo = "Total Interactions"

    columnas_excluir = [
        "Total Interactions",
        "like",
        "comment",
        "share"
    ]

    X = df.drop(columns=columnas_excluir)
    y = df[variable_objetivo]

    X = X.copy()
    X = X.drop(columns=[], errors="ignore")

    X = X.astype({
        "Category": "int64",
        "Post Month": "int64",
        "Post Weekday": "int64",
        "Post Hour": "int64",
        "Paid": "int64"
    })

    X = X.fillna(0)

    X = X.join(
        X["Type"]
        .str.get_dummies()
        .add_prefix("Type_")
    )

    X = X.drop(columns=["Type"])

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.30,
        random_state=42
    )

    return X_train, X_test, y_train, y_test, X.columns.tolist()


if __name__ == "__main__":
    X_train, X_test, y_train, y_test, columnas = preparar_datos_modelo()

    print("\nFASE 3 - FEATURE ENGINEERING")
    print("=" * 60)

    print("X_train:", X_train.shape)
    print("X_test :", X_test.shape)
    print("y_train:", y_train.shape)
    print("y_test :", y_test.shape)

    print("\nColumnas finales del modelo:")
    for columna in columnas:
        print("-", columna)