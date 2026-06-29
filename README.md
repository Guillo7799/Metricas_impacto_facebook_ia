# Metricas_impacto_facebook_ia

## Proyecto Integrado de Ciencia de Datos e Inteligencia Artificial

### Docente: Ing. Diego Changoluisa

### Estudiantes: Guillermo Rivera | Sebastián Poveda | Armando Brito

Aplicación web desarrollada con Python, Flask y XGBoost para analizar el rendimiento de publicaciones en Facebook mediante técnicas de Ciencia de Datos e Inteligencia Artificial.

El sistema permite explorar un conjunto de datos real, entrenar un modelo predictivo y visualizar los resultados mediante un dashboard interactivo.

## Objetivo del proyecto

Desarrollar una aplicación web que permita identificar los factores que influyen en el impacto de las publicaciones en Facebook, utilizando técnicas de análisis exploratorio de datos y un modelo de aprendizaje automático basado en XGBoost.

El proyecto busca servir como herramienta de apoyo para la toma de decisiones en estrategias de marketing digital.

## Tecnologías utilizadas

Tecnología Descripción
Python 3.12 Lenguaje principal
Flask Framework web
Pandas Manipulación de datos
Plotly Visualización interactiva
Scikit-Learn Preprocesamiento y métricas
XGBoost Modelo de Inteligencia Artificial
Bootstrap 5 Diseño responsivo
Joblib Persistencia del modelo

## Estructura del proyecto

<img width="286" height="628" alt="image" src="https://github.com/user-attachments/assets/a696ad3b-f587-4461-bd12-44a4143955e0" />

## Dataset

El proyecto utiliza el conjunto de datos:

Facebook Metrics Dataset

Repositorio:

UCI Machine Learning Repository
Enlace: https://archive.ics.uci.edu/dataset/368/facebook+metrics

Características principales:

500 publicaciones
19 variables
Información relacionada con:
Alcance
Impresiones
Usuarios comprometidos
Likes
Shares
Comentarios

Variable objetivo:

Total Interactions

## Arquitectura del sistema

Dataset

↓

Preparación de datos

↓

Análisis Exploratorio (EDA)

↓

Ingeniería de características

↓

Modelo XGBoost

↓

Dashboard Web

Cada módulo cumple una responsabilidad específica, facilitando el mantenimiento y escalabilidad del proyecto.

## Instalación

1. Clonar el repositorio
   git clone https://github.com/Guillo7799/Metricas_impacto_facebook_ia.git

cd facebook-impact-ai 2. Crear entorno virtual

Windows

python -m venv .venv

Activar

.venv\Scripts\activate

Linux / Mac

python3 -m venv .venv

source .venv/bin/activate 3. Instalar dependencias
pip install -r requirements.txt 4. Ejecutar la aplicación
python run.py

Abrir el navegador en:

http://127.0.0.1:5000

## Flujo de procesamiento

1. Preparación de datos

Durante esta etapa se realiza:

Lectura del dataset
Validación del archivo
Limpieza de registros
Tratamiento de valores nulos
Estadísticas descriptivas

Archivo:

preparacion.py 2. Exploración de datos (EDA)

Se generan visualizaciones interactivas para analizar:

Impacto según tipo de publicación
Publicaciones pagadas vs. orgánicas
Mejor hora de publicación
Mejor día de publicación
Correlación entre variables

Archivo:

exploracion.py 3. Ingeniería de características

Se prepara el conjunto de datos para el modelo de IA.

Incluye:

One-Hot Encoding
Eliminación de Data Leakage
División Train/Test (70%-30%)

Archivo:

ingenieria.py 4. Modelo de Inteligencia Artificial

Se implementó un modelo de regresión utilizando:

XGBoost Regressor

Configuración:

n_estimators = 100

learning_rate = 0.1

max_depth = 4

random_state = 42

Archivo:

modelo_xgboost.py

## Métricas utilizadas

El modelo es evaluado mediante:

MAE

Error absoluto medio.

Representa el error promedio entre el valor real y el predicho.

RMSE

Raíz del error cuadrático medio.

Penaliza errores grandes.

R²

Coeficiente de determinación.

Representa el porcentaje de variabilidad explicado por el modelo.

En este proyecto el modelo obtuvo aproximadamente:

R² ≈ 0.70

## Dashboard

La aplicación web presenta:

Resumen del conjunto de datos.
Métricas del modelo.
Gráficos interactivos.
Variables más importantes.
Conclusiones automáticas.

El objetivo es facilitar la interpretación del comportamiento de las publicaciones en Facebook.
