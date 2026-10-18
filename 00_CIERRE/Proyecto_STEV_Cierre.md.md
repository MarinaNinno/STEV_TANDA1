# Proyecto STEV — Documento de cierre

**Documento:** `Proyecto_STEV_Cierre.md`
**Paquete:** TANDA1-STEV
**Versión del Codebook:** v1.0 (final)
**Fecha:** 2026-10-07
**Autoría:** Marina M. Ninno (diseño) + Claude (redacción y análisis)
**Estado:** cierre del proyecto

---

## 0. Propósito

Este documento cierra el proyecto STEV (Sistema Tricapa de Evaluación Epistémica). Consolida:

- El recorrido completo del proyecto (Capa 1 → Codebook v1.0).
- Los aprendizajes principales.
- Los límites del instrumento.
- Los entregables finales.
- La hoja de ruta futura.

Su función es servir como **documento maestro de referencia** para auditoría, portfolio y publicaciones derivadas.

---

## 1. Resumen ejecutivo

**El proyecto STEV diseñó, calibró y validó un instrumento de evaluación epistémica tricapa para clasificar respuestas de modelos de lenguaje.**

**Resultado final:** Codebook v1.0, con acuerdos del 95–100% en L2 y L3, y 63.3% en L1 (motivo).

**Historia:** 6 iteraciones del Codebook (v0.1 a v0.6), 5 pilotos (v0.3 a etapa 5), 67 decisiones registradas, 10 ejercicios × 6 evaluadores externos = 60 registros finales.

**Conclusión:** el instrumento es estable en las dimensiones clave (¿hay fallo? ¿dónde se manifiesta? ¿qué impacto tiene?). Tiene un límite conocido en la clasificación fina del motivo de vacío en L1.

---

## 2. Contexto y motivación

### 2.1 El problema inicial

Los modelos de lenguaje producen respuestas con distintos tipos de fallos epistémicos: falsedades, omisiones, evasiones, tautologías, errores de aplicación. La clasificación plana no captura la relación causal entre estos fallos.

### 2.2 La hipótesis

Una arquitectura tricapa (L1 causa, L2 manifestación, L3 impacto) permite clasificar los fallos sin competencia entre categorías.

### 2.3 El objetivo

Diseñar un instrumento que:

- Sea trazable (cada decisión documentada).
- Sea auditable (cualquier tercero puede reproducir).
- Sea aplicable por evaluadores independientes.
- Reconozca sus límites.

---

## 3. Recorrido del proyecto

### 3.1 Fase 1 — Recolección cruda

**Producto:** 80 evaluaciones (10 ejercicios × 8 evaluadores).

**Evaluadores iniciales:** Grok, GPT, Copilot, Gemini, Meta, Claude, DeepSeek + Marina (referencia).

**Formato:** fichas STEV sin homologación. Códigos mezclados entre versiones.

### 3.2 Fase 2 — Consolidación y detección de huecos

**Producto:** documento `Capa2_AnalisisTransversal.md`.

**Hallazgos:**

- Códigos no homologados (D1.3, E5.3, APPARENT_CAUSALITY, I2.2).
- Movimientos de capa incorrectos (A1.2, A4.3 en L1; T1.4 en L2; E2.2, E1.1 en L3).
- A8.3 mal aplicado en múltiples casos.
- Fronteras críticas no resueltas (A1.2 vs E2.1 vs A1.4).

### 3.3 Fase 3 — Iteraciones del Codebook

| Versión | Fecha | Aportes principales |
|---|---|---|
| **v0.1** | 2026-09-29 | Homologación de códigos no catalogados. Arquitectura tricapa inicial. |
| **v0.2** | 2026-09-29 | Árbol L1 explícito. Test 1 de L2. Criterio L3. |
| **v0.3** | 2026-09-29 | Test 1 reformulado. Distinción errónea vs incompleta en L3. |
| **v0.4** | 2026-10-02 | Definiciones operacionales D1.1/D1.2. Test 1 en 3 casos. Ajuste 6 (fronteras de motivos de vacío en L1). Regla de mapeo para Evaluación global. |
| **v0.5** | 2026-10-06 | Reversión del Test 1 a v0.3. Zonas de ambigüedad irreducible. Advertencia de convergencia. |
| **v0.6** | 2026-10-06 | Fila faltante en regla de mapeo. Fractura A6 L1 documentada. Nota sobre alpha. |
| **v1.0** | 2026-10-07 | Declaración de versión final. |

### 3.4 Fase 4 — Pilotos

| Piloto | Ejercicios | Evaluadores | Resultado |
|---|---|---|---|
| **v0.1** | A2, A5, A6 | 7 modelos + Marina | Alpha L1: 0.395; L2: 0.327; L3: 0.124 |
| **v0.2** | A2, A5, A6 | 7 modelos + Marina | Alpha L1: 0.572; L2: 0.285; L3: 0.511 |
| **v0.3** | A2, A5, A6 | 7 modelos + Marina | Alpha L1: 0.572; L2: 1.000 (inflado); L3: 1.000 (inflado) |
| **v0.4** | A2, A5, A6 | 6 externos + Claude (ref) | Alpha L1: 0.40; L2: 0.06; L3: 1.00 |
| **v0.5** | A2, A5, A6 | 6 externos + Claude (ref) | Acuerdo L1 (motivo): 66.7%; L2: 88.9%; L3: 88.9% |
| **v0.6** | A2, A5, A6 | 6 externos + Claude (ref) | Acuerdo L1 (motivo): 83.3%; L2: 88.9%; L3: 94.4% |
| **Etapa 5** | A1–A10 | 6 externos + Claude (ref) | Acuerdo L1 (motivo): 63.3%; L2: 95%; L3: 100% |

### 3.5 Fase 5 — Cierre

**Producto:** Codebook v1.0 + este documento de cierre + Decision Log (67 decisiones).

---

## 4. El instrumento final (Codebook v1.0)

### 4.1 Arquitectura

| Capa | Pregunta | Tipo |
|---|---|---|
| **L1** | ¿Cuál es la causa técnico-ontológica del fallo? | Interpretativa |
| **L2** | ¿Cómo se manifiesta el fallo en el texto? | Determinista con zonas de ambigüedad irreducible |
| **L3** | ¿Qué impacto cognitivo genera? | Determinista |

### 4.2 Componentes operativos

1. **Regla del Verbo:** tipo de pregunta determina familia L1.
2. **Prueba de Algodón:** distingue falso de vacío.
3. **Árbol L1** con 4 pasos y 5 motivos de vacío.
4. **Definiciones operacionales** de D1.1 y D1.2.
5. **Test 1 simple de L2** (revertido en v0.5).
6. **Tres zonas de ambigüedad irreducible** en L2 (Z1, Z2, Z3).
7. **Criterio L3** con regla dura "vacío por defecto".
8. **Regla de mapeo** para Evaluación global (8 filas).
9. **Restricción de A8.3** (siempre con A8.1/A8.2).
10. **Catálogo de 62 códigos, 19 familias.**

### 4.3 Métricas de estabilidad

| Capa | Acuerdo bruto | Alpha | Interpretación |
|---|---|---|---|
| L1 (¿vacío?) | 100% | — | Unanimidad |
| L1 (motivo) | 63.3% | 0.48 | Moderado (punto débil documentado) |
| L2 | 95% | 0.85 | Casi perfecto |
| L3 | 100% | 1.00 | Unanimidad (techo) |

---

## 5. Aprendizajes principales

### 5.1 Sobre la arquitectura

1. **La arquitectura tricapa funciona.** Cada capa responde una pregunta distinta y no compite con las otras.
2. **L1 es interpretativa, L2 y L3 son deterministas.** Esto es una propiedad del diseño, no un defecto.
3. **Los tests deterministas inflan el alpha.** Un alpha = 1.0 con tests deterministas no es logro. La consistencia interna del manual no es confiabilidad inter-evaluador.

### 5.2 Sobre el Codebook

1. **Los árboles de decisión son más efectivos que las tablas de códigos.** El árbol de L1 redujo la dispersión de 0.395 a 0.60.
2. **Los tests operativos deben distinguir categorías semánticas, no solo formas lingüísticas.** El Test 1 v0.4 no distinguía entre marcos interpretativos.
3. **Un test demasiado estricto puede sobrecodificar.** Con v0.3, 6 de 10 ejercicios caían en A1.2. Con v0.5, el Test 1 simple recuperó el acuerdo.
4. **La parsimonia informativa es tan importante como el test de independencia.** A10 lo demostró.
5. **Algunas fronteras son irreducibles.** Z1, Z2, Z3 no se resuelven con más criterios.
6. **Documentar las zonas de ambigüedad es más honesto que forzar una resolución.** El kit v0.5 y v0.6 incluyen zonas explícitas.

### 5.3 Sobre el proceso de validación

1. **Los pilotos deben medir lo que se pretende medir.** Los tres primeros no lo hicieron.
2. **La consistencia interna del manual no es confiabilidad inter-evaluador.** Son dos cosas distintas.
3. **Iterar tiene un techo.** Después de v0.6, iterar más no mejora las métricas.
4. **El rediseño es parte del proceso, no un fracaso.** Los pilotos refinaron el Codebook.

### 5.4 Sobre la auditoría

1. **Documentar los errores es tan importante como documentar los aciertos.** El Decision Log registra 67 decisiones, incluyendo correcciones.
2. **Los hallazgos negativos son hallazgos.** La sobrecodificación de A1.2 es un hallazgo que informó v0.5.
3. **La trazabilidad permite auditar.** Cualquier tercero puede reproducir los pasos.
4. **Los límites del instrumento son parte del instrumento.** Documentarlos es rigor, no debilidad.

---

## 6. Límites documentados del instrumento

| Límite | Documentado en |
|---|---|
| L1 (motivo) con 63.3% de acuerdo | D-066 |
| A4 y A9 como casos de máxima ambigüedad | D-067 |
| Z1, Z2, Z3 como zonas de ambigüedad irreducible | v0.5 |
| A5 L1 con fractura 5-1 | D-064 |
| A6 L1 con fractura resuelta 6-0 | D-064 |
| Alpha distorsionado por prevalencia | D-062 |
| Test 1 no aplica perfectamente a preguntas definicionales | v0.6 |
| Error de formato residual en el kit (motivo como código) | resuelto en v0.6 |

---

## 7. Entregables finales

### 7.1 Documentos del proyecto

| Documento | Rol |
|---|---|
| Codebook_STEV_v1.0.md | Instrumento final |
| DecisionLog_STEV.md | Registro de 67 decisiones |
| Proyecto_STEV_Cierre.md | Este documento |
| DataAvailability_STEV.md | Declaración de disponibilidad |
| Reporte_Portfolio.md | Reporte para portfolio |
| Kit_Evaluacion_STEV_v1.0.md | Kit de evaluación final |

### 7.2 Documentos históricos

| Documento | Rol |
|---|---|
| Capa2_AnalisisTransversal.md | Análisis del corpus original |
| Codebook_STEV_v0.1.md a v0.6.md | Iteraciones |
| Piloto_v0.3_rediseno_desacuerdos.md | Análisis de desacuerdos |
| Piloto_v0.4_resultados.md | Resultados del piloto v0.4 |
| Piloto_v0.5_resultados.md | Resultados del piloto v0.5 |
| Piloto_v0.6_resultados.md | Resultados del piloto v0.6 |
| Etapa5_resultados.md | Resultados de etapa 5 |

### 7.3 Datasets

| Archivo | Contenido |
|---|---|
| stev_tanda1_v0.csv / .json | Corpus original |
| stev_tanda1_v0.3.csv / .json | Recodificación v0.3 |
| Etapa5_consolidado.csv | Corpus final (60 registros) |

---

## 8. Hoja de ruta futura

### 8.1 Aplicaciones del instrumento

1. **Evaluación de respuestas de LLMs** en dominios específicos (biología, física, ciencias sociales).
2. **Auditoría de calidad epistémica** en producción de contenido.
3. **Investigación sobre sesgos** de modelos de lenguaje.
4. **Herramienta de fine-tuning** (usar los vectores STEV como señal de corrección).

### 8.2 Extensiones posibles

1. **Aplicar el Codebook a corpus más grandes** (100+ ejercicios).
2. **Aplicar el Codebook a dominios no cubiertos** (matemática, derecho, medicina).
3. **Desarrollar un pipeline automático** que aplique el Codebook vía LLM.
4. **Publicar el instrumento** en revista de metodología o NLP.
5. **Extender la arquitectura a una cuarta capa** (si se identifica una dimensión no cubierta).

### 8.3 Hallazgos pendientes para v1.1

| ID | Hallazgo | Prioridad |
|---|---|---|
| H-01 | Sustitución mecanística (código nuevo para A2/A6) | Alta |
| H-02 | Subdivisión de A6 (comprensión vs ejecución) | Media |
| H-03 | Subdivisión de L3 (L3A naturaleza / L3B severidad) | Media |
| H-04 | Refinamiento de A7.2 para over-hedging | Media |
| H-05 | Código específico para "comprensión insuficiente" en L3 | Media |
| H-09 | Zonas de ambigüedad irreducible en L2 | Documentado |
| H-10 | Fractura interpretativa entre marcos | Documentado |
| H-11 | L1 (motivo) como punto débil documentado | Documentado |
| H-12 | A4 y A9 como casos de máxima ambigüedad | Documentado |

---

## 9. Métricas del proyecto

| Métrica | Valor |
|---|---|
| Iteraciones del Codebook | 6 (v0.1 a v0.6) + 1 (v1.0) |
| Pilotos | 5 |
| Ejercicios del corpus | 10 (A1–A10) |
| Evaluadores externos | 6 |
| Registros totales en etapa 5 | 60 |
| Decisiones registradas | 67 |
| Documentos generados | ~20 |
| Alpha L1 (motivo) | 0.48 |
| Alpha L2 | 0.85 |
| Alpha L3 | 1.00 |
| Acuerdo bruto L1 (motivo) | 63.3% |
| Acuerdo bruto L2 | 95% |
| Acuerdo bruto L3 | 100% |
| Errores de formato (etapa 5) | 0/60 |

---

## 10. Conclusión

El proyecto STEV diseñó, calibró y validó un instrumento de evaluación epistémica tricapa para respuestas de modelos de lenguaje. El Codebook v1.0 es estable en las dimensiones clave y reconoce sus límites.

**Los tres aportes principales del proyecto son:**

1. **Arquitectura tricapa** que separa causa, manifestación e impacto.
2. **Método de calibración iterativo** que documenta cada decisión y acepta límites.
3. **Instrumento auditable** aplicable por evaluadores independientes.

**El proyecto cierra con un instrumento estable, un registro de 67 decisiones, y un corpus de 60 registros listo para investigación futura.**

---

## 11. Estado del cierre

| Sección | Estado |
|---|---|
| 0. Propósito | ✅ |
| 1. Resumen ejecutivo | ✅ |
| 2. Contexto | ✅ |
| 3. Recorrido | ✅ |
| 4. Instrumento final | ✅ |
| 5. Aprendizajes | ✅ |
| 6. Límites | ✅ |
| 7. Entregables | ✅ |
| 8. Hoja de ruta futura | ✅ |
| 9. Métricas | ✅ |
| 10. Conclusión | ✅ |
| 11. Estado | ✅ |

---

## 12. Próximos pasos

Con el cierre del proyecto listo:

1. **Paso 2 — Data Availability Statement** actualizado con etapa 5.
2. **Paso 3 — Reporte de portfolio** adaptado para presentación.
3. **Paso 4 — Repositorio final** con todos los documentos organizados.