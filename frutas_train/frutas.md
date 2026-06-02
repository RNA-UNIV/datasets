# 🍎 Dataset Clasificación de Frutas: Predicción de Tipos de Frutas
## 1. 📖 Descripción General
El conjunto de datos de Clasificación de Frutas es una herramienta educativa diseñada para principiantes en aprendizaje automático que desean explorar modelos de clasificación basados en características físicas de frutas. Este dataset contiene información sobre variables visuales que influyen en la identificación de diferentes tipos de frutas, permitiendo desarrollar modelos predictivos para determinar qué tipo de fruta corresponde según sus atributos físicos.

Los datos reflejan relaciones entre factores como el diámetro y el color, lo que lo convierte en un recurso ideal para ejercicios de clasificación binaria en contextos educativos y de introducción a la ciencia de datos.

## 2. 📊 Atributos y Significados

### 2.1 🍊 Variable Objetivo
**Clase**: Tipo de fruta según sus características físicas.
 - `Naranja`: Fruta cítrica de color naranja
 - `Melon`: Fruta grande y redonda de color verde/amarillo

### 2.2 📏 Atributos Físicos
**Diametro**: Diámetro de la fruta en centímetros (variable continua).
**Color**: Valor numérico que representa el tono de color de la fruta en escala de 0-255 (variable continua).

### 2.3 🏷️ Notas sobre los Atributos
- Todas las mediciones son numéricas, con valores bien definidos.
- El atributo Clase es categórico y sirve como variable objetivo en tareas de clasificación supervisada.
- El diámetro y el color muestran patrones diferenciados entre los tipos de frutas.
- No se reportan valores nulos en los archivos, lo que los hace ideales para análisis iniciales.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: GitHub
El dataset propio, fue creado específicamente para fines educativos y está alojado en GitHub.

> **URL Oficial**:
👉 https://github.com/aap-unlp/datasets/tree/main/frutas
>
> **Nombres de los archivos**:
> - frutas_train.csv (conjunto de entrenamiento)
> - frutas_test.csv (conjunto de prueba)

### 3.2 🏛️ Contexto Educativo
Este conjunto de datos fue diseñado para simular un escenario simple de clasificación binaria, ideal para enseñar conceptos fundamentales de machine learning como preprocesamiento de datos, entrenamiento de modelos y evaluación de resultados.

## 4. 🔄 Proceso de Creación
La versión documentada ha sido adaptada mediante:
- Organización del contenido siguiendo el formato del dataset de fármacos
- Documentación clara de unidades y significado de las variables
- Creación de conjuntos separados para entrenamiento y prueba

## 5. 🎯 Valor Analítico
Este dataset ofrece múltiples oportunidades para el aprendizaje y análisis:
- Clasificación binaria de tipos de frutas
- Análisis de decisiones basadas en reglas (ej. árboles de decisión)
- Visualización de relaciones entre variables (e.g., Diámetro vs. Color)
- Preprocesamiento de variables numéricas (escalado, normalización)
- Evaluación de modelos de clasificación (regresión logística, KNN, SVM)
- Introducción a la separación train/test y validación cruzada

## 6. 📝 Consideraciones
Los datos son sintéticos y creados específicamente para fines educativos. Su uso está orientado exclusivamente a la educación y la práctica de ciencia de datos.

## 7. 🔗 Acceso y Uso
El dataset está disponible para uso educativo sin restricciones.

### 7.1 📥 Cómo cargarlo en Python:

Acceso vía GitHub:
```python
import pandas as pd

# URLs de los archivos
train_url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/frutas/frutas_train.csv"
test_url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/frutas/frutas_test.csv"

# Cargar datasets
train_df = pd.read_csv(train_url)
test_df = pd.read_csv(test_url)

# Separar características y etiquetas
X_train = train_df.drop(columns=['Clase'])
y_train = train_df['Clase']
X_test = test_df.drop(columns=['Clase'])
y_test = test_df['Clase']

# Información de los datasets
print("Conjunto de entrenamiento:")
print("Columnas:", train_df.columns.tolist())
print("Primeras filas:\n", train_df.head())
print("\nConjunto de prueba:")
print("Primeras filas:\n", test_df.head())
```

## 8. 🔖 Cita Recomendada:

> Dataset de Clasificación de Frutas. (2024). Universidad Nacional de La Plata. \
https://github.com/aap-unlp/datasets/tree/main/frutas

