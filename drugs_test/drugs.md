# 🩺 Dataset Clasificación de Fármacos: Predicción de Tipos de Medicamentos
## 1. 📖 Descripción General
El conjunto de datos de Clasificación de Fármacos es una herramienta valiosa para principiantes en aprendizaje automático que desean explorar modelos de clasificación basados en características clínicas del paciente. Este dataset contiene información detallada sobre variables médicas que influyen en la elección de un medicamento específico, permitiendo desarrollar modelos predictivos para determinar qué fármaco podría ser más efectivo para un paciente según su perfil fisiológico.
Los datos reflejan relaciones clínicas clave entre factores como la presión arterial, el colesterol y la relación sodio-potasio, lo que lo convierte en un recurso ideal para ejercicios de clasificación multiclase en contextos educativos y de investigación biomédica.
La versión utilizada en este análisis se basa en el dataset original disponible en Kaggle, estructurado y documentado con claridad.

## 2. 📊 Atributos y Significados   

### 2.1 💊 Variable Objetivo
**Drug**: Categoría del medicamento recetado según el perfil del paciente.
 - `drugY`: Fármaco tipo Y (eficaz en pacientes con alta relación Na/K)
 - `drugX`: Fármaco tipo X (uso común en niveles normales de presión y electrolitos)
 - `drugA`, `drugB`, `drugC`: Fármacos específicos con diferentes mecanismos de acción y criterios de prescripción

### 2.2 📏 Atributos Clínicos
**Age**: Edad del paciente al momento de la evaluación (en años).
**Sex**: Sexo del paciente.
 - `M`: Masculino
 - `F`: Femenino

**BP** (Presión Arterial): Nivel de presión arterial del paciente.
 - `HIGH`: Alta
 - `LOW`: Baja
 - `NORMAL`: Normal
 - 
**Cholesterol**: Nivel de colesterol en sangre.
 - `HIGH`: Alto
 - `NORMAL`: Normal

**Na_to_K**: Relación entre sodio y potasio en sangre (proporción adimensional). Indicador clave del equilibrio electrolítico y predictor importante en la selección del fármaco.
**Nota importante**: en este dataset este atributo está separado en los valores `NA` (sodio) y `K` (potacio).

### 2.3 🏷️ Notas sobre los Atributos   

 - Todas las mediciones son numéricas o categóricas, con valores bien definidos.  
 - El atributo Tipo de Fármaco es categórico y sirve como variable objetivo en tareas de clasificación supervisada.  
 - La Relación Na/K es una variable continua que muestra una fuerte correlación con el tipo de fármaco prescrito, especialmente para DrugY.  
 - No se reportan valores nulos en el archivo drug200.csv, lo que lo hace ideal para análisis iniciales sin necesidad de imputación.


## 3. 🏢 Origen y Procedencia   

### 3.1 📚 Fuente Primaria: Kaggle
El dataset fue obtenido de la plataforma Kaggle, un repositorio ampliamente utilizado para datos científicos y de aprendizaje automático.
> **URL Oficial**:
👉 https://www.kaggle.com/datasets/prathamtripathi/drug-classification
>
> **Nombre del archivo**: 
>  - Kaggle: drug200.csv   
>  - Repositorio: drugs.csv

### 3.2 🏛️ Fuente Original y Contexto Científico
Aunque no se especifica una fuente clínica directa, el conjunto de datos parece estar diseñado para simular un escenario realista de toma de decisiones médicas basadas en parámetros fisiológicos. Podría estar inspirado en estudios clínicos sobre hipertensión, metabolismo electrolítico o farmacocinética. Su estructura simple y clara lo hace adecuado para fines educativos y de entrenamiento en ciencia de datos aplicada a la salud.


## 4. 🔄 Proceso de Curaduría
La versión documentada ha sido adaptada mediante:   

 - Organización del contenido siguiendo el formato del dataset de halcones (hawks.md)  
 - Documentación clara de unidades, rangos y significado clínico  
 - Eliminación de contenido duplicado o redundante presente en la página original
     


## 5. 🎯 Valor Analítico
Este dataset ofrece múltiples oportunidades para el aprendizaje y análisis:   

 - Clasificación multiclase de tipos de fármacos  
 - Análisis de decisiones médicas basadas en reglas (ej. árboles de decisión)  
 - Visualización de relaciones entre variables (e.g., Edad vs. Relación Na/K)  
 - Preprocesamiento de variables categóricas (one-hot encoding, label encoding)  
 - Evaluación de modelos de clasificación (regresión logística, SVM, random forest)  
 - Interpretación clínica de patrones predictivos  
 - Contexto realista con aplicaciones en medicina personalizada y salud digital


## 6. 📝 Consideraciones Éticas
Los datos son sintéticos o anonimizados y no representan información médica real de pacientes identificables. Su uso está orientado exclusivamente a la educación y la investigación. Se debe evitar hacer inferencias clínicas reales sin validación médica adicional. El modelo predictivo derivado de este dataset no debe usarse en entornos clínicos sin supervisión profesional.   
 

## 7. 🔗 Acceso y Uso
El dataset está disponible bajo licencia CC0: Dominio Público, lo que permite su uso libre para fines educativos, de investigación y comerciales sin restricciones.   

### 7.1 📥 Cómo cargarlo en Python:   

Acceso vía GitHub:
```python
import pandas as pd

# URL del archivo en Kaggle o repositorio
url = "https://raw.githubusercontent.com/aap-unlp/datasets/main/drugs/drugs.csv"
drugs_ds = pd.read_csv(url)

# Separar características y etiquetas
X = drugs_ds.drop(columns=['Drug'])
y = drugs_ds['Drug']

# Información del dataset
print("Columnas:", drugs_ds.columns.tolist())
print("Primeras filas:\n", drugs_ds.head())
```

## 8. 🔖 Cita Recomendada:
> Pratham Tripathi. (2023). Drug Classification Dataset. Kaggle.
https://www.kaggle.com/datasets/prathamtripathi/drug-classification    

---

*Última actualización: Abril 2024
Mantenido por la comunidad de ciencia de datos para propósitos educativos.*