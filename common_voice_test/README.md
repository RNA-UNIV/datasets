<p align="center">
<img src="banner.png" width="1000">
</p>

# 🎤 Dataset Spoken Words: Common Voice 7.0

## 1. 📖 Descripción General
El dataset **Spoken Words** es un subconjunto derivado de **Mozilla Common Voice 7.0**, diseñado para tareas de reconocimiento de palabras aisladas (*Keyword Spotting*).
Este subconjunto está filtrado específicamente para el idioma español (es), lo que lo hace particularmente útil para aplicaciones en dispositivos de bajos recursos y entornos educativos.

Contiene grabaciones de una única palabra pronunciada por voluntarios. El vocabulario está compuesto por **14 clases**:
- Dígitos: `zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, `nine`
- Comandos: `yes`, `no`, `hey`, `firefox`

Este tipo de dataset es ideal para clasificación de audio, TinyML y aprendizaje profundo.

## 2. 📊 Atributos y Significados

### 2.1 🎯 Variable Objetivo
**word**: palabra pronunciada.

### 2.2 🎧 Audio
Cada instancia corresponde a una grabación de una única palabra. Dependiendo de la distribución pueden existir metadatos como identificador del hablante, idioma, sexo, edad y estado de validación.

### 2.3 📁 Organización
Habitualmente los archivos se organizan por clases o mediante un archivo de metadatos que relaciona cada audio con su etiqueta.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria
El dataset deriva de **Mozilla Common Voice 7.0**, un proyecto abierto para la recopilación colaborativa de voz.

### 3.2 🏛️ Proyecto Original
Common Voice fue creado para proporcionar un corpus abierto de voz para investigación en reconocimiento automático del habla y procesamiento del lenguaje.
A partir del corpus completo, se extrajeron únicamente las grabaciones correspondientes a las 14 palabras objetivo, utilizando los metadatos de validación disponibles para garantizar que cada clip contiene efectivamente la palabra indicada.
## 4. 🔄 Proceso de Curaduría

Las grabaciones fueron obtenidas mediante colaboración abierta de voluntarios. Cada clip ha sido validado por al menos dos miembros de la comunidad, quienes escuchan y confirman que el contenido corresponde a la palabra etiquetada.

Para este subconjunto, se aplicaron los siguientes criterios de calidad:

* Se descartaron grabaciones con etiquetas de validación negativa.
* Se estandarizó la frecuencia de muestreo a 22.050 Hz.
* No se aplicó recorte de silencios ni normalización de amplitud para preservar las condiciones originales de grabación.

El resultado es un conjunto balanceado y confiable para tareas de clasificación supervisada.
## 5. 🎯 Valor Analítico

Este dataset resulta adecuado para:

- Keyword Spotting
- Reconocimiento automático del habla
- Clasificación de audio
- TinyML
- Redes neuronales convolucionales
- MFCC, STFT y Mel Spectrogram
- Sistemas embebidos

## 6. 📈 Estadísticas del Dataset

### 6.1 General y Técnica

| Métrica | Valor |
|---------|-------|
| Total de audios | 16.631 |
| Train | 10.282 |
| Test | 6.349 |
| Número de clases | 14 |
| Tamaño total | 256,88 MB |
| Sample rate | 22.050 Hz |
| Canales | 1 (mono) |

### 6.2 Duración General

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

Aunque los audios no contienen información personal asociada (como nombre, correo electrónico o ubicación), la voz es un dato biométrico. Se recomienda a los investigadores y desarrolladores:

* No intentar reidentificar a los hablantes.
* Utilizar el dataset exclusivamente para los fines descritos en esta documentación. 
* Respetar los términos de la licencia CC0, atribuyendo correctamente la fuente original.

Mozilla Foundation garantiza que no se almacenan datos sensibles vinculados a los clips.

## 8. 🔗 Acceso y Uso

Ejemplo de carga:

```python
from datasets import load_dataset

dataset = load_dataset("mozilla-foundation/common_voice_7_0", "en")
print(dataset)
```

Ejemplo para cargar un archivo local:

```python
import librosa

audio, sr = librosa.load("audio.wav", sr=16000)
```

## 9. 🔖 Cita Recomendada

> Ardila, R., Branson, M., Davis, K., Henretty, M., Kohler, M., Meyer, J., ... & Tyers, F. (2020). Common Voice: A Massively-Multilingual Speech Corpus. Proceedings of the 12th Language Resources and Evaluation Conference (LREC 2020), pp. 4211-4215.
Disponible en: https://aclanthology.org/2020.lrec-1.520/
---
*Última actualización: Junio 2026*

*Mantenido por la comunidad de ciencia de datos para propósitos educativos y de investigación.*
