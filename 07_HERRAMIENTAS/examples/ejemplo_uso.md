# Ejemplo de uso — calcular_alpha.py

Este script permite calcular el acuerdo entre evaluadores utilizando Krippendorff's alpha.

## Requisitos
- Python 3.9+
- pandas
- numpy

## Instalación de dependencias
pip install pandas numpy

## Ejecución
Desde la raíz del repositorio, ejecutar:

python 07_herramientas/calcular_alpha.py --input 04_corpus/etapa5/Etapa5_consolidado.csv --output 05_pilotos/etapa5/resultados_alpha/

El script leerá el archivo CSV, calculará los acuerdos por capa (L1, L2, L3) y generará los reportes en la carpeta de salida.