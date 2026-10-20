# Protocolo STEV — Arquitectura Tricapa

**Versión:** 1.0
**Paquete:** TANDA1-STEV
**Autoría:** Marina M. Ninno

---

## 1. Qué es el Protocolo STEV

El Sistema Tricapa de Evaluación Epistémica (STEV) es un instrumento diseñado para clasificar los fallos en las respuestas generadas por modelos de lenguaje. 

A diferencia de las taxonomías planas (que mezclan causas, síntomas y efectos), STEV separa la evaluación en tres dimensiones independientes que no compiten entre sí.

## 2. Las tres capas

### L1 — Causa (Capa Interpretativa)
Responde a la pregunta: **¿Cuál es la causa técnico-ontológica del fallo?**
Evalúa la raíz del problema (por ejemplo, una diferencia específica demasiado amplia, una falsa causalidad o una tautología). Es la capa más interpretativa del protocolo.

### L2 — Manifestación (Capa Determinista)
Responde a la pregunta: **¿Cómo se manifiesta el fallo en el texto?**
Evalúa cómo se ve el error en la superficie semántica (por ejemplo, vaguedad, omisión de mecanismos, o respuestas evasivas). Es una capa determinista (dados los tests, el resultado es el mismo).

### L3 — Impacto (Capa Determinista)
Responde a la pregunta: **¿Qué impacto cognitivo genera en quien lee?**
Evalúa las consecuencias para el usuario (por ejemplo, si induce una heurística errónea o refuerza un mito). Rige la regla de "vacío por defecto": solo se activa con evidencia textual explícita.

## 3. Orden de aplicación

El protocolo exige un orden canónico estricto:
**L1 → L2 → L3**
*(Primero se busca la causa raíz, luego el síntoma, luego el impacto).*

## 4. Reglas operativas clave

1. **Regla del Verbo:** El tipo de pregunta del prompt ("¿Qué es?", "¿Por qué?", "¿Cómo funciona?") orienta la búsqueda inicial en L1.
2. **Prueba de Algodón:** Antes de asignar un código, el evaluador debe distinguir si la respuesta es *falsa*, *vacía* o *verdadera pero insuficiente*.
3. **Máximo 3 etiquetas:** Para corrección de modelos (fine-tuning), se recomienda usar una etiqueta por capa.