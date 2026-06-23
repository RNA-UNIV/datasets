<p align="center">
<img src="banner.png" width="1000">
</p>

# 📦 RNA-UNIV — Repositorio de Datasets

Colección de datasets para prácticas y proyectos de machine learning, mantenida por la comunidad **RNA-UNIV**. Está diseñada para ser usada en conjunto con el **DataLoader** de [EmbedIA](https://github.com/RNA-UNIV/embedia), que permite descargar y cargar cualquier dataset con pocas líneas de código.

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
from embedia.data import DataLoader

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

| Dataset | Descripción | Tarea | Muestras | Clases | Faltantes | Variantes |
|---|---|---|---|---|---|---|

| 🚗 [automobile](automobile/) | Especificaciones técnicas detalladas de 205 vehículos de diferentes marcas y modelos, junto con información sobre su evaluación de riesgo de seguros y pérdidas normalizadas. | Clasificación · Regresión · Agrupamiento | 205 | 6 | ✅ | [completo](automobile/) · [simple](automobile_simple/) |
| ⚖️ [balance](balance/) | El conjunto de datos de Balance Scale fue creado para modelar los resultados de experimentos psicológicos que estudian la percepción del equilibrio. | Clasificación | 625 | 3 | — | [completo](balance/) |
| ⚡ [ccpp](ccpp/) | Dataset de mediciones ambientales horarias recolectadas durante 6 años en una planta de ciclo combinado operando a plena carga, utilizado para predecir la producción neta de energía eléctrica. | Regresión | 9.568 | — | — | [completo](ccpp/) |
| 💳 [creditcard](creditcard/) | Dataset de transacciones con tarjeta de crédito realizadas por tarjetahabientes europeos en septiembre de 2013. Altamente desbalanceado (0.172% fraudes), con atributos anonimizados mediante PCA. Utilizado para detección de fraude financiero. | Clasificación · Regresión | 284.807 | 2 | — | [completo](creditcard/) |
| 💊 [drugs](drugs/) | Contiene información detallada sobre variables médicas que influyen en la elección de un medicamento específico. | Clasificación · Regresión | 200 | 5 | — | [completo](drugs/) · [train](drugs_train/) · [test](drugs_test/) · [atípicos](drugs_atipicos/) |
| 🍊 [frutas](frutas_test/) | Conjunto de prueba sintético para clasificar frutas (naranja o melón) basado en diámetro y color. | Clasificación · Regresión | 4 | 2 | — | [train](frutas_train/) · [test](frutas_test/) |
| 🎈 [globos](globos/) | Adaptación en español del dataset clásico Balloons de la UCI, utilizado para la inducción de reglas sobre si un globo se infla o no. | Clasificación | 16 | 2 | — | [completo](globos/) |
| 🦅 [hawks](hawks/) | Medidas morfológicas de tres especies de halcones (cola roja, alas anchas y cola lineada) registradas en estudios de campo. | Clasificación | 893 | — | — | [completo](hawks/) |
| 🏠 [housing](housing/) | Dataset derivado del Censo de California de 1990 donde cada instancia representa un bloque censal. Contiene atributos demográficos, habitacionales y geográficos para predecir el valor mediano de las viviendas. | Regresión | 20.640 | — | ✅ | [completo](housing/) |
| 🌸 [iris](iris/) | Dataset botánico clásico de Ronald Fisher que contiene mediciones morfológicas de tres especies de flores Iris. | Clasificación · Agrupamiento | 150 | 3 | — | [completo](iris/) |
| 👓 [lentes](lentes/) | Dataset clásico para determinar si un paciente debe usar lentes de contacto duros, blandos o ninguno. | Clasificación | 24 | 3 | — | [completo](lentes/) |
| ⚕️ [obesity_uci](obesity_uci/) | Estimación de niveles de obesidad basados en hábitos alimentarios y condición física de personas de México, Perú y Colombia. | Clasificación · Regresión · Agrupamiento | 2.111 | 7 | — | [completo](obesity_uci/) |
| 🏢 [occupancy_detection](occupancy_detection/) | Datos experimentales para clasificación binaria de ocupación de habitaciones. Las mediciones provienen de sensores de temperatura, humedad, luz y CO2, con etiquetas de ocupación obtenidas de fotografías con marca de tiempo tomadas cada minuto. | Clasificación | 9.752 | 2 | — | [completo](occupancy_detection/) |
| 🌾 [semillas](semillas/) | Mediciones geométricas de granos de trigo pertenecientes a tres variedades distintas (Kama, Rosa y Canadian) obtenidas mediante rayos X. | Clasificación · Agrupamiento | 210 | 3 | — | [completo](semillas/) |
| 🔊 [sonar](sonar/) | Este conjunto de datos se utiliza para la clasificación de señales de sonar que rebotan en diferentes objetos. El objetivo es distinguir entre señales rebotadas en una mina (metal) y señales rebotadas en una roca. Los datos son ideales para la evaluación de algoritmos de clasificación en problemas de detección y reconocimiento de patrones. | Clasificación | 208 | 2 | — | [completo](sonar/) |
| 🚢 [titanic](titanic/) | Datos históricos de pasajeros del RMS Titanic para predecir la supervivencia basada en variables demográficas y de viaje. | Clasificación | 891 | 2 | ✅ | [completo](titanic/) |
| 🍷 [wine](wine/) | Dataset de análisis químicos de vinos producidos en la región del Piamonte, Italia, derivados de tres cultivares distintos. Utilizado para clasificación multiclase mediante 13 atributos quimiométricos. | Clasificación | 178 | 3 | — | [completo](wine/) |
| 🦁 [zoo](zoo/) | Clasificación taxonómica de animales basada en características morfológicas, fisiológicas y comportamentales. | Clasificación · Agrupamiento | 101 | 7 | — | [completo](zoo/) |

### 🖼️ Imágenes

| Dataset | Descripción | Tarea | Muestras | Clases | Variantes |
|---|---|---|---|---|---|

| ✋ [fingers](fingers/) | Imágenes en escala de grises de manos mostrando de 0 a 5 dedos, etiquetadas con el número de dedos y orientación (izquierda/derecha). | Clasificación | 21.600 | 6 | [completo](fingers/) · [train](fingers_train/) · [test](fingers_test/) |
| 🏔️ [natural_scenes](natural_scenes_test/) | Imágenes de escenas naturales y urbanas organizadas en 6 categorías, destinadas a la evaluación de modelos de clasificación. Subconjunto del Intel Scene Classification Challenge (2018). | Clasificación | 3.000 | 6 | [train](natural_scenes_train/) · [test](natural_scenes_test/) |

---

## 📄 Licencia

La documentación y metadatos de este repositorio se distribuyen bajo licencia [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](LICENSE).

Cada dataset proviene de fuentes externas con sus propias condiciones de uso, detalladas en el `README.md` de cada carpeta. Se recomienda verificar la licencia original antes de usar los datos en publicaciones o proyectos comerciales.

---

*Última actualización: June 2026*  
*Mantenido por la comunidad RNA-UNIV para propósitos educativos y de investigación.*
