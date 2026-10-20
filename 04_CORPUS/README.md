# Corpus STEV

Esta carpeta contiene los datasets producidos durante el proyecto STEV.

## Subcarpetas

- `original/`: corpus inicial con 80 evaluaciones (10 ejercicios × 8 evaluadores).
- `recodificado/`: recodificación con Codebook v0.3.
- `etapa5/`: corpus final con 60 registros (10 ejercicios × 6 evaluadores externos).

## Corpus vigente

El corpus vigente es:

- `etapa5/Etapa5_consolidado.csv`
- `etapa5/Etapa5_consolidado.json`

Contiene 60 registros finales y es el que se usa para los análisis de confiabilidad reportados en el cierre.

## Esquema

El esquema de columnas y claves está documentado en:

- `00_cierre/DataAvailability_STEV.md`, sección 4.
- `09_recoleccion_externa/Recoleccion_externa_schema.json`.

## Cómo cargarlo

Ejemplo mínimo en Python:

```python
import pandas as pd

df = pd.read_csv("04_corpus/etapa5/Etapa5_consolidado.csv")
print(df.shape)
```