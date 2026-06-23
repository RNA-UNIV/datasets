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

| Dataset | Descripción | Tarea | Variantes |
|---|---|---|---|
| [automobile](automobile/) | Especificaciones técnicas y riesgo de seguros de 205 vehículos (1985) | Regresión · Clasificación | completo · [simple](automobile_simple/) |
| [balance](balance/) | Equilibrio de una balanza según pesos y distancias | Clasificación | completo |
| [ccpp](ccpp/) | Predicción de potencia eléctrica en planta de ciclo combinado | Regresión | completo |
| [creditcard](creditcard/) | Detección de fraude en transacciones de tarjetas de crédito | Clasificación · Detección de anomalías | completo |
| [drugs](drugs/) | Clasificación de consumo de drogas según rasgos de personalidad | Clasificación | completo · [train](drugs_train/) · [test](drugs_test/) · [atípicos](drugs_atipicos/) |
| [housing](housing/) | Precios de viviendas en California (Census 1990) | Regresión | completo |
| [iris](iris/) | Clasificación de especies de flores Iris según medidas morfológicas | Clasificación | completo |
| [obesity_uci](obesity_uci/) | Niveles de obesidad según hábitos alimentarios y actividad física | Clasificación | completo |
| [occupancy_detection](occupancy_detection/) | Detección de ocupación de habitaciones por sensores ambientales | Clasificación | completo |
| [semillas](semillas/) | Clasificación de variedades de semillas de trigo por geometría | Clasificación | completo |
| [sonar](sonar/) | Clasificación de objetos (roca/mina) mediante señales sonar | Clasificación | completo |
| [titanic](titanic/) | Supervivencia de pasajeros del Titanic | Clasificación | completo |
| [wine](wine/) | Clasificación de vinos por análisis químico | Clasificación | completo |
| [zoo](zoo/) | Clasificación de animales según características físicas | Clasificación | completo |

### 🖼️ Imágenes

| Dataset | Descripción | Tarea | Variantes |
|---|---|---|---|
| [fingers](fingers/) | Imágenes de manos contando dedos (0–5) | Clasificación | completo · [train](fingers_train/) · [test](fingers_test/) |
| [frutas](frutas/) | Imágenes de frutas por categoría | Clasificación | [train](frutas_train/) · [test](frutas_test/) |
| [globos](globos/) | Imágenes de globos de colores | Clasificación | completo |
| [hawks](hawks/) | Fotografías de halcones de distintas especies | Clasificación | completo |
| [lentes](lentes/) | Imágenes de anteojos para clasificación o detección | Clasificación | completo |
| [natural_scenes](natural_scenes_train/) | Escenas naturales y urbanas en 6 categorías (Intel, 2018) | Clasificación | [train](natural_scenes_train/) · [test](natural_scenes_test/) |

---

## 📄 Licencia

La documentación y metadatos de este repositorio se distribuyen bajo licencia [**Creative Commons Attribution 4.0 International (CC BY 4.0)**](LICENSE).

Cada dataset proviene de fuentes externas con sus propias condiciones de uso, detalladas en el `README.md` de cada carpeta. Se recomienda verificar la licencia original antes de usar los datos en publicaciones o proyectos comerciales.

---

*Última actualización: Junio 2026*
*Mantenido por la comunidad RNA-UNIV para propósitos educativos y de investigación.*
