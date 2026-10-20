# Capa 2 — Análisis Transversal (Consolidación y Huecos)

**Documento:** `Capa2_AnalisisTransversal.md`
**Paquete:** TANDA1-STEV
**Autoría:** Marina M. Ninno

---

## 1. Descripción

Este documento consolida las 80 evaluaciones iniciales (10 ejercicios × 8 evaluadores, incluyendo la referencia humana) y documenta los huecos estructurales del instrumento original.

## 2. Hallazgos Críticos

El análisis transversal detectó los siguientes problemas sistemáticos:

### A. Códigos No Homologados
Se encontraron múltiples etiquetas inventadas o fuera de catálogo que debían ser mapeadas o eliminadas:
- `APPARENT_CAUSALITY` (Gemini A2)
- `I2.2` (Gemini A7)
- `D1.3` (Copilot A10)
- `E5.3` (Copilot A10)
- `D3.1`, `D2.1`, `A6.2`, `A4.2`, `E1.2` (Gemini)

### B. Movimientos de Capa Incorrectos
Los modelos movieron códigos a capas que no les correspondían:
- Códigos de L2 (como `A1.2` y `A4.3`) siendo usados como causa en L1.
- Códigos de L1 (como `T1.4`) siendo usados como manifestación en L2.
- Códigos de L2 (como `E2.2` y `E1.1`) siendo forzados en L3.

### C. Mal Uso de Modificadores
- Se detectó un uso excesivo del modificador `A8.3` (Perfil vulnerable) sin que existiera un código de sobre-inferencia (`A8.1` o `A8.2`) en L1 que lo justificara.

### D. Fronteras Críticas No Resueltas
Las mayores discrepancias entre modelos ocurrieron en:
- La frontera entre omisión de mecanismo (`A1.2`), trivialidad (`A1.4`) y omisión de contexto (`E2.1`).
- La distinción entre tipos de vacío en L1 (etiqueta sin contenido vs. ausencia de pretensión).

## 3. Conclusión y Acción

Este análisis fue el insumo directo para la fase de Homologación. Sentó las bases para el **Codebook v0.1** y motivó las reglas operativas (Regla del Verbo, Prueba de Algodón, Árbol L1) que se consolidarían en las versiones posteriores hasta llegar a la v1.0.