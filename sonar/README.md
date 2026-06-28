<p align="center">
<img src="banner.png" width="1000">
</p>

# 🔊 Dataset Sonar: Clasificación de Minas Submarinas vs. Rocas

## 1. 📖 Descripción General

El **Sonar Dataset** es un conjunto de datos clásico y ampliamente utilizado en el ámbito del aprendizaje automático, especialmente en problemas de clasificación binaria. Fue introducido por **R. Paul Gorman** y **Terrence J. Sejnowski** en 1988 en su artículo *"Analysis of Hidden Units in a Layered Network Trained to Classify Sonar Targets"*, publicado en Neural Networks. Su origen está ligado a la investigación en redes neuronales artificiales y reconocimiento de patrones acústicos.

La versión estándar proviene del **repositorio de Machine Learning de la Universidad de California, Irvine (UCI)**, siendo un benchmark de referencia para clasificación binaria con alta dimensionalidad relativa.

El dataset contiene señales de sonar rebotadas sobre dos tipos de objetos sumergidos en el fondo del océano:

- **Minas cilíndricas de metal (M)**
- **Rocas de forma cilíndrica (R)**

Lo que hace a este dataset tan valioso es la **dificultad intrínseca de la tarea**: las dos clases son físicamente similares en forma, por lo que la discriminación depende de patrones sutiles en el espectro de energía de la señal sonar. Con 60 atributos numéricos continuos y solo 208 instancias, es ideal para estudiar problemas de alta dimensión, sobreajuste y la capacidad de generalización de distintos clasificadores.

## 2. 📊 Atributos y Significados

### 2.1 🔑 Variable Objetivo

**Class (Tipo de objeto)**: Clasificación del objeto detectado por el sonar.
- `M` — Mine (mina cilíndrica de metal)
- `R` — Rock (roca de forma aproximadamente cilíndrica)

### 2.2 📏 Atributos de Medición

**Atributos 1 a 60 (Band_01 – Band_60)**: Energía de la señal sonar en 60 bandas de frecuencia diferentes, obtenidas mediante un barrido de frecuencias sobre el objeto.

- Cada atributo representa la **energía integrada** dentro de una banda de frecuencia particular, en el rango de frecuencias sonar relevantes para la detección submarina.
- *Valores numéricos continuos en el intervalo [0.0, 1.0].*
- Las bandas están ordenadas de menor a mayor frecuencia, capturando el **perfil espectral completo** del eco sonar recibido.

La combinación de estas 60 bandas constituye una **firma espectral** característica para cada tipo de objeto, que los clasificadores deben aprender a discriminar.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository

El dataset fue obtenido del repositorio oficial de la Universidad de California, Irvine, donde ha sido mantenido como recurso educativo y de benchmarking.

> **URL Oficial**: 👉 `https://archive.ics.uci.edu/dataset/151/connectionist+bench+sonar+mines+vs+rocks`
>
> **Nombre del dataset**: `connectionist+bench+sonar+mines+vs+rocks`  
> **ID UCI**: `151`

### 3.2 📜 Contexto Histórico

Los datos fueron recolectados experimentalmente por Gorman y Sejnowski en el contexto de investigación en **sonar de baja frecuencia** para detección submarina. Las señales fueron obtenidas haciendo rebotar pulsos de frecuencia modulada sobre un **cilindro metálico** (simulando una mina) y sobre **rocas de forma aproximadamente cilíndrica**, a distintos ángulos de aspecto. Los experimentos se realizaron en condiciones controladas de laboratorio, utilizando distintos ángulos entre 0° y 90° respecto al eje del objeto.

## 4. 🔁 Proceso de Curaduría

El dataset ha sido meticulosamente curado y verificado:

- 208 instancias totales (111 minas, 97 rocas)
- Sin valores faltantes
- Atributos normalizados en el rango [0.0, 1.0]
- Clases ligeramente desbalanceadas (53.4% M / 46.6% R)
- Datos recolectados bajo múltiples ángulos de aspecto para mayor variabilidad
- Documentación clara y estandarizada

## 5. 🎯 Valor Analítico

Este dataset ofrece un entorno analítico exigente para:

- **Clasificación binaria** con alta dimensionalidad relativa (60 features, 208 instancias)
- **Análisis de sobreajuste** y técnicas de regularización
- **Selección y reducción de características** (PCA, análisis de importancia)
- **Pruebas de algoritmos** de machine learning (redes neuronales, SVM, KNN, Random Forest)
- **Enseñanza de conceptos** de generalización en escenarios con pocos datos
- **Visualización** de separabilidad con PCA, t-SNE y análisis de correlación espectral

La combinación de alta dimensión, pocas instancias y clases difícilmente separables lo convierte en un recurso ideal para explorar la frontera entre capacidad del modelo y generalización.

## 6. 📝 Consideraciones Éticas

Si bien el dataset no presenta problemas éticos significativos al tratarse de señales experimentales de sonar, es importante:

- Reconocer el trabajo original de Gorman y Sejnowski
- Utilizar el dataset con fines educativos y de investigación
- Citar apropiadamente las fuentes originales
- Tener en cuenta que los datos fueron recolectados en condiciones de laboratorio controladas, por lo que la generalización a entornos reales de sonar submarino requiere validación adicional

## 7. 🔗 Acceso y Uso

El dataset está disponible bajo **dominio público** y es accesible a través de múltiples fuentes en Python.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con UCI:
```python
from ucimlrepo import fetch_ucirepo

# Cargar dataset
sonar = fetch_ucirepo(id=151)

# data (como dataframes pandas)
X = sonar.data.features
y = sonar.data.targets

# metadata
print(sonar.metadata)

# información del dataset
print(sonar.variables)
```

Acceso con pandas (URL directa):
```python
import pandas as pd

# Cargar dataset desde UCI
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data"
col_names = [f"Band_{i:02d}" for i in range(1, 61)] + ["class"]
sonar = pd.read_csv(url, header=None, names=col_names)

# Separar características y etiqueta
X = sonar.drop(columns=["class"])
y = sonar["class"]

# Información del dataset
print("Columnas:", sonar.columns.tolist())
print("Distribución de clases:\n", y.value_counts())
print("Primeras filas:\n", sonar.head())
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

# url del repositorio github para descargar
url = "https://raw.githubusercontent.com/rna-univ/datasets/main/sonar/sonar.csv"
sonar = pd.read_csv(url)

# Separar características y etiqueta
X = sonar.drop(columns=["class"])
y = sonar["class"]

# Información del dataset
print("Columnas:", sonar.columns.tolist())
print("Primeras filas:\n", sonar.head())
```

## 8. 🔖 Cita Recomendada:

> Gorman, R. P., & Sejnowski, T. J. (1988). *Analysis of hidden units in a layered network trained to classify sonar targets*. Neural Networks, 1(1), 75–89. https://doi.org/10.1016/0893-6080(88)90023-8
