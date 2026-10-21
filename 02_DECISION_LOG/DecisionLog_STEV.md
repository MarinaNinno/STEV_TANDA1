# Decision Log — Protocolo STEV

**Documento:** `DecisionLog_STEV.md`
**Paquete:** TANDA1-STEV
**Fecha de apertura:** 2026-09-29
**Última actualización:** 2026-10-19
**Versión actual del Codebook:** v1.0 (final)
**Autoría:** Marina M. Ninno (diseño) + Claude (redacción)

---

## 0. Propósito

Este Decision Log registra **cada decisión estructural, metodológica o de calibración** del proyecto STEV con trazabilidad completa. Su función es que un tercero pueda auditar qué se decidió, cuándo, por qué, y qué versión del Codebook afectó.

---

## 1. Convenciones

| Campo | Descripción |
|---|---|
| **ID** | Identificador único: `D-NNN` |
| **Fecha** | Fecha de la decisión |
| **Versión** | Versión del Codebook afectada |
| **Categoría** | Diseño / Nosografía / Capa / Regla / Metodología / Corrección |
| **Cambio** | Qué se decidió |
| **Motivo** | Por qué |
| **Estado** | Aceptado / Pendiente / Rechazado |

---

## 2. Registro de decisiones (Resumen de las 67 decisiones)

*(Nota: Para mantener la legibilidad del repositorio, se presentan las decisiones fundacionales y de mayor impacto. El registro completo se detalla en los documentos de cierre).*

### Decisiones de Diseño y Arquitectura
- **D-001:** Adoptar arquitectura tricapa (L1 causa, L2 manifestación, L3 impacto).
- **D-002:** Orden canónico L1 → L2 → L3 (Hallo-compliant).
- **D-003:** Reformular el instrumento como arquitectura jerárquica, no taxonomía plana.

### Decisiones de Capa
- **D-008:** D1.1 vive en L1; A1.4 vive en L2 (separación estricta).
- **D-010:** A1.2 no se mueve a L1; permanece en L2.
- **D-011:** A4.3 no se mueve a L1; permanece en L2.
- **D-012:** E2.2 y E1.1 no se usan en L3; L3 usa E5.1, E5.2, A8.3, A9.1.

### Decisiones de Reglas Operativas
- **D-019:** Regla del Verbo (tipo de pregunta determina familia L1).
- **D-020:** Prueba de Algodón (distinguir falso de vacío).
- **D-021:** Test de Independencia (múltiples causas en L1).
- **D-023:** L3 vacío por defecto (solo con evidencia textual).
- **D-024:** A8.3 no se usa solo (siempre con A8.1/A8.2).
- **D-032:** Tests L2 redefinidos en v0.3 (mecanismo interno).
- **D-033:** Test L3 errónea vs incompleta (v0.3).

### Decisiones Metodológicas y de Calibración
- **D-034:** Marina se excluye del cálculo de alpha (es diseñadora).
- **D-036:** Documentar sobrecodificación de A1.2 (hallazgo H-06).
- **D-037:** Piloto v0.3 mide consistencia interna, no confiabilidad (tests deterministas).
- **D-038:** Rediseño del piloto con evaluadores LLM independientes.
- **D-047:** Claude actúa como referencia de aplicación esperada, no como evaluador en alpha.
- **D-049:** DeepSeek se incluye como sexto evaluador externo.
- **D-059:** Reversión del Test 1 a v0.3 y documentación de zonas de ambigüedad irreducible (Z1, Z2, Z3).
- **D-063:** Avanzar a Etapa 5 con Codebook v0.6.
- **D-065:** Declarar Codebook v0.6 como versión final (v1.0).
- **D-069:** Registrar el rol fundacional e influencia epistémica de Grok en Tanda 1. Grok cumplió un triple rol... (Estado: Aceptado).
- **D-070:** Adoptar el orden Hallo-compliant (L1 > L2 > L3) como modelo por defecto para la priorización de capas. (Estado: Aceptado).
- **D-071:** Establecer la "Parsimonia Etiológica" como regla de oro: dejar L1 vacío es una decisión válida y necesaria cuando no hay un mecanismo estructural claro, evitando el "relleno" artificial. (Estado: Aceptado).

### Correcciones Aceptadas
- **D-040:** Copilot A1: colapso L1/L2 corregido.
- **D-041:** Copilot A2: L1 forzado corregido a vacío.
- **D-042:** Gemini A2: código inventado (APPARENT_CAUSALITY) mapeado a vacío.
- **D-043:** DeepSeek A2: F1.3 cambiado a A8.2.
- **D-044:** Claude A5: Nivel Bajo corregido a Medio.

---

## 3. Estado Actual

| Métrica | Valor |
|---|---|
| Total de decisiones registradas | 67 |
| Decisiones fundacionales | 12 |
| Correcciones de evaluadores | 8 |
| Decisiones de calibración (pilotos) | 15 |
| Estado del Codebook | v1.0 (Final) |
| Estado del Corpus | Etapa 5 finalizada (60 registros) |

---

### Nota sobre el origen del instrumento
El protocolo STEV no nació como una arquitectura teórica abstracta, sino de la práctica empírica de su autora al incursionar como principiante en la evaluación de modelos de lenguaje. Las primeras iteraciones, la agrupación ad hoc de errores y la necesidad de un criterio de calidad (como el que exigen plataformas tipo Hallo) fueron moldeando la Nosografía, acompañada en su fase inicial por Grok, quien ejerció un rol de tutoría y calibración antes de la conformación del equipo de 7 modelos.

---

*Fin del Decision Log.*