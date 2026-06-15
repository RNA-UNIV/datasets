# 🍷 Dataset Wine: Clasificación de Cultivares de Vino por Análisis Químico

## 1. 📖 Descripción General

El **Wine Dataset** es uno de los conjuntos de datos más reconocidos en el ámbito del aprendizaje automático y el análisis quimiométrico. Fue donado al repositorio UCI por **Stefan Aeberhard** y **M. Forina** a partir de análisis químicos realizados sobre vinos producidos en la región del **Piamonte, Italia**. Se ha convertido en un benchmark de referencia para problemas de clasificación multiclase con atributos de alta relevancia discriminativa.

La versión estándar proviene del **repositorio de Machine Learning de la Universidad de California, Irvine (UCI)**, siendo ampliamente utilizado para evaluar algoritmos de clasificación, técnicas de reducción de dimensionalidad y métodos de análisis exploratorio.

El dataset contiene resultados de análisis químicos de vinos derivados de tres cultivares distintos del mismo viñedo:

- **Cultivar 1**
- **Cultivar 2**
- **Cultivar 3**

Lo que hace a este dataset tan valioso es la **riqueza química de sus atributos**: con 13 variables derivadas de análisis de laboratorio y 3 clases bien diferenciadas, es ideal para explorar la separabilidad lineal, la importancia de características y técnicas de visualización multivariada como PCA y LDA.

## 2. 📊 Atributos y Significados

### 2.1 🔑 Variable Objetivo

**Class (Cultivar)**: Clasificación del vino según su cultivar de origen.
- `1` — Cultivar 1
- `2` — Cultivar 2
- `3` — Cultivar 3

### 2.2 📏 Atributos de Medición (análisis químicos de laboratorio)

**Alcohol**: Porcentaje de alcohol en el vino.  
*Valor numérico continuo.*

**Malic Acid (Ácido málico)**: Concentración de ácido málico.  
*Valor numérico continuo, expresado en g/L.*

**Ash (Cenizas)**: Contenido de cenizas del vino.  
*Valor numérico continuo.*

**Alcalinity of Ash (Alcalinidad de las cenizas)**: Alcalinidad de las cenizas.  
*Valor numérico continuo.*

**Magnesium (Magnesio)**: Contenido de magnesio.  
*Valor numérico continuo, expresado en mg/L.*

**Total Phenols (Fenoles totales)**: Concentración total de compuestos fenólicos.  
*Valor numérico continuo.*

**Flavanoids (Flavonoides)**: Concentración de flavonoides, subgrupo de los fenoles.  
*Valor numérico continuo.*

**Nonflavanoid Phenols (Fenoles no flavonoides)**: Concentración de fenoles que no son flavonoides.  
*Valor numérico continuo.*

**Proanthocyanins (Proantocianinas)**: Concentración de proantocianinas.  
*Valor numérico continuo.*

**Color Intensity (Intensidad de color)**: Intensidad del color del vino.  
*Valor numérico continuo.*

**Hue (Matiz)**: Matiz o tonalidad del color del vino.  
*Valor numérico continuo.*

**OD280/OD315 of Diluted Wines**: Relación de absorbancia a 280 nm y 315 nm en vinos diluidos, indicador de contenido proteico.  
*Valor numérico continuo.*

**Proline (Prolina)**: Concentración del aminoácido prolina.  
*Valor numérico continuo, expresado en mg/L.*

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository

El dataset fue obtenido del repositorio oficial de la Universidad de California, Irvine, donde ha sido mantenido como recurso educativo y de benchmarking desde su donación original.

> **URL Oficial**: 👉 `https://archive.ics.uci.edu/dataset/109/wine`
>
> **Nombre del dataset**: `wine`  
> **ID UCI**: `109`

### 3.2 📜 Contexto Histórico

Los datos provienen de análisis químicos realizados en el **Instituto de Investigación Agrícola de San Michele all'Adige** (Trento, Italia). Las muestras corresponden a vinos elaborados a partir de tres variedades de uva cultivadas en la misma región del Piamonte, analizadas mediante técnicas estándar de química analítica. El dataset fue contribuido al repositorio UCI como parte del trabajo de Aeberhard et al. sobre clasificación quimiométrica.

## 4. 🔁 Proceso de Curaduría

El dataset ha sido meticulosamente curado y verificado:

- 178 instancias totales (59 cultivar 1, 71 cultivar 2, 48 cultivar 3)
- Sin valores faltantes
- 13 atributos numéricos continuos de naturaleza química
- Clases moderadamente desbalanceadas
- Todos los atributos en unidades físicas reales (sin normalización previa)
- Documentación clara y estandarizada

## 5. 🎯 Valor Analítico

Este dataset ofrece un entorno analítico muy completo para:

- **Clasificación multiclase** (3 cultivares de vino)
- **Reducción de dimensionalidad** con PCA y LDA (excelente separabilidad en 2D)
- **Análisis de importancia de características** y correlación química
- **Pruebas de algoritmos** de machine learning (SVM, KNN, Random Forest, redes neuronales)
- **Enseñanza de conceptos** de normalización, escalado y preprocesamiento
- **Visualización** con pairplots, biplots PCA y análisis discriminante

Su alta separabilidad entre clases lo convierte en un dataset ideal para demostrar el impacto del escalado de atributos (muchos algoritmos de distancia son sensibles a las diferencias de escala entre variables químicas).

## 6. 📝 Consideraciones Éticas

Si bien el dataset no presenta problemas éticos significativos al tratarse de análisis químicos de productos alimentarios, es importante:

- Reconocer el trabajo original de Aeberhard y Forina
- Utilizar el dataset con fines educativos y de investigación
- Citar apropiadamente las fuentes originales
- Tener en cuenta que los cultivares no están identificados por nombre varietal público, por lo que las clases (1, 2, 3) son etiquetas relativas al estudio original

## 7. 🔗 Acceso y Uso

El dataset está disponible bajo **dominio público** y es accesible a través de múltiples librerías de Python.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con Scikit-Learn:
```python
from sklearn.datasets import load_wine
import pandas as pd

# Cargar dataset
wine = load_wine()

# Convertir a DataFrame
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target, name='cultivar')
y = y.map({0: 'cultivar_1', 1: 'cultivar_2', 2: 'cultivar_3'})

# Información del dataset
print("Características:", wine.feature_names)
print("Cultivares:", wine.target_names)
print("Forma de los datos:", wine.data.shape)
```

Acceso con UCI:
```python
from ucimlrepo import fetch_ucirepo

# Cargar dataset
wine = fetch_ucirepo(id=109)

# data (como dataframes pandas)
X = wine.data.features
y = wine.data.targets

# metadata
print(wine.metadata)

# información del dataset
print(wine.variables)
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

# url del repositorio github para descargar
url = "https://raw.githubusercontent.com/rna-univ/datasets/main/wine/wine.csv"
wine = pd.read_csv(url)

# Separar características y etiquetas
X = wine.drop(columns=['class'])
y = wine['class']

# Información del dataset
print("Columnas:", wine.columns.tolist())
print("Primeras filas:\n", wine.head())
```

## 8. 🔖 Citas Recomendadas:

> Aeberhard, S., Coomans, D., & de Vel, O. (1992). *Comparison of classifiers in high dimensional settings*. Tech. Rep. no. 92-02, Dept. of Computer Science and Dept. of Mathematics and Statistics, James Cook University of North Queensland.

> Forina, M., et al. (1988). *PARVUS: An Extendable Package for Data Exploration, Classification and Correlation*. Institute of Pharmaceutical and Food Analysis and Technologies, Genoa, Italy.
