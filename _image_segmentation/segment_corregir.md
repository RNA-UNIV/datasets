# 🌆 Dataset de Segmentación de Imágenes: Clasificación de Tipos de Superficie
## 1. 📖 Descripción General

El Image Segmentation Dataset es un conjunto de datos fundamental en el ámbito del procesamiento de imágenes y el aprendizaje automático. Este dataset fue creado para la clasificación de tipos de superficie basándose en características extraídas de regiones de 3x3 píxeles pertenecientes a 7 imágenes distintas.

La versión utilizada en este análisis proviene del repositorio de Machine Learning de la Universidad de California, Irvine (UCI), una fuente de referencia en ciencia de datos. Este conjunto de datos ha sido ampliamente utilizado como benchmark para algoritmos de clasificación en visión por computadora y procesamiento de imágenes.

Lo que lo hace especialmente valioso es su estructura bien definida y su perfecta condición: todas las regiones fueron caracterizadas meticulosamente a partir de imágenes reales, lo que lo convierte en un estándar confiable para probar la capacidad de los modelos para distinguir entre diferentes tipos de superficie basándose en atributos visuales y texturales.

Este dataset representa un caso de estudio excelente para comprender cómo las características de bajo nivel de imágenes pueden definir la pertenencia a una categoría visual, y sirve como base para el desarrollo de sistemas de segmentación automatizada en visión por computadora.
## 2. 📊 Atributos y Significados

Todas las características se midieron a partir de regiones de 3x3 píxeles extraídas de imágenes. Todas las variables son numéricas continuas, excepto la clase objetivo.
### 2.1 🔑 Variable Objetivo

Clase: Tipo de superficie a la que pertenece la región de 3x3 píxeles.

    brickface: Superficie de ladrillo

    sky: Cielo

    foliage: Follaje

    cement: Cemento

    window: Ventana

    path: Camino

    grass: Pasto

### 2.2 🎨 Atributos de Imagen (19 características)

Atributos de Posición y Forma:

    region-centroid-col: La columna del pixel central de la región.

    region-centroid-row: La fila del pixel central de la región.

    region-pixel-count: El número de pixeles de la región (siempre = 9).

Atributos de Textura y Contorno:

    short-line-density-5: Resultado de algoritmo de extracción de líneas (bajo contraste).

    short-line-density-2: Resultado de algoritmo de extracción de líneas (alto contraste).

    vedge-mean: Medida del contraste para eje vertical (valor promedio).

    vegde-sd: Desviación estándar del contraste vertical.

    hedge-mean: Medida del contraste para eje horizontal (valor promedio).

    hedge-sd: Desviación estándar del contraste horizontal.

Atributos de Color e Intensidad:

    intensity-mean: Promedio de intensidad (R + G + B)/3.

    rawred-mean: Promedio de los valores del canal Rojo.

    rawblue-mean: Promedio de los valores del canal Azul.

    rawgreen-mean: Promedio de los valores del canal Verde.

Atributos de Balance de Color:

    exred-mean: Medida de exceso de color rojo: (2R - (G + B)).

    exblue-mean: Medida de exceso de color azul: (2B - (G + R)).

    exgreen-mean: Medida de exceso de color verde: (2G - (R + B)).

Atributos de Espacio de Color HSV:

    value-mean: Transformación no lineal 3D de RGB (componente Value).

    saturation-mean: Componente de saturación en espacio HSV.

    hue-mean: Componente de tono (hue) en espacio HSV.

## 3. 🏢 Origen y Procedencia
### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository

El dataset fue obtenido del repositorio oficial de la Universidad de California, Irvine, una de las fuentes más respetadas en ciencia de datos y aprendizaje automático.

URL Oficial:
👉 https://archive.ics.uci.edu/ml/datasets/Image+Segmentation

Nombres de archivos:

    segment_train o segmentación.train - datos de entrenamiento

    segmentación.tst o segmentación.test - datos de prueba

### 3.2 🏛�?Características del Dataset

Este dataset fue diseñado específicamente para investigación en segmentación de imágenes:

- 210 instancias de entrenamiento (30 por cada una de las 7 clases)
- 2100 instancias de prueba (300 por clase)
- 19 atributos numéricos por instancia
- 7 clases balanceadas perfectamente

## 4. 🔁 Estructura del Dataset

El dataset está dividido en dos partes claramente separadas:
### 4.1 📁 Conjunto de Entrenamiento

- Archivo: Segment_Train.csv o segmentation.data
- Instancias: 210
- Distribución: 30 muestras por cada una de las 7 clases
- Propósito: Entrenamiento de modelos

### 4.2 📁 Conjunto de Prueba

- Archivo: segment_test.csv o segmentation.test
- Instancias: 2100
- Distribución: 300 muestras por cada una de las 7 clases
- Propósito: Validación y testing de modelos

## 5. 🎯 Valor Analítico

Este dataset ofrece un entorno analítico clásico y robusto, ideal para:

- **Clasificación multiclase** (7 tipos de superficie).
- **Procesamiento de imágenes y visión por computadora**.
- **Selección de características en dominios visuales**.
- **Modelos de clasificación con SVM, Redes Neuronales, K-NN, etc**.
- **Reducción de dimensionalidad** (19 características correlacionadas).
- **Estudios de transfer learning entre dominios visuales**.

Su estructura bien definida y la diversidad de características lo convierten en un recurso excelente para la enseñanza de conceptos fundamentales de visión por computadora y aprendizaje automático.
## 6. 📝 Consideraciones Técnicas

Aunque el dataset es técnicamente sólido, es importante considerar:

- Las variables tienen diferentes escalas y rangos.
- Algunas características están correlacionadas (ej: componentes RGB).
- El espacio de características es de dimensionalidad media (19 atributos).
- Perfecto para demostrar técnicas de normalización y estandarización.
- Las clases están perfectamente balanceadas en ambos conjuntos

## 7. 🔗 Acceso y Uso

El dataset está disponible bajo licencia abierta para investigación y enseñanza. Se recomienda citar adecuadamente el repositorio UCI.
### 7.1 📥 Cómo cargarlo en Python:

Acceso directo desde UCI:
```python
import pandas as pd
from sklearn.datasets import fetch_ucirepo

# Cargar dataset desde UCI
image_segmentation = fetch_ucirepo(id=50)  # ID para Image Segmentation

# Datos como dataframes de pandas
X_train = image_segmentation.data.features
y_train = image_segmentation.data.targets

# Metadatos
print(image_segmentation.metadata)
print(image_segmentation.variables)
```

Acceso desde archivos locales:

```python
import pandas as pd

# Cargar conjuntos de entrenamiento y prueba
train_df = pd.read_csv('segment_train.csv')
test_df = pd.read_csv('segment_test.csv')

# Información del dataset
print("Entrenamiento - Dimensiones:", train_df.shape)
print("Prueba - Dimensiones:", test_df.shape)
print("\nColumnas:", train_df.columns.tolist())
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

# URLs hypothetical - ajustar según repositorio real
train_url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/image_segment/segment_train.csv"
test_url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/image_segment/segment_test.csv"

train_df = pd.read_csv(train_url)
test_df = pd.read_csv(test_url)

print("Dataset cargado exitosamente")
print("Entrenamiento:", train_df.shape)
print("Prueba:", test_df.shape)
```

🔖 Cita Recomendada:
Dua, D. and Graff, C. (2019). UCI Machine Learning Repository 
[http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, 
School of Information and Computer Science.

Image Segmentation Data Set. Donor: Vision Group, University of Massachusetts.


Datos de la evoluci��n

Recibe entradas (desde el mundo exterior) y produce salidas (al mundo exterior)

