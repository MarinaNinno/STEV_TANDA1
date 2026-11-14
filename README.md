# Protocolo STEV — TANDA1

Sistema Tricapa de Evaluación Epistémica para respuestas de modelos de lenguaje.

> **Estado: contenido informativo, no auditado.**
> Este repositorio reúne material de trabajo del proyecto STEV. Ninguna parte ha pasado por un proceso de auditoría de fidelidad. Las cifras (incluidas las métricas de acuerdo entre evaluadores) son reportes del autor, sin verificación independiente. La auditoría se lleva por separado y no forma parte de este repositorio.
> El contenido se publica sin citas literales de terceros y sin datos personales o sensibles.

- **Codebook:** v1.0 de trabajo (sin auditar)
- **Paquete:** TANDA1-STEV
- **Última actualización:** [fecha de la última subida]
- **Autoría:** Marina (diseño y dirección). Redacción asistida por modelos de lenguaje: Claude (documentos de diseño), DeepSeek (extracciones de capa 1) y Meta AI (fichas de capa 2). Las fichas tienen revisión humana pendiente.

---

## Qué es este proyecto

STEV es un instrumento de evaluación epistémica tricapa que clasifica respuestas de modelos de lenguaje según:

- **L1 (Causa):** ¿cuál es la causa técnico-ontológica del fallo?
- **L2 (Manifestación):** ¿cómo se manifiesta el fallo en el texto?
- **L3 (Impacto):** ¿qué impacto cognitivo genera?

Cada capa responde una pregunta distinta y no compite con las otras.

---

## Estado del proyecto (reportado, sin auditar)

| Componente | Estado reportado |
|---|---|
| Codebook | v1.0 de trabajo |
| Iteraciones | 6 (v0.1 a v0.6) |
| Pilotos de confiabilidad | 5 (v0.3 a etapa 5) |
| Ejercicios del corpus del piloto | 10 (A1–A10) |
| Evaluadores externos | 6 (Grok, GPT, Copilot, Gemini, Meta, DeepSeek) |
| Decisiones registradas | 67 |
| Corpus del piloto (etapa 5) | 60 registros |

> El corpus del piloto (60 registros) es distinto del corpus de génesis, que consta de 254 extracciones trazables registradas en un manifiesto aparte.

## Métricas del piloto (reportadas, sin auditar)

| Capa | Acuerdo bruto | Alpha |
|---|---|---|
| L1 (¿vacío?) | 100% | — |
| L1 (motivo) | 63.3% | 0.48 |
| L2 | 95% | 0.85 |
| L3 | 100% | 1.00 |

---

## Cómo navegar este repositorio

[mantener la tabla, pero verificar antes de publicar que cada ruta existe]

---

## Cómo citar

Marina. (2026). *Protocolo STEV: evaluación epistémica tricapa de respuestas de modelos de lenguaje* (versión de trabajo). Paquete TANDA1-STEV.

---

## Licencia

Por definir. Recomendado: documentos CC BY 4.0, código MIT, datasets CC BY 4.0.

---

## Contacto

Ver `CITATION.cff` para metadatos completos.