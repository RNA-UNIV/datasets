<p align="center">
<img src="banner.png" width="1000">
</p>

# ⚖️ Dataset de Balance: Clasificación de Equilibrio en Balanzas

## 1. 📖 Descripción General

El Balance Scale Dataset es un conjunto de datos clásico y fundamental en el ámbito del aprendizaje automático, utilizado frecuentemente como punto de referencia (benchmark) para tareas de clasificación multiclase. Su simplicidad y lógica física clara lo convierten en una herramienta pedagógica.

El dataset modela el comportamiento de una balanza de palanca, donde el estado de equilibrio se determina aplicando el principio físico de los momentos: el producto del peso por la distancia en cada brazo. La versión utilizada proviene del repositorio de Machine Learning de la Universidad de California, Irvine (UCI), un estándar de facto en la comunidad de ciencia de datos.

Lo que distingue a este dataset es su naturaleza determinista y fácilmente interpretable. Cada instancia representa una configuración específica de pesos y distancias, y la clase resultante se deriva directamente de la ley de palancas. Esto permite validar las predicciones de cualquier modelo con una regla física simple, facilitando la comprensión de cómo los algoritmos aprenden y toman decisiones.

Este dataset es ideal para introducir conceptos fundamentales de clasificación, análisis de atributos numéricos y evaluación de modelos en problemas con fronteras de decisión bien definidas.

## 2. 📊 Atributos y Significados
Todas las características son variables numéricas discretas (enteros del 1 al 5). La clase objetivo es categórica.

### 2.1 🔑 Variable Objetivo
**ClassName**: Resultado del equilibrio de la balanza.
- `L`: La balanza se inclina hacia la izquierda (**L**eft).
- `D`: La balanza se inclina hacia la derecha (**R**ight).
- `B`: La balanza permanece equilibrada (**B**alanced).

### 2.2 🧰 Atributos Físicos (valores enteros de 1 a 5)
**LeftWeight**: Peso colocado en el lado izquierdo de la balanza.

**LeftDistance**: Distancia del peso izquierdo al centro de rotación.

**RightWeight**: Peso colocado en el lado derecho de la balanza.

**RightDistance**: Distancia del peso derecho al centro de rotación.

Importante: El estado de la balanza se define por la comparación de los momentos (Peso × Distancia):

- `LeftWeight × LeftDistance > RightWeight × RightDistance → L`
- `LeftWeight × LeftDistance = RightWeight × RightDistance → B`
- `LeftWeight × LeftDistance < RightWeight × RightDistance → R`

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository
El dataset fue obtenido del repositorio oficial de la Universidad de California, Irvine, una de las fuentes más respetadas en ciencia de datos y aprendizaje automático.

URL Oficial:
👉 [https://archive.ics.uci.edu/ml/datasets/Balance+Scale](https://archive.ics.uci.edu/ml/databases/balance-scale/balance-scale.data)

Nombre del archivo: `balance-scale.data`

### 3.2 🏛️ Fuentes Históricas y Metodológicas

Este dataset fue creado para simular resultados psicológicos de experimentos con balanzas, pero su aplicación principal se ha trasladado al ámbito de la minería de datos y el aprendizaje automático. A diferencia de muchos conjuntos de datos, no contiene datos reales ni sintéticos de mediciones físicas, sino que todas las instancias fueron generadas sistemáticamente para cubrir combinaciones posibles de los atributos dentro de su rango (1-5), resultando en 625 instancias (5^4).

## 4. 🔁 Proceso de Generación

El dataset es el resultado de una enumeración completa de todas las combinaciones posibles de sus cuatro atributos, cada uno con valores de 1 a 5. Para cada combinación, la clase objetivo se asignó de manera determinista aplicando la ley de la palanca. Este proceso garantiza:

- Un espacio de instancias completo y sin ambigüedades.
- Ausencia de valores faltantes o ruido.
- Una relación funcional exacta y conocida entre las características y la clase.

## 5. 🎯 Valor Analítico
Este dataset ofrece un entorno analítico claro y controlado, ideal para:
- Clasificación multiclase (3 clases: Izquierda, Derecha, Equilibrio).
- Análisis de reglas de decisión basadas en productos cruzados (peso × distancia).
- Evaluación de modelos simples como árboles de decisión, k-NN o redes neuronales.
- Estudios de sobreajuste y generalización en conjuntos de datos pequeños pero complejos.
- Estudios de sobreajuste en conjuntos pequeños.
- Visualización de espacios de decisión binarios.
- Enseñanza de conceptos fundamentales de ML, ya que el "modelo perfecto" es conocido y puede verificarse.

Con 625 instancias completas y una distribución asimétrica de clases (la clase de equilibrio B es minoritaria), representa un escenario excelente para probar la robustez de los clasificadores frente al desbalanceo de clases.

## 6. 📝 Consideraciones Técnicas
Aunque el dataset es simple, es importante tener en cuenta:
- Las clases están desbalanceadas: hay muchos más casos de "no equilibrio" que de "equilibrio".
- El modelo óptimo puede derivarse analíticamente: si `LeftWeight × LeftDistance > RightWeight × RightDistance → L (Left)`
- Es excelente para demostrar cómo los modelos pueden aprender relaciones no lineales entre atributos.
- Dado que los atributos están en la misma escala (1-5), la normalización no es estrictamente necesaria para muchos algoritmos, pero puede beneficiar a otros (como SVM o redes neuronales).

## 7. 🔗 Acceso y Uso
El dataset está disponible bajo licencia abierta para investigación y enseñanza. Se recomienda citar adecuadamente el repositorio UCI.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con el DataLoader de la biblioteca `rna` (Recomendado):
```python
# Instalar la biblioteca si no está disponible:
# !pip install https://github.com/RNA-UNIV/rna/archive/refs/heads/main.zip

from rna.data.ClassDataLoader import DataLoader

# Cargar el dataset como DataFrame de Pandas
df = DataLoader.load_dataframe('balance')
```

**Acceso via UCI:**
```python
import pandas as pd
from sklearn.datasets import fetch_ucirepo

# Método 1: Desde UCI directamente
balance_scale = fetch_ucirepo(id=1)  # ID específico para Balance Scale dataset

# Datos como dataframes de pandas
X = balance_scale.data.features
y = balance_scale.data.targets

# Metadatos
print(balance_scale.metadata)
print(balance_scale.variables)
```

Acceso vía Scikit-Learn:
```python
import pandas as pd
from sklearn.datasets import fetch_openml

# Método 2: Desde Scikit-Learn (Open ML)
balance_scale = fetch_openml(name='balance-scale', version=1, as_frame=True)

# Datos como DataFrames de pandas
X = balance_scale.data  # Características (atributos)
y = balance_scale.target # Etiquetas (clase objetivo)

# Metadatos
print(balance_scale.details)
print("Nombres de las características:", balance_scale.feature_names)
print("Nombres de las clases:", balance_scale.target_names)
```

Acceso vía local:
```python
# Método 2: Desde archivo local (como el proporcionado balance.csv)
df = pd.read_csv('balance.csv')

# Separar características y etiquetas
X = df.drop(columns=['ClassName'])
y = df['ClassName']

# Información del dataset
print("Columnas:", df.columns.tolist())
print("Dimensiones:", df.shape)
print("\nPrimeras filas:\n", df.head())
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

url = "https://raw.githubusercontent.com/rna-univ/datasets/main/balnce/balnce.csv"
df = pd.read_csv(url)

# Separar características y etiquetas
X = df.drop(columns=['ClassName'])
y = df['ClassName']

# Información del dataset
print("Columnas:", df.columns.tolist())
print("Dimensiones:", df.shape)
print("\nPrimeras filas:\n", df.head())
```

## 🔖 8. Cita Recomendada: 
No author specified. (1990). Balance Scale Dataset. UCI Machine Learning Repository.
Recuperado de: https://archive.ics.uci.edu/ml/databases/balance-scale/  