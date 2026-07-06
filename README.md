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
  <td colspan="5">Especificaciones técnicas detalladas de 205 vehículos de diferentes marcas y modelos, junto con información sobre su evaluación de riesgo de seguros y pérdidas normalizadas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br><a href="automobile/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚗 <a href="automobile_simple/">automobile_simple</a></b></td>
  <td colspan="5">Versión simplificada del dataset de automóviles con un subconjunto de atributos originales y variables derivadas (volumen, eco-rating), adaptada con fines educativos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>205</td>
  <td><b>Clases</b><br>186</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br><a href="automobile_simple/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚖️ <a href="balance/">balance</a></b></td>
  <td colspan="5">El conjunto de datos de Balance Scale fue creado para modelar los resultados de experimentos psicológicos que estudian la percepción del equilibrio.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>625</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="balance/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚡ <a href="ccpp/">ccpp</a></b></td>
  <td colspan="5">Dataset de mediciones ambientales horarias recolectadas durante 6 años en una planta de ciclo combinado operando a plena carga, utilizado para predecir la producción neta de energía eléctrica.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>9.568</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="ccpp/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💳 <a href="creditcard/">creditcard</a></b></td>
  <td colspan="5">Dataset de transacciones con tarjeta de crédito realizadas por tarjetahabientes europeos en septiembre de 2013. Altamente desbalanceado (0.172% fraudes), con atributos anonimizados mediante PCA. Utilizado para detección de fraude financiero.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>284.807</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="creditcard/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>💊 <a href="drugs/">drugs</a></b></td>
  <td colspan="5">Contiene información detallada sobre variables médicas que influyen en la elección de un medicamento específico.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>200</td>
  <td><b>Clases</b><br>5</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="drugs/">completo</a> · <a href="drugs_train/">train</a> · <a href="drugs_test/">test</a> · <a href="drugs_atipicos/">atípicos</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🫀 <a href="ecg5000/">ecg5000</a></b></td>
  <td colspan="5">Series temporales de latidos cardíacos (140 puntos de amplitud) extraídas de un electrocardiograma continuo de un paciente, utilizado para clasificación de ritmos y detección de anomalías.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>4.998</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="ecg5000/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍊 <a href="frutas_test/">frutas</a></b></td>
  <td colspan="5">Conjunto de prueba sintético para clasificar frutas (naranja o melón) basado en diámetro y color.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión</td>
  <td><b>Muestras</b><br>4</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="frutas_train/">train</a> · <a href="frutas_test/">test</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎈 <a href="globos/">globos</a></b></td>
  <td colspan="5">Adaptación en español del dataset clásico Balloons de la UCI, utilizado para la inducción de reglas sobre si un globo se infla o no.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>16</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="globos/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦅 <a href="hawks/">hawks</a></b></td>
  <td colspan="5">Medidas morfológicas de tres especies de halcones (cola roja, alas anchas y cola lineada) registradas en estudios de campo.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>893</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="hawks/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏠 <a href="housing/">housing</a></b></td>
  <td colspan="5">Dataset derivado del Censo de California de 1990 donde cada instancia representa un bloque censal. Contiene atributos demográficos, habitacionales y geográficos para predecir el valor mediano de las viviendas.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Regresión</td>
  <td><b>Muestras</b><br>20.640</td>
  <td><b>Clases</b><br>—</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br><a href="housing/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌸 <a href="iris/">iris</a></b></td>
  <td colspan="5">Dataset botánico clásico de Ronald Fisher que contiene mediciones morfológicas de tres especies de flores Iris.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>150</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="iris/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>👓 <a href="lentes/">lentes</a></b></td>
  <td colspan="5">Dataset clásico para determinar si un paciente debe usar lentes de contacto duros, blandos o ninguno.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>24</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="lentes/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>⚕️ <a href="obesity_uci/">obesity_uci</a></b></td>
  <td colspan="5">Estimación de niveles de obesidad basados en hábitos alimentarios y condición física de personas de México, Perú y Colombia.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Regresión · Agrupamiento</td>
  <td><b>Muestras</b><br>2.111</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="obesity_uci/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏢 <a href="occupancy_detection/">occupancy_detection</a></b></td>
  <td colspan="5">Datos experimentales para clasificación binaria de ocupación de habitaciones. Las mediciones provienen de sensores de temperatura, humedad, luz y CO2, con etiquetas de ocupación obtenidas de fotografías con marca de tiempo tomadas cada minuto.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>9.752</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="occupancy_detection/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌾 <a href="semillas/">semillas</a></b></td>
  <td colspan="5">Mediciones geométricas de granos de trigo pertenecientes a tres variedades distintas (Kama, Rosa y Canadian) obtenidas mediante rayos X.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>210</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="semillas/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🔊 <a href="sonar/">sonar</a></b></td>
  <td colspan="5">Este conjunto de datos se utiliza para la clasificación de señales de sonar que rebotan en diferentes objetos. El objetivo es distinguir entre señales rebotadas en una mina (metal) y señales rebotadas en una roca. Los datos son ideales para la evaluación de algoritmos de clasificación en problemas de detección y reconocimiento de patrones.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>208</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="sonar/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🚢 <a href="titanic/">titanic</a></b></td>
  <td colspan="5">Datos históricos de pasajeros del RMS Titanic para predecir la supervivencia basada en variables demográficas y de viaje.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>891</td>
  <td><b>Clases</b><br>2</td>
  <td><b>Faltantes</b><br>✅</td>
  <td><b>Variantes</b><br><a href="titanic/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🍷 <a href="wine/">wine</a></b></td>
  <td colspan="5">Dataset de análisis químicos de vinos producidos en la región del Piamonte, Italia, derivados de tres cultivares distintos. Utilizado para clasificación multiclase mediante 13 atributos quimiométricos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>178</td>
  <td><b>Clases</b><br>3</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="wine/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🦁 <a href="zoo/">zoo</a></b></td>
  <td colspan="5">Clasificación taxonómica de animales basada en características morfológicas, fisiológicas y comportamentales.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación · Agrupamiento</td>
  <td><b>Muestras</b><br>101</td>
  <td><b>Clases</b><br>7</td>
  <td><b>Faltantes</b><br>—</td>
  <td><b>Variantes</b><br><a href="zoo/">completo</a></td>
</tr>

</table>

### 🖼️ Imágenes

<table>

<tr>
  <td rowspan="2" width="140" valign="top"><b>✋ <a href="fingers/">fingers</a></b></td>
  <td colspan="4">Imágenes en escala de grises de manos mostrando de 0 a 5 dedos, etiquetadas con el número de dedos y orientación (izquierda/derecha).</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>21.600</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Variantes</b><br><a href="fingers/">completo</a> · <a href="fingers_train/">train</a> · <a href="fingers_test/">test</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🌻 <a href="flowers16/">flowers16</a></b></td>
  <td colspan="4">Imágenes de flores de 256x256 píxeles pertenecientes a 16 especies distintas. Recuperado mediante un mirror del dataset original de Kaggle y curado para unificar la resolución y calidad de todas las clases.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>15.648</td>
  <td><b>Clases</b><br>16</td>
  <td><b>Variantes</b><br><a href="flowers16/">completo</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🏔️ <a href="natural_scenes_test/">natural_scenes</a></b></td>
  <td colspan="4">Imágenes de escenas naturales y urbanas organizadas en 6 categorías, destinadas a la evaluación de modelos de clasificación. Subconjunto del Intel Scene Classification Challenge (2018).</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>3.000</td>
  <td><b>Clases</b><br>6</td>
  <td><b>Variantes</b><br><a href="natural_scenes_train/">train</a> · <a href="natural_scenes_test/">test</a></td>
</tr>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🎵 <a href="common_voice_spectrum_test/">common_voice_spectrum</a></b></td>
  <td colspan="4">Espectrogramas de audio en formato de imagen PNG y escala de grises, generados a partir de Mozilla Common Voice 7.0. Diseñado para reconocimiento de palabras aisladas (Keyword Spotting) con un vocabulario de 14 clases entre dígitos y comandos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>16.631</td>
  <td><b>Clases</b><br>14</td>
  <td><b>Variantes</b><br><a href="common_voice_spectrum_train/">train</a> · <a href="common_voice_spectrum_test/">test</a></td>
</tr>

</table>

### 🔊 Audio

<table>

<tr>
  <td rowspan="2" width="140" valign="top"><b>🗣️ <a href="common_voice_test/">common_voice</a></b></td>
  <td colspan="4">Subconjunto derivado de Mozilla Common Voice 7.0 diseñado para tareas de reconocimiento de palabras aisladas (Keyword Spotting). Contiene grabaciones de una única palabra pronunciada por voluntarios, con un vocabulario de 14 clases entre dígitos y comandos.</td>
</tr>
<tr>
  <td><b>Tarea</b><br>Clasificación</td>
  <td><b>Muestras</b><br>16.631</td>
  <td><b>Clases</b><br>14</td>
  <td><b>Variantes</b><br><a href="common_voice_train/">train</a> · <a href="common_voice_test/">test</a></td>
</tr>

</table>

---

## 📄 Licencia

La documentación y metadatos de este repositorio se distribuyen bajo licencia [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](LICENSE).

Cada dataset proviene de fuentes externas con sus propias condiciones de uso, detalladas en el `README.md` de cada carpeta. Se recomienda verificar la licencia original antes de usar los datos en publicaciones o proyectos comerciales.

---

*Última actualización: Julio 2026*  
*Mantenido por la comunidad RNA-UNIV para propósitos educativos y de investigación.*