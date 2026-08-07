<p align="center">
<img src="banner.png" width="1000">
</p>

# 🌦️ Dataset Jena Climate (2009–2016)

## 1. 📖 Descripción General

El dataset **Jena Climate** contiene registros meteorológicos obtenidos por la estación del **Max Planck Institute for Biogeochemistry**, ubicada en Jena, Alemania. Las mediciones fueron realizadas cada **10 minutos** entre enero de 2009 y diciembre de 2016, generando más de **420 mil observaciones**.

Este conjunto de datos se ha convertido en uno de los ejemplos clásicos para el estudio de **series temporales** y es utilizado frecuentemente en cursos de Deep Learning y TensorFlow para desarrollar modelos de predicción basados en redes neuronales recurrentes (RNN, LSTM, GRU), Transformers y otros modelos de forecasting.

La versión utilizada en este repositorio proviene de una copia pública del dataset original distribuida a través de Kaggle.

---

# 2. 📊 Variables del Dataset

Cada fila representa una medición realizada aproximadamente cada **10 minutos**.

## 2.1 🌡 Variables Atmosféricas

**T (degC)** (Temperatura)
- Temperatura del aire en grados Celsius.
- Es la variable objetivo más utilizada en problemas de predicción.

**Tpot (K)** (Temperatura potencial)
- Temperatura potencial del aire expresada en Kelvin.

**Tdew (degC)** (Punto de rocío)
- Temperatura a la cual comienza la condensación del vapor de agua.

**rh (%)** (Humedad relativa)
- Humedad relativa del aire.

---

## 2.2 🌬 Viento

**wv (m/s)**
- Velocidad del viento.

**max. wv (m/s)**
- Velocidad máxima del viento.

**wd (deg)**
- Dirección del viento en grados.

---

## 2.3 ☁ Humedad y Vapor

**VPmax (mbar)**
- Presión máxima de vapor.

**VPact (mbar)**
- Presión real de vapor.

**VPdef (mbar)**
- Déficit de presión de vapor.

**sh (g/kg)**
- Humedad específica.

**H2OC (mmol/mol)**
- Concentración de vapor de agua.

---

## 2.4 🌍 Variables Físicas

**p (mbar)**
- Presión atmosférica.

**rho (g/m³)**
- Densidad del aire.

---

## 2.5 🕒 Tiempo

**Date Time**
- Fecha y hora de la medición.

---

# 3. 🏢 Origen y Procedencia

## 3.1 Fuente Original

Los datos fueron registrados por:

**Max Planck Institute for Biogeochemistry**
Jena, Alemania

Posteriormente fueron publicados para investigación y utilizados por TensorFlow en numerosos ejemplos oficiales sobre predicción de series temporales.

---

# 4. 🔄 Curaduría

El dataset original contiene mediciones prácticamente continuas durante ocho años.

Durante el proceso de adquisición pueden aparecer:

- registros incompletos;
- valores faltantes ocasionados por fallas temporales de sensores;
- valores atípicos asociados principalmente a mediciones de velocidad del viento.

En la mayoría de las aplicaciones es recomendable realizar una etapa previa de limpieza que incluya:

- detección de valores faltantes;
- interpolación temporal o imputación;
- tratamiento de valores extremos;
- normalización o estandarización de las variables.

---

# 5. 🎯 Valor Analítico

Este dataset resulta especialmente interesante porque:

- posee más de 420.000 observaciones;
- contiene múltiples variables meteorológicas correlacionadas;
- presenta una resolución temporal constante (10 minutos);
- permite estudiar dependencias temporales de corto y largo plazo;
- es ideal para modelos de forecasting;
- puede utilizarse para detección de anomalías y análisis exploratorio.

Aplicaciones frecuentes:

- predicción de temperatura;
- predicción multivariable;
- forecasting de series temporales;
- detección de anomalías;
- comparación entre modelos clásicos y Deep Learning.

---

# 6. 📝 Consideraciones

El dataset no contiene información personal ni datos sensibles.

Debe tenerse en cuenta que:

- existen registros faltantes en algunas variables;
- algunas implementaciones públicas eliminan o imputan dichos registros antes del entrenamiento;
- la variable **Date Time** debe convertirse a formato temporal para aprovechar adecuadamente la información estacional y periódica.

---

# 7. 🔗 Acceso y Uso

## Cargar con la biblioteca RNA

```python
from rna.data.ClassDataLoader import DataLoader

df = DataLoader.load_dataframe("jena_climate")
```

## Cargar desde CSV

```python
import pandas as pd

df = pd.read_csv("jena_climate.csv")

print(df.head())
```

---

# 8. 🔖 Referencia

Max Planck Institute for Biogeochemistry.

Jena Climate Dataset (2009–2016).

Utilizado en numerosos ejemplos oficiales de TensorFlow para predicción de series temporales.

---

*Última actualización: Agosto 2026*

*Mantenido para fines educativos y de investigación.*