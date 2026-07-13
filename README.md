<p align="center">
<img src="banner.png" width="1000">
</p>

# 📦 RNA — Repositorio de Datasets

Colección de datasets para prácticas y proyectos de machine learning, mantenida por la comunidad **RNA-UNIV**. Está diseñada para ser usada en conjunto con el **DataLoader** del repositorio de código para aprendizaje de redes neuronales [rna](https://github.com/RNA-UNIV/rna), que permite descargar y cargar cualquier dataset con pocas líneas de código.

---

## 🗂️ Estructura del Repositorio

Cada dataset ocupa su propia carpeta y contiene al menos dos archivos:

```
nombre_dataset/
├── info.json       # Metadatos del dataset (tipo, tareas, clases, muestras, etc.)
├── README.md       # Descripción detallada, atributos, origen y ejemplos de uso
└── ...             # Archivos de datos (CSV, imágenes, etc.)
```

### 📄 `info.json`
Archivo de metadatos estructurado que el DataLoader utiliza para identificar y describir el dataset. Incluye campos como `nombre`, `tipo`, `tareas`, `muestras`, `clases`, entre otros. El schema completo con todas las opciones válidas está documentado en [`info_schema.json`](info_schema.json).

### 📝 `README.md`
Documentación detallada de cada dataset: descripción general, atributos, origen y procedencia, proceso de curaduría, consideraciones éticas y ejemplos de carga en Python.

### ☁️ Archivos de datos
Los archivos de datos pequeños (< 50 MB) se almacenan directamente en la carpeta del dataset. Los datasets más grandes se distribuyen como archivos `.zip` en los [**Assets de los Releases**](../../releases) del repositorio, y el DataLoader los descarga y extrae automáticamente.

---

## 🚀 Uso con DataLoader

```python
from rna.data import DataLoader

# Ver datasets disponibles
DataLoader.list_datasets()

# Ver información de un dataset
DataLoader.dataset_info_display("iris")
```

Datasets tabulares (CSV):
```python
# Como DataFrame de pandas
df = DataLoader.load_dataframe("iris")

# Como array numpy
columnas, data = DataLoader.load_array("iris")
```

Datasets de imágenes:
```python
# Carga completa en memoria (eager)
X, y, clases = DataLoader.load_images("natural_scenes_train", resize=(150, 150))

# Carga lazy como tf.data.Dataset
ds, clases = DataLoader.load_images_dataset("natural_scenes_train", resize=(150, 150))
```

Datasets de audio:
```python
# Carga lazy como tf.data.Dataset
ds, clases = DataLoader.load_audio_dataset("nombre_dataset", sample_rate=16000, duration=1.0)
```

---

## 📋 Datasets Disponibles

### 📊 Tabulares

<table>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile/">automobile</a></b></td>
  <td colspan="5">Especificaciones técnicas detalladas de vehículos junto con información sobre evaluación de riesgo de seguros y pérdidas normalizadas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile_simple/">automobile_simple</a></b></td>
  <td colspan="5">Versión simplificada del dataset Automobile con atributos seleccionados y variables derivadas para fines educativos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>186</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚖️ <a href="balance/">balance</a></b></td>
  <td colspan="5">Dataset basado en experimentos psicológicos sobre percepción del equilibrio.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>625</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚡ <a href="ccpp/">ccpp</a></b></td>
  <td colspan="5">Mediciones ambientales de una planta de ciclo combinado utilizadas para predecir producción eléctrica.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>9.568</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎨 <a href="colores_rgb_16/">colores_rgb_16</a></b></td>
  <td colspan="5">Colores definidos mediante componentes RGB clasificados en 16 categorías.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>1.200</td>
  <td><b>Clases</b><br>16</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💳 <a href="creditcard/">creditcard</a></b></td>
  <td colspan="5">Transacciones con tarjeta de crédito utilizadas para detección de fraude financiero.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>284.807</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💊 <a href="drugs/">drugs</a></b></td>
  <td colspan="5">Información médica utilizada para determinar la elección de medicamentos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>200</td>
  <td><b>Clases</b><br>5</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo<br><small>train (160) · test (40) · atípicos</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🫀 <a href="ecg5000/">ecg5000</a></b></td>
  <td colspan="5">Series temporales de electrocardiogramas utilizadas para clasificación de ritmos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>4.998</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="energy_efficiency/">energy_efficiency</a></b></td>
  <td colspan="5">Características edilicias utilizadas para estimar eficiencia energética.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>768</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>✋ <a href="fingers_features_train/">fingers_features</a></b></td>
  <td colspan="5">Características geométricas extraídas de imágenes de manos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>21.600</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><small>train (17.280) · test (4.320)</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍊 <a href="frutas_train/">frutas</a></b></td>
  <td colspan="5">Dataset sintético para clasificación de frutas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>20</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><small>train (16) · test (4)</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎈 <a href="globos/">globos</a></b></td>
  <td colspan="5">Adaptación del dataset Balloons utilizado para inducción de reglas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>16</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦅 <a href="hawks/">hawks</a></b></td>
  <td colspan="5">Mediciones morfológicas de tres especies de halcones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>893</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="housing/">housing</a></b></td>
  <td colspan="5">Datos habitacionales y demográficos para predicción del valor de viviendas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>20.640</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌸 <a href="iris/">iris</a></b></td>
  <td colspan="5">Mediciones morfológicas de tres especies de flores Iris.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>150</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>👓 <a href="lentes/">lentes</a></b></td>
  <td colspan="5">Dataset clásico para determinar uso de lentes de contacto.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>24</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚕️ <a href="obesity_uci/">obesity_uci</a></b></td>
  <td colspan="5">Estimación de niveles de obesidad mediante hábitos alimentarios y condición física.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>2.111</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏢 <a href="occupancy_detection/">occupancy_detection</a></b></td>
  <td colspan="5">Sensores ambientales para clasificación de ocupación de habitaciones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>9.752</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌾 <a href="semillas/">semillas</a></b></td>
  <td colspan="5">Mediciones geométricas de granos de trigo pertenecientes a tres variedades.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>210</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🔊 <a href="sonar/">sonar</a></b></td>
  <td colspan="5">Señales de sonar para distinguir rocas y minas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>208</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚢 <a href="titanic/">titanic</a></b></td>
  <td colspan="5">Información histórica de pasajeros del Titanic para predicción de supervivencia.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>891</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍷 <a href="wine/">wine</a></b></td>
  <td colspan="5">Análisis químico de vinos de tres cultivares italianos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>178</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦁 <a href="zoo/">zoo</a></b></td>
  <td colspan="5">Clasificación taxonómica de animales basada en características morfológicas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>101</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

</table>

### 📊 Tabulares

<table>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile/">automobile</a></b></td>
  <td colspan="5">Especificaciones técnicas detalladas de vehículos junto con información sobre evaluación de riesgo de seguros y pérdidas normalizadas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile_simple/">automobile_simple</a></b></td>
  <td colspan="5">Versión simplificada del dataset Automobile con atributos seleccionados y variables derivadas para fines educativos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>186</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚖️ <a href="balance/">balance</a></b></td>
  <td colspan="5">Dataset basado en experimentos psicológicos sobre percepción del equilibrio.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>625</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚡ <a href="ccpp/">ccpp</a></b></td>
  <td colspan="5">Mediciones ambientales de una planta de ciclo combinado utilizadas para predecir producción eléctrica.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>9.568</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎨 <a href="colores_rgb_16/">colores_rgb_16</a></b></td>
  <td colspan="5">Colores definidos mediante componentes RGB clasificados en 16 categorías.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>1.200</td>
  <td><b>Clases</b><br>16</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💳 <a href="creditcard/">creditcard</a></b></td>
  <td colspan="5">Transacciones con tarjeta de crédito utilizadas para detección de fraude financiero.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>284.807</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💊 <a href="drugs/">drugs</a></b></td>
  <td colspan="5">Información médica utilizada para determinar la elección de medicamentos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>200</td>
  <td><b>Clases</b><br>5</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo<br><small>train (160) · test (40) · atípicos</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🫀 <a href="ecg5000/">ecg5000</a></b></td>
  <td colspan="5">Series temporales de electrocardiogramas utilizadas para clasificación de ritmos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>4.998</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="energy_efficiency/">energy_efficiency</a></b></td>
  <td colspan="5">Características edilicias utilizadas para estimar eficiencia energética.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>768</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>✋ <a href="fingers_features_train/">fingers_features</a></b></td>
  <td colspan="5">Características geométricas extraídas de imágenes de manos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>21.600</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><small>train (17.280) · test (4.320)</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍊 <a href="frutas_train/">frutas</a></b></td>
  <td colspan="5">Dataset sintético para clasificación de frutas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>20</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><small>train (16) · test (4)</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎈 <a href="globos/">globos</a></b></td>
  <td colspan="5">Adaptación del dataset Balloons utilizado para inducción de reglas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>16</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦅 <a href="hawks/">hawks</a></b></td>
  <td colspan="5">Mediciones morfológicas de tres especies de halcones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>893</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="housing/">housing</a></b></td>
  <td colspan="5">Datos habitacionales y demográficos para predicción del valor de viviendas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>20.640</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌸 <a href="iris/">iris</a></b></td>
  <td colspan="5">Mediciones morfológicas de tres especies de flores Iris.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>150</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>👓 <a href="lentes/">lentes</a></b></td>
  <td colspan="5">Dataset clásico para determinar uso de lentes de contacto.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>24</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚕️ <a href="obesity_uci/">obesity_uci</a></b></td>
  <td colspan="5">Estimación de niveles de obesidad mediante hábitos alimentarios y condición física.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>2.111</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏢 <a href="occupancy_detection/">occupancy_detection</a></b></td>
  <td colspan="5">Sensores ambientales para clasificación de ocupación de habitaciones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>9.752</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌾 <a href="semillas/">semillas</a></b></td>
  <td colspan="5">Mediciones geométricas de granos de trigo pertenecientes a tres variedades.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>210</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🔊 <a href="sonar/">sonar</a></b></td>
  <td colspan="5">Señales de sonar para distinguir rocas y minas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>208</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚢 <a href="titanic/">titanic</a></b></td>
  <td colspan="5">Información histórica de pasajeros del Titanic para predicción de supervivencia.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>891</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍷 <a href="wine/">wine</a></b></td>
  <td colspan="5">Análisis químico de vinos de tres cultivares italianos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>178</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦁 <a href="zoo/">zoo</a></b></td>
  <td colspan="5">Clasificación taxonómica de animales basada en características morfológicas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>101</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

</table>

### 📊 Tabulares

<table>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile/">automobile</a></b></td>
  <td colspan="5">Especificaciones técnicas detalladas de vehículos junto con información sobre evaluación de riesgo de seguros y pérdidas normalizadas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile_simple/">automobile_simple</a></b></td>
  <td colspan="5">Versión simplificada del dataset Automobile con atributos seleccionados y variables derivadas para fines educativos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>186</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚖️ <a href="balance/">balance</a></b></td>
  <td colspan="5">Dataset basado en experimentos psicológicos sobre percepción del equilibrio.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>625</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚡ <a href="ccpp/">ccpp</a></b></td>
  <td colspan="5">Mediciones ambientales de una planta de ciclo combinado utilizadas para predecir producción eléctrica.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>9.568</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎨 <a href="colores_rgb_16/">colores_rgb_16</a></b></td>
  <td colspan="5">Colores definidos mediante componentes RGB clasificados en 16 categorías.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>1.200</td>
  <td><b>Clases</b><br>16</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💳 <a href="creditcard/">creditcard</a></b></td>
  <td colspan="5">Transacciones con tarjeta de crédito utilizadas para detección de fraude financiero.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>284.807</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💊 <a href="drugs/">drugs</a></b></td>
  <td colspan="5">Información médica utilizada para determinar la elección de medicamentos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>200</td>
  <td><b>Clases</b><br>5</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo<br><small>train (160) · test (40) · atípicos</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🫀 <a href="ecg5000/">ecg5000</a></b></td>
  <td colspan="5">Series temporales de electrocardiogramas utilizadas para clasificación de ritmos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>4.998</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="energy_efficiency/">energy_efficiency</a></b></td>
  <td colspan="5">Características edilicias utilizadas para estimar eficiencia energética.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>768</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>✋ <a href="fingers_features_train/">fingers_features</a></b></td>
  <td colspan="5">Características geométricas extraídas de imágenes de manos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>21.600</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><small>train (17.280) · test (4.320)</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍊 <a href="frutas_train/">frutas</a></b></td>
  <td colspan="5">Dataset sintético para clasificación de frutas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>20</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><small>train (16) · test (4)</small></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎈 <a href="globos/">globos</a></b></td>
  <td colspan="5">Adaptación del dataset Balloons utilizado para inducción de reglas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>16</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦅 <a href="hawks/">hawks</a></b></td>
  <td colspan="5">Mediciones morfológicas de tres especies de halcones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>893</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="housing/">housing</a></b></td>
  <td colspan="5">Datos habitacionales y demográficos para predicción del valor de viviendas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>20.640</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌸 <a href="iris/">iris</a></b></td>
  <td colspan="5">Mediciones morfológicas de tres especies de flores Iris.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>150</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>👓 <a href="lentes/">lentes</a></b></td>
  <td colspan="5">Dataset clásico para determinar uso de lentes de contacto.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>24</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚕️ <a href="obesity_uci/">obesity_uci</a></b></td>
  <td colspan="5">Estimación de niveles de obesidad mediante hábitos alimentarios y condición física.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>2.111</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏢 <a href="occupancy_detection/">occupancy_detection</a></b></td>
  <td colspan="5">Sensores ambientales para clasificación de ocupación de habitaciones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>9.752</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌾 <a href="semillas/">semillas</a></b></td>
  <td colspan="5">Mediciones geométricas de granos de trigo pertenecientes a tres variedades.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>210</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🔊 <a href="sonar/">sonar</a></b></td>
  <td colspan="5">Señales de sonar para distinguir rocas y minas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>208</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚢 <a href="titanic/">titanic</a></b></td>
  <td colspan="5">Información histórica de pasajeros del Titanic para predicción de supervivencia.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>891</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍷 <a href="wine/">wine</a></b></td>
  <td colspan="5">Análisis químico de vinos de tres cultivares italianos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>178</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦁 <a href="zoo/">zoo</a></b></td>
  <td colspan="5">Clasificación taxonómica de animales basada en características morfológicas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>101</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br>completo</td>
</tr>

</table>

---

## 📄 Licencia

La documentación y metadatos de este repositorio se distribuyen bajo licencia [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](LICENSE).

Cada dataset proviene de fuentes externas con sus propias condiciones de uso, detalladas en el `README.md` de cada carpeta. Se recomienda verificar la licencia original antes de usar los datos en publicaciones o proyectos comerciales.

---

*Última actualización: Julio 2026*  
*Mantenido por la comunidad RNA-UNIV para propósitos educativos y de investigación.*