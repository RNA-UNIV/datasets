<p align="center">
<img src="banner.png" width="1000">
</p>

# 💳 Dataset Credit Card Fraud Detection: Clasificación de Transacciones Fraudulentas

## 1. 📖 Descripción General

El **Credit Card Fraud Detection Dataset** es uno de los conjuntos de datos más utilizados en el ámbito del aprendizaje automático para problemas de **detección de anomalías y clasificación binaria desbalanceada**. Fue recopilado y publicado por el **Machine Learning Group de la Université Libre de Bruxelles (ULB)**, y está disponible públicamente en Kaggle desde 2018. Ha sido ampliamente adoptado como benchmark de referencia para evaluar algoritmos de detección de fraude financiero.

El dataset contiene transacciones realizadas con tarjetas de crédito por **tarjetahabientes europeos** durante **dos días de septiembre de 2013**. El objetivo es clasificar cada transacción como:

- **Legítima (0)**
- **Fraudulenta (1)**

Lo que hace a este dataset tan relevante y desafiante es su **extremo desbalance de clases**: de 284,807 transacciones totales, solo 492 son fraudulentas, representando apenas el **0.172% del total**. Esta característica lo convierte en el recurso ideal para estudiar técnicas de manejo de desbalance (SMOTE, undersampling, class weighting) y métricas de evaluación apropiadas (AUC-ROC, F1, precisión-recall), donde la exactitud (*accuracy*) resulta una métrica engañosa.

Por razones de confidencialidad, la mayoría de los atributos originales han sido anonimizados mediante una transformación **PCA (Análisis de Componentes Principales)**, por lo que no se dispone de información semántica sobre las variables transformadas.

## 2. 📊 Atributos y Significados

### 2.1 🔑 Variable Objetivo

**Class (Clase)**: Clasificación de la transacción.
- `0` — Transacción legítima (284,315 instancias — 99.828%)
- `1` — Transacción fraudulenta (492 instancias — 0.172%)

### 2.2 📏 Atributos de Medición

**Time (Tiempo)**: Segundos transcurridos entre la transacción y la primera transacción del dataset.
- Rango observado: 0 – 172,792 segundos
- *Valor numérico continuo. Permite analizar patrones temporales de fraude.*

**Amount (Monto)**: Monto de la transacción en euros.
- *Valor numérico continuo. Puede utilizarse para cost-sensitive learning.*

**V1 – V28**: Componentes principales obtenidas mediante PCA sobre los atributos originales (anonimizados por confidencialidad).
- *28 valores numéricos continuos.*
- *Son las únicas features transformadas con PCA; no tienen interpretación semántica directa.*
- *Capturan la mayor parte de la varianza de las características originales de las transacciones.*

> ⚠️ **Nota**: Due to confidentiality constraints, the original features and background information about the data cannot be provided. Only `Time` and `Amount` retain their original meaning.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: Kaggle / MLG-ULB

El dataset fue publicado por el Machine Learning Group de la Université Libre de Bruxelles y se encuentra disponible en Kaggle bajo la Open Database License (ODbL).

> **URL Oficial**: 👉 `https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud`
>
> **Nombre del archivo**: `creditcard.csv`

### 3.2 📜 Contexto Histórico

Los datos fueron recolectados como parte de la investigación doctoral de **Andrea Dal Pozzolo** (supervisada por Gianluca Bontempi) sobre aprendizaje automático adaptativo para detección de fraude. El grupo MLG-ULB ha producido múltiples publicaciones relevantes utilizando este dataset como base experimental, contribuyendo al desarrollo de métodos de detección en streaming y aprendizaje activo para sistemas de fraude en tiempo real.

## 4. 🔁 Proceso de Curaduría

El dataset ha sido meticulosamente curado y verificado:

- 284,807 instancias totales (2 días de transacciones, septiembre 2013)
- Sin valores faltantes
- Variables V1–V28 transformadas mediante PCA (datos originales anonimizados)
- Solo `Time` y `Amount` conservan su significado original
- Desbalance de clases extremo: 492 fraudes (0.172%) vs 284,315 legítimas (99.828%)
- Disponible en un único archivo CSV (~150 MB)

## 5. 🎯 Valor Analítico

Este dataset ofrece un entorno analítico exigente y muy aplicado para:

- **Clasificación binaria desbalanceada** (detección de anomalías financieras)
- **Técnicas de balanceo de clases**: SMOTE, ADASYN, Random Undersampling, class weighting
- **Evaluación con métricas apropiadas**: AUC-ROC, Average Precision, F1-score, curva Precisión-Recall
- **Pruebas de algoritmos**: Regresión Logística, Random Forest, Gradient Boosting, Autoencoders, Isolation Forest
- **Enseñanza de conceptos** de accuracy paradox, threshold tuning y cost-sensitive learning
- **Análisis temporal** de patrones de fraude a partir del atributo `Time`
- **Detección de anomalías no supervisada** usando únicamente las transacciones legítimas como distribución base

La combinación de desbalance extremo, alta dimensionalidad (30 features) y volumen considerable (~285k instancias) lo convierte en el benchmark estándar para sistemas de detección de fraude financiero.

## 6. 📝 Consideraciones Éticas

Este dataset presenta consideraciones éticas relevantes que deben tenerse en cuenta:

- Los datos originales fueron anonimizados mediante PCA para proteger la privacidad de los tarjetahabientes
- El dataset está licenciado bajo **Open Database License (ODbL)** — se requiere atribución y compartir derivados bajo la misma licencia
- Reconocer el trabajo original del grupo MLG-ULB y citar apropiadamente
- Los modelos entrenados sobre este dataset reflejan patrones de fraude de 2013 en Europa; su aplicación directa a otros contextos geográficos o temporales requiere validación adicional
- Los falsos negativos (fraudes no detectados) y falsos positivos (transacciones legítimas bloqueadas) tienen costos asimétricos reales; el diseño del modelo debe considerar esta asimetría

## 7. 🔗 Acceso y Uso

El dataset está disponible públicamente en Kaggle bajo **Open Database License (ODbL)**.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con pandas (descarga manual desde Kaggle):
```python
import pandas as pd

# Cargar dataset (requiere descarga previa desde Kaggle)
df = pd.read_csv('creditcard.csv')

# Separar características y etiqueta
X = df.drop(columns=['Class'])
y = df['Class']

# Información del dataset
print("Forma de los datos:", df.shape)
print("Distribución de clases:\n", y.value_counts())
print("Porcentaje de fraudes: {:.4f}%".format(y.mean() * 100))
print("Primeras filas:\n", df.head())
```

Acceso con Kaggle API:
```python
# Requiere tener configurado kaggle.json con credenciales
import subprocess
subprocess.run(['kaggle', 'datasets', 'download', '-d', 'mlg-ulb/creditcardfraud'])

import zipfile, pandas as pd
with zipfile.ZipFile('creditcardfraud.zip', 'r') as z:
    z.extractall('.')

df = pd.read_csv('creditcard.csv')
```

Acceso vía repositorio GitHub:
```python
import pandas as pd

# url del repositorio github para descargar
url = "https://raw.githubusercontent.com/rna-univ/datasets/main/creditcard/creditcard.csv"
df = pd.read_csv(url)

# Separar características y etiqueta
X = df.drop(columns=['Class'])
y = df['Class']

# Información del dataset
print("Columnas:", df.columns.tolist())
print("Primeras filas:\n", df.head())
```

Ejemplo de manejo del desbalance con Scikit-Learn:
```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score

# Escalar Time y Amount (V1-V28 ya están en escala PCA)
scaler = StandardScaler()
X[['Time', 'Amount']] = scaler.fit_transform(X[['Time', 'Amount']])

# Modelo con class_weight para manejar desbalance
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# Evaluar con métricas apropiadas (NO accuracy)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("AUC-ROC:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))
```

## 8. 🔖 Citas Recomendadas:

> Dal Pozzolo, A. (2015). *Adaptive Machine Learning for Credit Card Fraud Detection*. PhD Thesis, Université Libre de Bruxelles, supervised by G. Bontempi.

> Carcillo, F., Dal Pozzolo, A., Le Borgne, Y.-A., Caelen, O., Mazzer, Y., & Bontempi, G. (2018). *SCARFF: A Scalable Framework for Streaming Credit Card Fraud Detection with Spark*. Information Fusion, 41, 182–194. https://doi.org/10.1016/j.inffus.2017.09.005

> Lebichot, B., Le Borgne, Y.-A., He, L., Oblé, F., & Bontempi, G. (2020). *Deep-Learning Domain Adaptation Techniques for Credit Card Fraud Detection*. INNSBDDL 2019, INNS Big Data and Deep Learning Conference.
