# Capa 1 — Análisis Paralelo (Corpus Original)

**Documento:** `Capa1_AnalisisParalelo.md`
**Paquete:** TANDA1-STEV
**Autoría:** Marina M. Ninno

---

## 1. Descripción

Este documento resume el análisis inicial de las respuestas de los 7 modelos evaluadores (Grok, GPT, Copilot, Gemini, Meta, Claude y DeepSeek) frente a los 10 ejercicios del corpus (A1 a A10).

El objetivo de esta fase fue identificar patrones de error, evaluar la consistencia entre modelos y detectar los primeros choques conceptuales en la evaluación epistémica.

## 2. Hallazgos Principales

1. **Colapso de capas:** Varios modelos mezclaron causas (L1) con manifestaciones (L2). Por ejemplo, ubicar la vaguedad (A1.4) como la causa raíz del fallo.
2. **Creación de códigos no catalogados:** Ante la falta de una categoría específica, algunos modelos inventaron códigos (ej. `APPARENT_CAUSALITY` por Gemini o `D1.3` por Copilot).
3. **Alta variabilidad en L1:** La capa interpretativa mostró una dispersión significativa. Para un mismo ejercicio (ej. A2), los modelos asignaron causas radicalmente distintas (C1.3, D1.1, vacío).
4. **Consistencia en L2 y L3:** Las capas de manifestación e impacto mostraron un mayor acuerdo inicial, especialmente en identificar respuestas correctas pero triviales (A1.4).

## 3. Conclusión

El análisis paralelo reveló que una taxonomía plana no era suficiente para capturar la complejidad de los errores. La falta de reglas estrictas de frontera y la ambigüedad en los criterios de vacío demostraron la necesidad de diseñar una arquitectura tricapa formalizada con reglas operativas claras (Codebook v0.1).