<p align="center">
<img src="banner.png" width="1000">
</p>

# 📊 Espectrogramas de Dataset Spoken Words: Common Voice 7.0

## 1. 📖 Descripción General
Este dataset contiene **espectrogramas** (imágenes en formato PNG y escala de grises, con una resolución de 65x64 píxeles) generados a partir de las grabaciones de audio del dataset **Spoken Words**, un subconjunto derivado de **Mozilla Common Voice 7.0** diseñado para tareas de reconocimiento de palabras aisladas (*Keyword Spotting*).
Este subconjunto está filtrado específicamente para el idioma español (es), lo que lo hace particularmente útil para aplicaciones en dispositivos de bajos recursos y entornos educativos.

Contiene imágenes correspondientes a una única palabra pronunciada por voluntarios. El vocabulario está compuesto por **14 clases**:
- Dígitos: `zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine`
- Comandos: `yes`, `no`, `hey`, `firefox`

Este tipo de dataset es ideal para clasificación de imágenes, visión artificial, TinyML y aprendizaje profundo.

## 2. 📊 Atributos y Significados

### 2.1 🎯 Variable Objetivo
**word**: palabra pronunciada (representada por el nombre de la carpeta de la clase).

### 2.2 🖼️ Espectrogramas
Cada instancia corresponde al espectrograma de un audio de una única palabra, representado como una imagen en escala de grises de 65x64 píxeles. La convención de nombres y la distribución se derivan directamente del dataset de audio original.

### 2.3 📁 Organización
Los archivos se organizan por clases en carpetas con el nombre de cada palabra objetivo (por ejemplo, `CERO/`, `UNO/`, `SI/`).

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria
El dataset deriva de **Mozilla Common Voice 7.0**, un proyecto abierto para la recopilación colaborativa de voz.

### 3.2 🏛️ Proyecto Original
Common Voice fue creado para proporcionar un corpus abierto de voz para investigación en reconocimiento automático del habla y procesamiento del lenguaje.
A partir del corpus completo, se extrajeron únicamente las grabaciones correspondientes a las 14 palabras objetivo, utilizando los metadatos de validación disponibles para garantizar que cada clip contiene efectivamente la palabra indicada.

## 4. 🔄 Proceso de Curaduría y Generación

### 4.1 Criterios de Selección de Audios
Las grabaciones fueron obtenidas mediante colaboración abierta de voluntarios. Cada clip ha sido validado por al menos dos miembros de la comunidad, quienes escuchan y confirman que el contenido corresponde a la palabra etiquetada.

Para este subconjunto, se aplicaron los siguientes criterios de calidad en el audio:
* Se descartaron grabaciones con etiquetas de validación negativa.
* Se estandarizó la frecuencia de muestreo a 22.050 Hz.

### 4.2 Conversión de Audio a Espectrograma (Imagen)
Los espectrogramas se generaron siguiendo estas etapas de procesamiento y conversión:

1. **Recorte de Silencios (Trimming)**:
   Se eliminaron los silencios/ruido de fondo al inicio y final del audio utilizando un umbral de energía (`top_db=15`, tamaño de trama de 256 y paso de 128 muestras).
2. **Ajuste Temporal (Time Stretching)**:
   Se estiró o comprimió el audio temporalmente para fijar la duración exacta de todas las muestras a **0,75 segundos** (sin alterar el tono o pitch).
3. **Espectrograma de Mel**:
   Se calculó el espectrograma Mel con los siguientes parámetros:
   - **Frecuencia de muestreo**: 22.050 Hz.
   - **Filtros Mel (Frecuencias)**: `64` bandas Mel (determina el alto de la imagen: 64 píxeles).
   - **Ventana FFT**: Tamaño de FFT de `512` muestras (`n_fft`).
   - **Desplazamiento (Hop Length)**: Paso de `256` muestras (determina el ancho de la imagen: 65 píxeles, dado que \(0,75 \text{ s} \times 22.050 \text{ Hz} / 256 \approx 65\) tramas).
4. **Escala Logarítmica y Normalización**:
   Se aplicó la escala logarítmica de decibelios (\(10 \times \log(\text{mel} + 10^{-9})\)) y una normalización Min-Max para mapear los valores al rango `[0, 1]`.
5. **Conversión a Imagen de 8 bits**:
   - Los valores normalizados se escalaron al rango `[0, 255]`.
   - Se invirtió verticalmente el espectrograma para posicionar las bajas frecuencias en la parte inferior de la imagen.
   - Se invirtieron los colores (inversión de bits: `255 - valor`) para que las zonas con mayor energía/intensidad acústica se representen en tonos oscuros (negros) y el silencio o baja energía en tonos claros (blanco).

## 5. 🎯 Valor Analítico

Este dataset resulta adecuado para:

- Clasificación de imágenes (espectrogramas)
- Keyword Spotting (mediante aproximación visual/CNN)
- TinyML
- Redes neuronales convolucionales (CNN)
- Visión por computadora aplicada al habla
- Sistemas embebidos

## 6. 📈 Estadísticas del Dataset

### 6.1 General y Técnica

| Métrica | Valor |
|---------|-------|
| Total de imágenes | 16.631 |
| Train | 10.282 |
| Test | 6.349 |
| Número de clases | 14 |
| Tamaño total | 49,25 MB (descomprimido) |
| Resolución | 65x64 |
| Canales | 1 (escala de grises) |

### 6.2 Duración General (del Audio Original)

| Estadístico | Valor |
|-------------|-------|
| Media | 2,743 s |
| Mediana | 2,544 s |
| Mínima | 1,080 s |
| Máxima | 11,328 s |
| Total horas | 12,67 h |

### 6.3 Distribución por Género

| Género | Cantidad | Porcentaje |
|--------|----------|------------|
| Desconocido | 11.640 | 69,99 % |
| Masculino | 3.337 | 20,06 % |
| Femenino | 1.654 | 9,95 % |

### 6.4 Distribución por Clase

| Clase | Train | Test | Total | % |
|-------|------:|-----:|------:|---:|
| CERO | 726 | 412 | 1.138 | 6,84 |
| CINCO | 744 | 432 | 1.176 | 7,07 |
| CUATRO | 743 | 485 | 1.228 | 7,38 |
| DOS | 743 | 462 | 1.205 | 7,25 |
| FIREFOX | 631 | 325 | 956 | 5,75 |
| HEY | 693 | 385 | 1.078 | 6,48 |
| NO | 751 | 501 | 1.252 | 7,53 |
| NUEVE | 730 | 463 | 1.193 | 7,17 |
| OCHO | 758 | 457 | 1.215 | 7,31 |
| SEIS | 743 | 472 | 1.215 | 7,31 |
| SI | 768 | 463 | 1.231 | 7,40 |
| SIETE | 753 | 520 | 1.273 | 7,65 |
| TRES | 750 | 485 | 1.235 | 7,43 |
| UNO | 749 | 487 | 1.236 | 7,43 |

### 6.5 Duración por Clase

La duración media por clase se mantiene en un rango estrecho, entre **2,597 s** (para "NO") y **2,887 s** (para "FIREFOX"), con una desviación estándar aproximada de 0,1 s entre clases. Esto indica una distribución homogénea en cuanto a longitud de las grabaciones, sin que ninguna palabra presente duraciones significativamente atípicas.

Los valores mínimos se sitúan alrededor de 1,1 s, mientras que los máximos alcanzan hasta 11,3 s en casos puntuales, probablemente debidos a hablantes con ritmos de habla más lentos o pausas prolongadas.

## 7. 📝 Consideraciones Éticas

Las grabaciones fueron aportadas voluntariamente por los participantes del proyecto Common Voice, quienes otorgaron su consentimiento explícito para el uso público de sus voces.

Aunque las imágenes no contienen información personal asociada, se derivan de la voz, que es un dato biométrico. Se recomienda a los investigadores y desarrolladores:

* No intentar reidentificar a los hablantes.
* Utilizar el dataset exclusivamente para los fines descritos en esta documentación. 
* Respetar los términos de la licencia CC0, atribuyendo correctamente la fuente original.

Mozilla Foundation garantiza que no se almacenan datos sensibles vinculados a los clips.

## 8. 🔗 Acceso y Uso

Ejemplo para cargar el dataset local de imágenes en Python:

Acceso con el DataLoader de la biblioteca `rna` (Recomendado):
```python
# Instalar la biblioteca si no está disponible:
# !pip install https://github.com/RNA-UNIV/rna/archive/refs/heads/main.zip

from rna.data.ClassDataLoader import DataLoader

# Cargar imágenes y etiquetas en memoria
X, y, clases, _ = DataLoader.load_images('common_voice_spectrum_train', resize=(65, 64))
```

```python
import os
import numpy as np
from PIL import Image

def load_spectrogram_dataset(data_dir):
    images = []
    labels = []
    
    for class_name in os.listdir(data_dir):
        class_dir = os.path.join(data_dir, class_name)
        if os.path.isdir(class_dir):
            for filename in os.listdir(class_dir):
                if filename.endswith('.png'):
                    img_path = os.path.join(class_dir, filename)
                    img = Image.open(img_path)
                    img_array = np.array(img)
                    images.append(img_array)
                    labels.append(class_name)
                    
    return np.array(images), np.array(labels)

# Cargar imágenes de test o train
X_train, y_train = load_spectrogram_dataset('datasets/common_voice_spectrum_train/')
print(f"Espectrogramas cargados: {X_train.shape}")
```

## 9. 🔖 Cita Recomendada

> Ardila, R., Branson, M., Davis, K., Henretty, M., Kohler, M., Meyer, J., ... & Tyers, F. (2020). Common Voice: A Massively-Multilingual Speech Corpus. Proceedings of the 12th Language Resources and Evaluation Conference (LREC 2020), pp. 4211-4215.
> Disponible en: https://aclanthology.org/2020.lrec-1.520/
---
*Última actualización: Julio 2026*

*Mantenido por la comunidad de ciencia de datos para propósitos educativos y de investigación.*
