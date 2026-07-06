<p align="center">
<img src="banner.png" width="1000">
</p>

# 🚢 Dataset Titanic: Análisis de Supervivencia

## 1. 📖 Descripción General

El dataset del Titanic constituye uno de los conjuntos de datos más emblemáticos en el ámbito de la ciencia de datos y el machine learning. Documenta la tragedia del RMS Titanic, el transatlántico británico que naufragó en su viaje inaugural la madrugada del 15 de abril de 1912 tras colisionar con un iceberg en el Atlántico Norte. Este evento histórico, que cobró la vida de aproximadamente 1,500 personas de las 2,224 abordo, ha sido meticulosamente documentado y representa un caso de estudio invaluable para el análisis predictivo y la comprensión de patrones de supervivencia en situaciones de crisis.

La versión utilizada en este análisis proviene del repositorio de **DataScience Dojo**, una organización dedicada a la educación en ciencia de datos que ha curado y mantenido esta versión del dataset para propósitos educativos y de investigación.

## 2. 📊 Atributos y Significados

### 2.1 🔑 Variable Objetivo
- **Survived** (Supervivencia): Indicador binario que registra el destino final del pasajero
  - `0`: No sobrevivió (falleció en el naufragio)
  - `1`: Sobrevivió (fue rescatado)

### 2.2 👤 Atributos Demográficos
- **Pclass** (Clase del Pasaje): Representa el nivel socioeconómico del pasajero a través de la clase del ticket
  - `1`: Primera clase (alta sociedad)
  - `2`: Segunda clase (clase media)
  - `3`: Tercera clase (inmigrantes y clase trabajadora)

- **Sex** (Género): Género biológico del pasajero
  - `male`: Masculino
  - `female`: Femenino

- **Age** (Edad): Edad del pasajero en años. Los menores de 1 año están representados con fracciones (ej: 0.75 = 9 meses). Presenta valores nulos que requieren imputación.

### 2.3 👨‍👩‍👧‍👦 Atributos Familiares
- **SibSp** (Hermanos/Cónyuges): Número de hermanos o cónyuges abordo del Titanic. Incluye:
  - Hermanos
  - Hermanastros
  - Cónyuges (los novios fueron contabilizados como cónyuges)

- **Parch** (Padres/Hijos): Número de padres o hijos abordo. Incluye:
  - Hijos
  - Hijastros
  - Padres o tutores

### 2.4 💰 Atributos Económicos y de Viaje
- **Fare** (Tarifa): Precio pagado por el ticket en libras esterlinas (£). Refleja la combinación de clase y comodidades.

- **Embarked** (Puerto de Embarque): Puerto inicial donde el pasajero abordó el Titanic
  - `C`: Cherbourg, Francia
  - `Q`: Queenstown (ahora Cobh), Irlanda
  - `S`: Southampton, Inglaterra

### 2.5 🏷️ Atributos Identificativos
- **PassengerId** (ID del Pasajero): Identificador único para cada pasajero. Variable administrativa sin valor predictivo.

- **Name** (Nombre): Nombre completo del pasajero, incluyendo título de cortesía (Mr, Mrs, Dr, etc.), que puede inferir edad, estado civil y estatus social.

- **Ticket** (Número de Ticket): Identificador alfanumérico del ticket. Presenta patrones complejos con valor predictivo limitado.

- **Cabin** (Cabina): Número de cabina asignado. Alto porcentaje de valores nulos (77.1%), pero puede indicar ubicación en el barco y estatus.

## 3. 🏢 Origen y Procedencia

### 3.1 📚 Fuente Primaria: DataScience Dojo

El dataset utilizado en este análisis fue obtenido del repositorio público de **DataScience Dojo** en GitHub, una organización educativa reconocida en la comunidad de ciencia de datos por proporcionar recursos de aprendizaje de alta calidad.

**URL Oficial**:  
> https://github.com/datasciencedojo/datasets
> 
> https://code.datasciencedojo.com/datasciencedojo/datasets

**Archivo Específico**:  
`titanic.csv` en la rama principal del repositorio

### 4. 🏛️ Fuentes Históricas Originales

Los datos originales provienen de múltiples fuentes históricas:

1. **British Board of Trade** - Informe oficial de la investigación del naufragio (1912)
2. **Comité del Senado de los Estados Unidos** - Investigación americana del desastre
3. **White Star Line** - Registros de la compañía naviera
4. **Encyclopedia Titanica** - Base de datos colaborativa de investigación histórica

### 4.1 🔄 Proceso de Curaduría

DataScience Dojo ha realizado un proceso de curaduría que incluye:

- **Unificación** de múltiples fuentes históricas
- **Limpieza** básica de datos inconsistentes
- **Estandarización** de formatos y valores
- **Documentación** clara de variables y valores posibles
- **Mantenimiento** continuo para asegurar accesibilidad

## 5. 🎯 Valor Analítico

Este dataset presenta características excepcionales para el aprendizaje:

- **Tamaño manejable** (891 registros, 12 variables)
- **Mezcla de tipos de datos** (numéricos, categóricos, textuales)
- **Valores nulos** que permiten practicar técnicas de imputación
- **Relaciones predictivas** no lineales y complejas
- **Contexto histórico** rico y documentado

## 6. 📝 Consideraciones Éticas

Si bien el dataset representa una tragedia humana real, su uso con propósitos educativos y de investigación ha sido ampliamente aceptado por la comunidad científica, siempre que se maneje con el respeto apropiado hacia la memoria de las víctimas y sobrevivientes.

## 7. 🔗 Acceso y Uso

El dataset está disponible bajo licencia abierta para propósitos educativos y de investigación. Su uso comercial puede requerir verificación de permisos específicos.

### 7.1 📥 Cómo cargarlo en Python:

Acceso con el DataLoader de la biblioteca `rna` (Recomendado):
```python
# Instalar la biblioteca si no está disponible:
# !pip install https://github.com/RNA-UNIV/rna/archive/refs/heads/main.zip

from rna.data.ClassDataLoader import DataLoader

# Cargar el dataset como DataFrame de Pandas
df = DataLoader.load_dataframe('titanic')
```

Acceso vía Seaborn:
```python
import seaborn as sns
import pandas as pd

# Cargar dataset Titanic desde Seaborn
titanic = sns.load_dataset('titanic')

# Separar características y etiquetas
X = titanic.drop(columns=['survived'])
y = titanic['survived']

print("Dimensiones:", titanic.shape)
print(titanic.head())
```
Acceso vía DataScience Dojo (GitHub):
```python
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)

# Separar características y etiquetas
X = titanic.drop(columns=['Survived'])
y = titanic['Survived']

print("Dimensiones:", titanic.shape)
print(titanic.head())

```

Acceso vía GitHub:
```python
import pandas as pd

url = "https://raw.githubusercontent.com/rna-univ/datasets/main/titanic/titanic.csv"
titanic = pd.read_csv(url)

# Separar características y etiquetas
X = titanic.drop(columns=['Survived'])
y = titanic['Survived']

print("Dimensiones:", titanic.shape)
print(titanic.head())

```

## 8. 🔖 Cita Recomendada:
>Dataset Titanic. Curated by DataScience Dojo. Retrieved from https://github.com/datasciencedojo/datasets

---

*Última actualización: Abril 2024*  
*Mantenido por la comunidad de Data Science para propósitos educativos*