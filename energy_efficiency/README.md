<p align="center">
<img src="banner.png" width="1000">
</p>

# 🏠 Dataset Eficiencia Energética en Edificios: Predicción de Carga de Calefacción y Refrigeración
## 1. 📖 Descripción General
El dataset "Energy Efficiency" es un conjunto de datos ampliamente utilizado en el campo del machine learning para tareas de regresión aplicadas a la eficiencia energética de edificios. Fue construido mediante simulaciones en el software Ecotect, analizando 12 formas edilicias distintas bajo diferentes combinaciones de área vidriada, distribución del vidriado y orientación, obteniendo un total de 768 configuraciones de edificios.

Este dataset es especialmente valioso para tareas de regresión (predecir la carga de calefacción y/o refrigeración de un edificio a partir de sus características arquitectónicas) y también puede adaptarse a tareas de clasificación multiclase si las variables objetivo se redondean al entero más cercano. Al no contener valores faltantes, resulta ideal para ejercicios introductorios de regresión, análisis exploratorio y regresión multisalida (multi-output regression).

La versión utilizada en este análisis proviene del repositorio oficial de UCI Machine Learning Repository, una fuente confiable y ampliamente citada en investigaciones académicas y proyectos educativos.

## 2. 📊 Atributos y Significados
### 2.1 🔍 Variables Objetivo
**Heating_Load** (Carga de calefacción): Valor continuo que representa la energía necesaria para calefaccionar el edificio.
- Unidad: kWh/m²
- Valores faltantes: No

**Cooling_Load** (Carga de refrigeración): Valor continuo que representa la energía necesaria para refrigerar el edificio.
- Unidad: kWh/m²
- Valores faltantes: No

> Ambas variables pueden predecirse de forma independiente (regresión simple) o de manera conjunta (regresión multisalida), ya que comparten el mismo conjunto de atributos de entrada.

### 2.2 🏗️ Atributos Geométricos y Arquitectónicos
**Relative_Compactness** (Relación de compacidad relativa): Indica cuán compacta es la forma del edificio en relación con una forma de referencia (a mayor compacidad, menor superficie externa por unidad de volumen).

**Surface_Area** (Área de superficie): Área de superficie total del edificio.

**Wall_Area** (Área de pared): Área total de las paredes exteriores.

**Roof_Area** (Área de techo): Área total del techo.

**Overall_Height** (Altura de edificio): Altura total del edificio.
- Valores típicos: 3.5 o 7 (dos niveles de altura simulados)

**Orientation** (Orientación): Orientación cardinal del edificio, codificada numéricamente.
- `2`, `3`, `4`, `5`: Corresponden a las distintas orientaciones simuladas

**Glazing_Area** (Área vidriada): Proporción del área acristalada (ventanas) respecto al área total del edificio.

**Glazing_Area_Distribution** (Distribución de vidrio): Forma en que el área vidriada se distribuye entre las distintas caras del edificio (norte, sur, este, oeste, uniforme, etc.), codificada numéricamente.

## 3. 🏢 Origen y Procedencia
### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository
El dataset fue obtenido del repositorio oficial:
- **URL**: https://archive.ics.uci.edu/dataset/242/energy+efficiency
- **ID del dataset**: 242
- **Creado por**: Angeliki Xifara (Ingeniera Civil/Estructural)
- **Procesado por**: Athanasios Tsanas (Oxford Centre for Industrial and Applied Mathematics, Universidad de Oxford, Reino Unido)

### 3.2 🏛️ Metodología de Origen
Los datos fueron generados mediante simulaciones energéticas realizadas con el software Ecotect sobre 12 formas edilicias base, variando parámetros como el área vidriada, su distribución y la orientación del edificio, hasta obtener las 768 configuraciones que componen el dataset.

## 4. 🔄 Proceso de Curaduría
El repositorio UCI ha realizado una curaduría básica del dataset original, incluyendo:
- Estandarización de formatos
- Documentación detallada de atributos
- Confirmación de ausencia de valores faltantes
- Disponibilidad pública bajo licencia abierta

## 5. 🎯 Valor Analítico
Este dataset presenta características ideales para el aprendizaje y la investigación:
- Tamaño manejable (768 instancias, 8 atributos de entrada)
- Atributos íntegramente numéricos, sin necesidad de codificación de variables categóricas complejas
- Sin valores faltantes (no requiere imputación)
- Tarea de regresión multisalida (predicción simultánea de dos variables continuas)
- También adaptable a clasificación multiclase redondeando las variables objetivo
- Contexto técnico real, aplicado a arquitectura sustentable y eficiencia energética

## 6. 📝 Consideraciones Éticas
Este dataset no contiene información personal ni sensible, ya que proviene de simulaciones sobre formas edilicias abstractas. Su uso está orientado a la investigación en eficiencia energética y diseño sustentable, promoviendo aplicaciones responsables en el ámbito de la construcción y el ahorro energético.

## 7. 🔗 Acceso y Uso
El dataset está disponible públicamente bajo una licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)**, lo que permite su uso, modificación y distribución, siempre que se dé el crédito adecuado.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con el DataLoader de la biblioteca `rna` (Recomendado):
```python
# Instalar la biblioteca si no está disponible:
# !pip install https://github.com/RNA-UNIV/rna/archive/refs/heads/main.zip

from rna.data.ClassDataLoader import DataLoader

# Cargar el dataset como DataFrame de Pandas
df = DataLoader.load_dataframe('energy_efficiency')
```

Acceso vía UCI:
```python
from ucimlrepo import fetch_ucirepo

# fetch dataset 
energy_efficiency_ds = fetch_ucirepo(id=242)

# data (as pandas dataframes) 
X = energy_efficiency_ds.data.features
y = energy_efficiency_ds.data.targets

# metadata 
print(energy_efficiency_ds.metadata) 
  
# variable information 
print(energy_efficiency_ds.variables) 
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

# url del repositorio github para descargar
url = "https://raw.githubusercontent.com/rna-univ/datasets/main/energy_efficiency/energy_efficiency.csv"
energy_efficiency_ds = pd.read_csv(url)

# Separar características y etiquetas
# Variables objetivo: Heating_Load, Cooling_Load
X = energy_efficiency_ds.drop(columns=['Heating_Load', 'Cooling_Load'])
y = energy_efficiency_ds[['Heating_Load', 'Cooling_Load']]

# Información del dataset
print("Columnas:", energy_efficiency_ds.columns.tolist())
print("Primeras filas:\n", energy_efficiency_ds.head())
```
## 8. 🔖 Cita Recomendada:
>Tsanas, A. & Xifara, A. (2012). Energy Efficiency [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C51307.

>A. Tsanas, A. Xifara: 'Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools', Energy and Buildings, Vol. 49, pp. 560-567, 2012.

---
*Última actualización: Julio 2026*
*Mantenido por la comunidad de ciencia de datos para propósitos educativos y de investigación.*
