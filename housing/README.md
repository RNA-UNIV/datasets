<p align="center">
<img src="banner.png" width="1000">
</p>

# 🏠 Dataset California Housing: Predicción del Valor Mediano de Viviendas

## 1. 📖 Descripción General

El **California Housing Dataset** es un conjunto de datos ampliamente utilizado en el ámbito del aprendizaje automático para problemas de regresión. Fue compilado por **R. Kelley Pace** y **Ronald Barry** a partir del **Censo de California de 1990**, y publicado en su artículo *"Sparse Spatial Autoregressions"* (1997). Se ha convertido en un benchmark de referencia para predicción de valores inmobiliarios y para el estudio de datos con componente geoespacial explícita.

La versión estándar proviene del **repositorio de Machine Learning de la Universidad de California, Irvine (UCI)** y también está disponible directamente en Scikit-Learn. Cada instancia representa un **bloque censal** de California, la unidad geográfica mínima utilizada por el censo estadounidense.

El objetivo del dataset es predecir el **valor mediano de las viviendas** de cada bloque censal a partir de características demográficas, habitacionales y geográficas:

- Información de ubicación geográfica (latitud y longitud)
- Características del parque habitacional del bloque
- Datos demográficos de los residentes

Lo que hace a este dataset tan valioso es su **componente geoespacial**: la latitud y longitud permiten visualizar los datos sobre el mapa de California, revelando patrones claros de valorización vinculados a la proximidad al océano, grandes ciudades y características regionales.

## 2. 📊 Atributos y Significados

### 2.1 🎯 Variable Objetivo

**MedHouseVal (Median House Value / Valor Mediano de Vivienda)**: Valor mediano de las viviendas del bloque censal.
- Rango observado: 14,999 – 500,001 USD
- *Valor numérico continuo. Los valores están truncados en 500,001 USD (techo censal).*

### 2.2 📏 Atributos de Entrada

**MedInc (Median Income / Ingreso Mediano)**: Ingreso mediano de los hogares del bloque censal.
- *Valor numérico continuo, expresado en decenas de miles de dólares (escala ~0.5 – 15).*

**HouseAge (Housing Median Age / Antigüedad Mediana)**: Antigüedad mediana de las viviendas del bloque.
- *Valor numérico continuo, expresado en años.*

**AveRooms (Average Rooms / Habitaciones Promedio)**: Número promedio de habitaciones por vivienda en el bloque.
- *Valor numérico continuo. Puede contener outliers por bloques con pocas viviendas.*

**AveBedrms (Average Bedrooms / Dormitorios Promedio)**: Número promedio de dormitorios por vivienda en el bloque.
- *Valor numérico continuo.*

**Population (Población)**: Población total del bloque censal.
- *Valor numérico continuo, expresado en número de personas.*

**AveOccup (Average Occupancy / Ocupación Promedio)**: Número promedio de miembros del hogar por vivienda.
- *Valor numérico continuo.*

**Latitude (Latitud)**: Latitud geográfica del centroide del bloque censal.
- Rango observado: 32.54° – 41.95° N
- *Valor numérico continuo. Correlaciona con patrones de precio norte-sur.*

**Longitude (Longitud)**: Longitud geográfica del centroide del bloque censal.
- Rango observado: -124.35° – -114.31° W
- *Valor numérico continuo. Junto con Latitude permite geolocalizar cada bloque sobre el mapa de California.*

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository

El dataset fue obtenido del repositorio oficial de la Universidad de California, Irvine, y posteriormente integrado en Scikit-Learn como dataset de ejemplo estándar.

> **URL Oficial**: 👉 `https://archive.ics.uci.edu/dataset/563/california+housing`
>
> **Nombre del dataset**: `california+housing`
> **ID UCI**: `563`

### 3.2 📜 Contexto Histórico

Los datos provienen del **censo decenal de los Estados Unidos de 1990**, específicamente de las respuestas del estado de California. Pace y Barry los utilizaron originalmente para estudiar modelos de regresión espacial con matrices de vecindad dispersas (*sparse spatial autoregressions*). Cada registro corresponde a un bloque censal, que en California agrupa típicamente entre 600 y 3000 personas. La inclusión explícita de coordenadas geográficas lo distingue de la mayoría de los datasets de vivienda y habilita análisis espaciales directos.

## 4. 🔁 Proceso de Curaduría

El dataset ha sido meticulosamente curado y verificado:

- 20,640 instancias totales (bloques censales de California)
- Sin valores faltantes en la versión estándar de Scikit-Learn
- Variables en unidades reales (sin normalización previa)
- Variable objetivo truncada en 500,001 USD (techo del censo original)
- Coordenadas geográficas reales, compatibles con herramientas de visualización cartográfica
- Ampliamente documentado y validado por la comunidad

## 5. 🎯 Valor Analítico

Este dataset ofrece un entorno analítico muy rico para:

- **Regresión supervisada** (predicción de valor de vivienda continuo)
- **Análisis geoespacial** y visualización sobre mapas de California
- **Detección y tratamiento de outliers** (AveRooms y AveOccup pueden tener valores extremos)
- **Pruebas de algoritmos** de machine learning (regresión lineal, SVR, Gradient Boosting, redes neuronales)
- **Enseñanza de conceptos** de normalización, ingeniería de features y análisis de residuos
- **Visualización** con mapas de calor geoespaciales, scatter plots lat/lon coloreados por precio, y análisis de correlación

La combinación de atributos geográficos, demográficos y habitacionales lo convierte en un recurso ideal para introducir la noción de **autocorrelación espacial** y el efecto de la ubicación en los modelos predictivos.

## 6. 📝 Consideraciones Éticas

Al tratarse de datos censales agregados por bloque, este dataset presenta algunas consideraciones importantes:

- Los datos son agregados (no individuales), lo que reduce riesgos de privacidad
- Reconocer el trabajo original de Pace y Barry
- El truncamiento en 500,001 USD puede introducir sesgo en modelos entrenados sobre zonas de alto valor
- Los patrones geoespaciales pueden reflejar dinámicas históricas de segregación residencial; su interpretación debe hacerse con contexto socioeconómico adecuado
- Utilizar el dataset con fines educativos y de investigación, citando apropiadamente las fuentes originales

## 7. 🔗 Acceso y Uso

El dataset está disponible bajo **dominio público** y es accesible a través de múltiples librerías de Python.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con el DataLoader de la biblioteca `rna` (Recomendado):
```python
# Instalar la biblioteca si no está disponible:
# !pip install https://github.com/RNA-UNIV/rna/archive/refs/heads/main.zip

from rna.data.ClassDataLoader import DataLoader

# Cargar el dataset como DataFrame de Pandas
df = DataLoader.load_dataframe('housing')
```

Acceso con Scikit-Learn:
```python
from sklearn.datasets import fetch_california_housing
import pandas as pd

# Cargar dataset
housing = fetch_california_housing()

# Convertir a DataFrame
X = pd.DataFrame(housing.data, columns=housing.feature_names)
y = pd.Series(housing.target, name='MedHouseVal')

# Información del dataset
print("Características:", housing.feature_names)
print("Forma de los datos:", housing.data.shape)
print("Primeras filas:\n", X.head())
```

Acceso con UCI:
```python
from ucimlrepo import fetch_ucirepo

# Cargar dataset
housing = fetch_ucirepo(id=563)

# data (como dataframes pandas)
X = housing.data.features
y = housing.data.targets

# metadata
print(housing.metadata)

# información del dataset
print(housing.variables)
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

# url del repositorio github para descargar
url = "https://raw.githubusercontent.com/rna-univ/datasets/main/housing/housing.csv"
housing = pd.read_csv(url)

# Separar características y etiqueta
X = housing.drop(columns=['MedHouseVal'])
y = housing['MedHouseVal']

# Información del dataset
print("Columnas:", housing.columns.tolist())
print("Primeras filas:\n", housing.head())
```

Visualización geoespacial básica:
```python
import matplotlib.pyplot as plt

# Scatter plot geográfico coloreado por valor de vivienda
plt.figure(figsize=(10, 7))
sc = plt.scatter(X['Longitude'], X['Latitude'],
                 c=y, cmap='viridis', alpha=0.4, s=5)
plt.colorbar(sc, label='Valor Mediano (x$100,000)')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('California Housing: distribución geoespacial de precios')
plt.tight_layout()
plt.show()
```

## 8. 🔖 Cita Recomendada:

> Pace, R. K., & Barry, R. (1997). *Sparse spatial autoregressions*. Statistics & Probability Letters, 33(3), 291–297. https://doi.org/10.1016/S0167-7152(96)00140-X
