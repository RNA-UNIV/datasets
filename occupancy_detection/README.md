<p align="center">
<img src="banner.png" width="1000">
</p>

# 🏢 Dataset Occupancy Detection: Detección de Ocupación de Habitaciones mediante Sensores Ambientales

## 1. 📖 Descripción General
El dataset "Occupancy Detection" es un conjunto de datos moderno y altamente relevante para problemas de clasificación binaria en el ámbito del Internet de las Cosas (IoT) y eficiencia energética. Fue creado por Luis Candanedo y publicado en el repositorio UCI en 2016. Este dataset contiene mediciones temporales de sensores ambientales (temperatura, humedad, luz, CO₂) recogidas en una habitación, junto con la etiqueta de ocupación real obtenida mediante fotografías con marca de tiempo.

El conjunto de datos es especialmente valioso para tareas de **clasificación binaria** (predecir si una habitación está ocupada o vacía), y es ideal para ejercicios introductorios de machine learning debido a que **todas las variables predictoras son numéricas continuas**, lo que elimina la necesidad de codificar variables categóricas. Además, su tamaño (20,560 instancias) es perfecto para obtener resultados robustos sin requerir grandes recursos computacionales.

La versión utilizada en este análisis proviene del repositorio oficial de UCI Machine Learning Repository, una fuente confiable y ampliamente citada en investigaciones académicas y proyectos educativos.

## 2. 📊 Atributos y Significados

### 2.1 🎯 Variable Objetivo
**Occupancy** (Ocupación): Variable binaria que indica si la habitación está ocupada en el momento de la medición.
- `0`: Habitación no ocupada (vacía)
- `1`: Habitación ocupada (con al menos una persona presente)
- **Método de obtención**: Fotografías con marca de tiempo tomadas cada minuto, verificadas manualmente

### 2.2 📅 Atributo Temporal
**date** (Fecha y hora): Marca de tiempo de cada observación en formato `año-mes-día hora:minuto:segundo`.
- Rango temporal: 11/02/2015 14:12:00 – 10/02/2015 10:30:00 (aproximadamente 14 días)
- **Frecuencia de muestreo**: Cada minuto
- **Uso típico**: Puede usarse para análisis de series temporales o ser descartado para modelos estándar

### 2.3 🌡️ Sensores Ambientales (Variables Predictoras)

**Temperature** (Temperatura): Temperatura ambiente medida en grados Celsius.
- Rango: 19.0 – 25.5 °C
- **Sensor**: Termómetro digital
- **Interpretación física**: La presencia humana tiende a aumentar ligeramente la temperatura ambiente

**Humidity** (Humedad relativa): Cantidad de vapor de agua en el aire, expresada como porcentaje.
- Rango: 19.0 – 60.0 %
- **Sensor**: Higrómetro
- **Interpretación física**: La respiración y sudoración humanas incrementan la humedad ambiental

**Light** (Iluminación): Intensidad de luz ambiental medida en Lux.
- Rango: 0 – 1,920 Lux (valores típicos: muy bajo cuando está vacío, alto cuando está ocupado)
- **Sensor**: Fotodiodo o sensor de luz
- **Interpretación física**: En una oficina, las luces suelen encenderse cuando hay personas presentes

**CO₂** (Dióxido de carbono): Concentración de dióxido de carbono en partes por millón (ppm).
- Rango: 330 – 2,000 ppm (valores típicos: ~400 ppm en exteriores, >1,000 ppm indica ocupación prolongada)
- **Sensor**: Sensor de CO₂ no dispersivo (NDIR)
- **Interpretación física**: Los humanos exhalamos CO₂ constantemente; su acumulación es un excelente indicador de ocupación

**HumidityRatio** (Relación de humedad): Cantidad derivada de temperatura y humedad relativa.
- Rango: 0.0026 – 0.0127 kg de vapor de agua / kg de aire seco
- **Cálculo**: Se obtiene a partir de `Temperature` y `Humidity` mediante ecuaciones psicrométricas
- **Interpretación física**: Representa la masa real de vapor de agua por unidad de masa de aire seco, independiente de la temperatura

### 2.4 📊 Resumen de Tipos de Datos

| Atributo | Tipo | Naturaleza | Valores Faltantes |
|:---|:---|:---|:---|
| date | Temporal (datetime) | Secuencial | No |
| Temperature | Numérico (float) | Continuo | No |
| Humidity | Numérico (float) | Continuo | No |
| Light | Numérico (int) | Discreto (conteo) | No |
| CO₂ | Numérico (float) | Continuo | No |
| HumidityRatio | Numérico (float) | Continuo | No |
| Occupancy | Binario (int) | Categórico objetivo | No |

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: UCI Machine Learning Repository
El dataset fue obtenido del repositorio oficial:
- **URL**: https://archive.ics.uci.edu/dataset/357/occupancy+detection
- **ID del dataset**: 357
- **Donado por**: Luis Candanedo (2016)

### 3.2 🏛️ Fuentes Originales
Los datos fueron recogidos experimentalmente en una habitación con condiciones controladas:
- **Ubicación**: Instalaciones de investigación (Universidad de Ciencias Aplicadas de Amberes, Bélgica)
- **Periodo de recolección**: Febrero de 2015 (aproximadamente 14 días)
- **Configuración**: Sensores colocados estratégicamente para capturar cambios ambientales por presencia humana
- **Verificación de la verdad fundamental (ground truth)**: Cámaras fotográficas con marca de tiempo, revisadas manualmente para evitar errores

## 4. 🔄 Proceso de Curaduría
El dataset ha pasado por un proceso de curaduría que incluye:
- **Limpieza inicial**: Eliminación de valores atípicos obvios y errores de medición
- **Estandarización de formatos**: Unificación de la representación de fechas y valores numéricos
- **Documentación detallada**: Descripción completa de cada sensor y su unidad de medida
- **División predefinida**: Separación en conjuntos de entrenamiento (`datatraining.txt`) y prueba (`datatest.txt`, `datatest2.txt`) para facilitar la comparación de resultados
- **Disponibilidad pública**: Bajo licencia Creative Commons

## 5. 🎯 Valor Analítico
Este dataset presenta características ideales para el aprendizaje automático y la investigación:

| Característica | Beneficio Didáctico |
|:---|:---|
| **Tamaño manejable** (20,560 instancias) | Suficiente para modelos robustos sin requerir GPUs ni largos tiempos de entrenamiento |
| **Solo variables numéricas** (5 predictoras) | Sin necesidad de codificar categóricas; ideal para primeros contactos con ML |
| **Sin valores faltantes** | Permite centrarse en el modelado, no en la limpieza compleja |
| **Problema de clasificación binaria clara** | Intuitivo para estudiantes: "¿hay alguien en la habitación?" |
| **Relaciones causales interpretables** | El CO₂ y la luz tienen lógica física directa con la ocupación |
| **División train/test predefinida** | Facilita la reproducibilidad y comparación de resultados |
| **Potencial para series temporales** | El atributo `date` permite análisis avanzados (LSTM, Prophet) |

## 6. 📝 Consideraciones Éticas
Este dataset no contiene información personal identificable, ya que las mediciones son exclusivamente ambientales y las fotografías utilizadas para etiquetar no se incluyen en el conjunto de datos público. Sin embargo, es importante considerar:

- **Privacidad por diseño**: El dataset demuestra que es posible detectar ocupación sin utilizar cámaras ni micrófonos, lo que tiene implicaciones positivas para la privacidad en edificios inteligentes.
- **Uso responsable**: Los modelos entrenados con estos datos podrían aplicarse a sistemas de monitoreo; se recomienda su uso para eficiencia energética y no para vigilancia no consentida.
- **Contexto limitado**: Los datos fueron recogidos en una habitación específica con condiciones particulares; la generalización a otros espacios debe hacerse con precaución.

## 7. 🔗 Acceso y Uso
El dataset está disponible públicamente bajo una licencia **Creative Commons Attribution 4.0 International (CC BY 4.0)** , lo que permite su uso, modificación y distribución, siempre que se dé el crédito adecuado a Luis Candanedo y al UCI Machine Learning Repository.

### 7.1 📥 Cómo cargarlo en Python:

**Acceso vía librería `ucimlrepo` (recomendado):**

```python
from ucimlrepo import fetch_ucirepo

# Fetch dataset
occupancy = fetch_ucirepo(id=357)

# Data (as pandas dataframes)
X = occupancy.data.features   # Variables predictoras
y = occupancy.data.targets     # Variable objetivo (Occupancy)

# Metadata
print(occupancy.metadata)

# Variable information
print(occupancy.variables)
```
Acceso vía repositorio GitHub:
```python
import pandas as pd

# Para cargar el archivo de entrenamiento
train_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00357/occupancy_data/datatraining.txt"
train_data = pd.read_csv(train_url, sep=',')

# Separar características y etiquetas
X_train = train_data.drop(['date', 'Occupancy'], axis=1)
y_train = train_data['Occupancy']

# Ver información del dataset
print("Columnas:", X_train.columns.tolist())
print("Primeras filas:\n", X_train.head())
print("Distribución de clases:\n", y_train.value_counts())
```

## 8. 🔖 Cita Recomendada:
Para referenciar este dataset en publicaciones académicas, utilice la siguiente cita:

    Candanedo, L. (2016). Occupancy Detection Dataset. UCI Machine Learning Repository. https://doi.org/10.24432/C5X01N
---
*Última actualización: Febrero 2016*
*Mantenido por la comunidad de ciencia de datos para propósitos educativos y de investigación.*