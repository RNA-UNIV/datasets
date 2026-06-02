# 🎈 Dataset Clasificación de Globos: Predicción de Inflado
## 1. 📖 Descripción General
El conjunto de datos de Clasificación de Globos es una herramienta educativa clásica para principiantes en aprendizaje automático y minería de datos. Este dataset contiene información sobre características físicas de globos y si pueden inflarse o no, permitiendo desarrollar modelos predictivos para determinar la viabilidad de inflado basado en atributos observables.

Los datos reflejan relaciones lógicas entre factores como color, tamaño, capacidad de estiramiento y edad del usuario, lo que lo convierte en un recurso ideal para ejercicios de clasificación binaria y aprendizaje de árboles de decisión en contextos educativos.

**Nota importante**: Esta es una adaptación en español del dataset clásico "Balloons" o "Inflating Balloons", con los atributos traducidos y valores categóricos en español.

## 2. 📊 Atributos y Significados

### 2.1 🎯 Variable Objetivo
**Inflado?**: Indica si el globo puede inflarse o no.
 - `Si`: El globo puede inflarse correctamente
 - `No`: El globo no puede inflarse

### 2.2 🎨 Atributos Físicos y Contextuales
**Color**: Color del globo.
 - `Amarillo`: Globos de color amarillo
 - `Rojo`: Globos de color rojo

**Tamanio**: Tamaño del globo.
 - `Chico`: Tamaño pequeño
 - `Mediano`: Tamaño mediano
 - `Grande`: Tamaño grande

**Se_estira?**: Capacidad de estiramiento del material.
 - `Si`: El material se estira
 - `No`: El material no se estira

**Edad**: Grupo de edad de la persona que intenta inflar el globo.
 - `Adulto`: Persona adulta
 - `Nene`: Niño/a

### 2.3 🏷️ Notas sobre los Atributos
- Todas las variables son categóricas con valores nominales bien definidos.
- El atributo "Inflado?" es categórico y sirve como variable objetivo en tareas de clasificación supervisada.
- Las relaciones entre los atributos siguen patrones lógicos que facilitan el aprendizaje de reglas de decisión.
- No se reportan valores nulos en el archivo, lo que lo hace ideal para análisis iniciales.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Original
El dataset original "Balloons" o "Inflating Balloons" es un conjunto de datos clásico en la comunidad de machine learning, ampliamente utilizado desde la década de 1990 para enseñar conceptos de árboles de decisión y sistemas de reglas.

**Fuentes originales en inglés**:
- **UCI Machine Learning Repository** (mencionado históricamente)
- **Repositorios académicos**: Universidad de Carnegie Mellon, MIT
- **Plataformas educativas**: Weka, Kaggle, OpenML

### 3.2 🌐 Adaptación en Español
Esta versión (`globos.csv`) es una adaptación al español del dataset original, con:
- Nombres de columnas traducidos al español
- Valores categóricos en español
- Mantenimiento de la estructura lógica original

> **Repositorio actual**:  
> 👉 https://github.com/aap-unlp/datasets/tree/main/globos  
>
> **Archivo**: `globos.csv`

## 4. 🔄 Diferencias con la Versión Original
- **Original**: `Color,Size,Stretch,Age,Inflated` (inglés)
- **Adaptado**: `Color,Tamanio,Se_estira?,Edad,Inflado?` (español)
- Misma estructura de datos y relaciones lógicas
- Equivalencia completa de valores categóricos

## 5. 🎯 Valor Analítico
Este dataset ofrece múltiples oportunidades para el aprendizaje:
- Clasificación binaria (inflado vs no inflado)
- Construcción y interpretación de árboles de decisión
- Preprocesamiento de variables categóricas (one-hot encoding, label encoding)
- Análisis de importancia de características
- Evaluación de modelos de clasificación simples
- Enseñanza de sobreajuste y generalización
- Introducción a la minería de reglas de asociación

## 6. 📝 Consideraciones
Los datos son sintéticos y creados específicamente para fines educativos. Representan un escenario simplificado diseñado para hacer tangible el proceso de clasificación en machine learning.

## 7. 🔗 Acceso y Uso
El dataset está disponible para uso educativo sin restricciones.

### 7.1 📥 Cómo cargarlo en Python:

Acceso vía UCI:
```python
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
balloons = fetch_ucirepo(id=13) 
  
# data (as pandas dataframes) 
X = balloons.data.features 
y = balloons.data.targets 
  
# metadata 
print(balloons.metadata) 
  
# variable information 
print(balloons.variables) 

```
Acceso vía GitHub
```python
import pandas as pd

# Desde GitHub
github_url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/globos/globos.csv"
globos_df = pd.read_csv(github_url)

# Desde archivo local (si lo tienes descargado)
# globos_df = pd.read_csv('D:/Desarrollo/Github Repositories/datasets/globos/globos.csv')

# Separar características y etiquetas
X = globos_df.drop(columns=['Inflado?'])
y = globos_df['Inflado?']

# Información del dataset
print("Columnas:", globos_df.columns.tolist())
print("Dimensiones:", globos_df.shape)
print("Primeras filas:\n", globos_df.head())
print("\nDistribución de la variable objetivo:")
print(y.value_counts())
```

## 8. 🔖 Cita Recomendada:

Dataset original:
> Pazzani, M. (1991). Balloons [Dataset]. UCI Machine Learning Repository. \
> https://doi.org/10.24432/C5BP4D

Adaptación en español:
> Dataset de Clasificación de Globos. (2020). Adaptación al español. Universidad Nacional de La Plata.
https://github.com/aap-unlp/datasets/tree/main/globos

---

*Última actualización: Diciembre 2024
Adaptación al español mantenida para propósitos educativos en ciencia de datos y machine learning.*
