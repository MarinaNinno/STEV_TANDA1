# Protocolo STEV — TANDA1

**Sistema Tricapa de Evaluación Epistémica para respuestas de modelos de lenguaje.**

- **Versión del Codebook:** v1.0 (final)
- **Paquete:** TANDA1-STEV
- **Fecha de cierre:** 2026-10-07
- **Autoría:** Marina (diseño) + Claude (redacción)

---

## Qué es este proyecto

STEV es un instrumento de evaluación epistémica tricapa que clasifica respuestas de modelos de lenguaje según:

- **L1 (Causa):** ¿cuál es la causa técnico-ontológica del fallo?
- **L2 (Manifestación):** ¿cómo se manifiesta el fallo en el texto?
- **L3 (Impacto):** ¿qué impacto cognitivo genera?

Cada capa responde una pregunta distinta y no compite con las otras.

---

## Estado del proyecto

| Componente | Estado |
|---|---|
| Codebook | v1.0 (final) |
| Iteraciones | 6 (v0.1 a v0.6) |
| Pilotos de confiabilidad | 5 (v0.3 a etapa 5) |
| Ejercicios del corpus | 10 (A1–A10) |
| Evaluadores externos | 6 (Grok, GPT, Copilot, Gemini, Meta, DeepSeek) |
| Decisiones registradas | 67 |
| Corpus final | 60 registros |

---

## Métricas finales

| Capa | Acuerdo bruto | Alpha |
|---|---|---|
| L1 (¿vacío?) | 100% | — |
| L1 (motivo) | 63.3% | 0.48 |
| L2 | 95% | 0.85 |
| L3 | 100% | 1.00 |

---

## Cómo navegar este repositorio

Cada carpeta principal tiene su propio `README.md` con instrucciones específicas. Esta tabla te orienta según lo que necesites.

| Si querés… | Andá a… |
|---|---|
| Entender el proyecto completo | `00_cierre/Proyecto_STEV_Cierre.md` |
| Ver el instrumento final | `01_codebook/Codebook_STEV_v1.0.md` |
| Ver las decisiones del proyecto | `02_decision_log/DecisionLog_STEV.md` |
| Consultar el catálogo de códigos | `03_nosografia/Nosografia_STEV_v0.md` |
| Ver los datos | `04_corpus/etapa5/Etapa5_consolidado.csv` |
| Ver los resultados | `05_pilotos/etapa5/Etapa5_resultados.md` |
| Aplicar el instrumento | `06_kits/Kit_Evaluacion_STEV_v1.0.md` |
| Reproducir los análisis | `07_herramientas/calcular_alpha.py` |
| Ver el análisis del corpus original | `08_analisis_transversal/Capa2_AnalisisTransversal.md` |
| Usar la plantilla de recolección | `09_recoleccion_externa/Recoleccion_externa_template.csv` |
| Ver el reporte de portfolio | `00_cierre/Reporte_Portfolio.md` |

---

## Cómo citar

> Marina. (2026). *Protocolo STEV: evaluación epistémica tricapa de respuestas de modelos de lenguaje*. Paquete TANDA1-STEV. Codebook v1.0.

---

## Licencia

Por definir. Recomendado:

- Documentos: CC BY 4.0
- Código: MIT o similar
- Datasets: CC BY 4.0

---

## Contacto

Ver `CITATION.cff` para metadatos completos.