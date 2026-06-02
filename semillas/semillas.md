# 🌾 Dataset de Semillas: Clasificación de Variedades de Trigo

## 1. 📖 Descripción General

El **Seed Dataset** es un conjunto de datos clásico y fundamental en el ámbito del reconocimiento de patrones y el aprendizaje automático. Este dataset fue creado para la clasificación de variedades de trigo basándose en características geométricas extraídas de imágenes de sus granos.

La versión utilizada en este análisis proviene del **repositorio de Machine Learning de la Universidad de California, Irvine (UCI)**, una fuente de referencia en ciencia de datos. Este conjunto de datos ha sido ampliamente utilizado durante décadas en la literatura de machine learning como benchmark para algoritmos de clasificación, especialmente en problemas de discriminación morfológica.

Lo que lo hace especialmente valioso es su **origen real y su perfecta condición**: todos los registros fueron medidos meticulosamente a partir de muestras reales de trigo, lo que lo convierte en un estándar confiable para probar la capacidad de los modelos para distinguir entre categorías estrechamente relacionadas basándose en mediciones físicas.

Este dataset representa un caso de estudio excelente para comprender cómo las propiedades geométricas pueden definir la pertenencia a una categoría biológica, y sirve como base para el desarrollo de sistemas de clasificación automatizada en agricultura y biometría.

## 2. 📊 Atributos y Significados

Todas las características se midieron a partir de imágenes de rayos X de los granos de trigo. Todas las variables son numéricas continuas, excepto la clase objetivo.

## 2.1 🔑 Variable Objetivo

**Clase**: Variedad de trigo a la que pertenece el grano.
- `Tipo1`: Trigo Kama
- `Tipo2`: Trigo Rosa  
- `Tipo3`: Trigo Canadian

## 2.2 📐 Atributos Geométricos (medidas en mm)

**Area (Área)**: Área de la sección transversal del grano.

**Perimetro (Perímetro)**: Perímetro exterior del grano.

**Compacidad**: Medida de compacidad calculada como `(perímetro²) / área - 1.0`.

**LongNucleo (Longitud del núcleo)**: Longitud del núcleo del grano.

**AnchoNucleo (Ancho del núcleo)**: Ancho del núcleo del grano.

**Asimetria (Coeficiente de asimetría)**: Medida de la asimetría del grano.

**LongSurco (Longitud del surco)**: Longitud del surco del grano.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository

El dataset fue obtenido del repositorio oficial de la Universidad de California, Irvine, una de las fuentes más respetadas en ciencia de datos y aprendizaje automático.

**URL Oficial**:  
👉 [https://archive.ics.uci.edu/ml/datasets/seeds](https://archive.ics.uci.edu/ml/datasets/seeds)

**Nombre del archivo**: `seeds_dataset.txt`

### 3.2 🏛️ Fuentes Históricas y Metodológicas

Este dataset se basa en una investigación académica realizada en la Universidad de Agricultura de Lublin, Polonia. Los datos fueron recolectados de forma exhaustiva:

- **100% datos reales**: Medidos directamente a partir de imágenes de rayos X de granos de trigo reales.
- **Técnica de medición**: Utilizando software especializado de análisis de imágenes para extraer las características geométricas con precisión.

**Investigadores principales**:  
> M. Charytanowicz, J. Niewczas, P. Kulczycki, P. A. Kowalski, S. Łukasik, S. Żak  
> Universidad de Agricultura de Lublin, Polonia

## 4. 🔁 Proceso de Curaduría

El equipo de investigación realizó un proceso meticuloso de medición y validación que incluye:

- Captura de imágenes de rayos X de alta calidad
- Extracción precisa de características geométricas mediante software especializado
- Verificación manual de las mediciones
- Eliminación de mediciones inconsistentes
- Clasificación experta de cada grano según su variedad
- Documentación detallada de cada variable

## 5. 🎯 Valor Analítico

Este dataset ofrece un entorno analítico clásico y robusto, ideal para:

- **Clasificación multiclase** (3 variedades de trigo).
- **Análisis discriminante** entre categorías morfológicas similares.
- **Reducción de dimensionalidad** (las características están correlacionadas).
- **Modelos de clasificación** con SVM, K-NN, Random Forest, etc.
- **Visualización de datos** multidimensionales.
- **Estudios de selección de características**.

Su tamaño manejable (210 instancias, 7 atributos) y la perfecta separabilidad de las clases lo convierten en un recurso excelente para la enseñanza de conceptos fundamentales de machine learning y reconocimiento de patrones.

## 6. 📝 Consideraciones Técnicas

Aunque el dataset es técnicamente sólido, es importante considerar:

- Las variables están altamente correlacionadas (la compacidad se deriva del área y perímetro)
- Las escalas de las variables son diferentes, por lo que often se recomienda normalizar
- El dataset es pequeño pero bien balanceado (70 instancias por clase)
- Perfecto para demostrar la importancia del preprocesamiento de datos

## 7. 🔗 Acceso y Uso

El dataset está disponible bajo **licencia abierta** para investigación y enseñanza. Se recomienda citar adecuadamente el repositorio UCI.

### 7.1 📥 Cómo cargarlo en Python:

Acceso via UCI:
```python
import pandas as pd
from sklearn.datasets import fetch_ucirepo

# Método 1: Desde UCI directamente
seeds = fetch_ucirepo(id=236)  # ID específico para Seeds dataset

# Datos como dataframes de pandas
X = seeds.data.features
y = seeds.data.targets

# Metadatos
print(seeds.metadata)
print(seeds.variables)
```
Acceso vía local:
```python
# Método 2: Desde archivo local (como el proporcionado semillas.csv)
df = pd.read_csv('semillas.csv')

# Separar características y etiquetas
X = df.drop(columns=['Clase'])
y = df['Clase']

# Información del dataset
print("Columnas:", df.columns.tolist())
print("Dimensiones:", df.shape)
print("\nPrimeras filas:\n", df.head())
```
Acceso vía repositorio GitHub:
```python
import pandas as pd

url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/semillas/semillas.csv"
df = pd.read_csv(url)

# Separar características y etiquetas
X = df.drop(columns=['Clase'])
y = df['Clase']

# Información del dataset
print("Columnas:", df.columns.tolist())
print("Dimensiones:", df.shape)
print("\nPrimeras filas:\n", df.head())
```
## 8.🔖 Cita Recomendada:
[deepseek_python_20250911_500f72.py](../../../../Sistema/Archivos/FDM/Descargas/cv-corpus-22.0-2025-06-20/deepseek_python_20250911_500f72.py)
    Charytanowicz, M., Niewczas, J., Kulczycki, P., Kowalski, P. A., Łukasik, S., & Żak, S. (2010). A complete gradient clustering algorithm for features analysis of X-ray images. Information Technologies in Biomedicine, Ewa Pietka and Jacek Kawa (Eds.), Springer-Verlag, Berlin-Heidelberg.
    Recuperado de: https://archive.ics.uci.edu/ml/datasets/seeds