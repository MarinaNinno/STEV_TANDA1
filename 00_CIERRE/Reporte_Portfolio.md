# Reporte de Portfolio — Proyecto STEV

**Documento:** `Reporte_Portfolio.md`
**Paquete:** TANDA1-STEV
**Versión del Codebook:** v1.0 (final)
**Fecha:** 2026-10-07
**Autoría:** Marina M. Ninno (diseño) + Claude (redacción)
**Público:** audiencia académica o profesional externa
**Estado:** versión para presentación

---

## 1. Resumen ejecutivo

**Proyecto:** Diseño, calibración y validación de un instrumento de evaluación epistémica tricapa para respuestas de modelos de lenguaje.

**Resultado:** Codebook STEV v1.0, con acuerdos del 95–100% en dos de sus tres capas.

**Historia:** 6 iteraciones del instrumento, 5 pilotos de confiabilidad, 67 decisiones documentadas, 60 registros finales.

**Qué demuestra este proyecto:**

- Capacidad de diseñar un instrumento desde cero.
- Capacidad de iterar sobre la base de datos empíricos.
- Capacidad de documentar cada decisión con trazabilidad.
- Capacidad de reconocer y documentar límites sin forzar soluciones artificiales.
- Capacidad de coordinar múltiples evaluadores independientes (humanos y LLMs).

**Por qué importa:** la evaluación de respuestas de modelos de lenguaje es un problema abierto. Este proyecto propone una arquitectura replicable que separa causa, manifestación e impacto, y que reconoce explícitamente lo que no puede resolver.

---

## 2. El problema

### 2.1 El contexto

Los modelos de lenguaje producen respuestas con distintos tipos de fallos epistémicos:

- **Falsedades** (dicen algo incorrecto).
- **Omisiones** (dicen algo verdadero pero incompleto).
- **Evasiones** (no responden).
- **Tautologías** (definen un término con el mismo término).
- **Errores de aplicación** (usan un concepto fuera de contexto).

### 2.2 El problema metodológico

Las taxonomías planas no capturan la relación causal entre estos fallos. Una misma respuesta puede tener múltiples fallos que se relacionan entre sí: una definición fallida produce una manifestación superficial, que produce un impacto cognitivo.

Clasificar todo en una sola dimensión mezcla causas, síntomas y efectos.

### 2.3 La pregunta de investigación

¿Es posible diseñar un instrumento que:

1. Separe causa, manifestación e impacto en capas distintas?
2. Sea aplicable por evaluadores independientes con alto acuerdo?
3. Reconozca sus propios límites sin forzar soluciones?

---

## 3. La solución

### 3.1 Arquitectura tricapa

El instrumento STEV separa la evaluación en tres capas:

| Capa | Pregunta | Tipo de capa |
|---|---|---|
| **L1** | ¿Cuál es la causa técnico-ontológica del fallo? | Interpretativa |
| **L2** | ¿Cómo se manifiesta el fallo en el texto? | Determinista |
| **L3** | ¿Qué impacto cognitivo genera? | Determinista |

Cada capa responde una pregunta distinta y no compite con las otras.

### 3.2 Componentes operativos

El Codebook v1.0 incluye:

- **Regla del Verbo:** el tipo de pregunta (definición, causal, mecanismo, evaluativa) orienta la búsqueda en L1.
- **Prueba de Algodón:** distingue falso de vacío antes de asignar código.
- **Árbol L1** con 4 pasos y 5 motivos de vacío.
- **Test 1 simple de L2** (revertido en v0.5 tras validación empírica).
- **Tres zonas de ambigüedad irreducible** en L2 (Z1, Z2, Z3) documentadas explícitamente.
- **Criterio L3** con regla dura "vacío por defecto".
- **Regla de mapeo** para Evaluación global (8 filas).

### 3.3 Catálogo

62 códigos organizados en 19 familias.

---

## 4. El proceso

### 4.1 Recorrido

| Fase | Producto |
|---|---|
| **1. Recolección cruda** | 80 evaluaciones (10 ejercicios × 8 evaluadores) |
| **2. Consolidación** | Análisis transversal del corpus |
| **3. Iteración (v0.1 → v0.6)** | 6 versiones del Codebook |
| **4. Pilotos (v0.3 → v0.6)** | 4 pilotos de confiabilidad |
| **5. Etapa 5** | Aplicación a 10 ejercicios × 6 evaluadores = 60 registros |
| **6. Codebook v1.0** | Versión final |

### 4.2 Método de calibración

El proyecto utilizó un método de calibración iterativo:

1. **Diseñar** una versión del Codebook.
2. **Aplicarla** a un conjunto de ejercicios con evaluadores independientes.
3. **Medir** el acuerdo entre evaluadores.
4. **Identificar** las zonas de baja convergencia.
5. **Iterar** el Codebook para resolver las ambigüedades.
6. **Repetir** hasta estabilizar.

Cada iteración fue documentada en el Decision Log con: fecha, versión, cambio, motivo, evidencia, resultado esperado.

### 4.3 Métricas de estabilidad

El instrumento se midió con:

- **Acuerdo bruto por capa:** porcentaje de evaluadores que coinciden.
- **Krippendorff's alpha:** acuerdo corregido por azar.
- **Uso de zonas:** porcentaje de evaluadores que reportan zonas de ambigüedad.
- **Fracturas residuales:** desacuerdos que se mantienen estables a través de los pilotos.

---

## 5. Los resultados

### 5.1 Métricas finales (Etapa 5, 60 registros)

| Capa | Acuerdo bruto | Alpha | Interpretación |
|---|---|---|---|
| L1 (¿vacío?) | 100% | — | Unanimidad |
| L1 (motivo) | 63.3% | 0.48 | Moderado |
| L2 | 95% | 0.85 | Casi perfecto |
| L3 | 100% | 1.00 | Unanimidad |

### 5.2 Lo que funciona

- **La arquitectura tricapa es estable.** Los evaluadores coinciden en que hay un fallo (L1), en cómo se manifiesta (L2), y en qué impacto tiene (L3).
- **La reversión del Test 1 funcionó.** El Test 1 simple recuperó el acuerdo del 95% en L2.
- **Las zonas de ambigüedad son útiles.** El 67% de los evaluadores reportaron zonas cuando se encontraron en ellas.
- **El formato está resuelto.** 0/60 errores de formato en etapa 5.

### 5.3 Lo que tiene límites

- **L1 (motivo) tiene 63.3% de acuerdo.** Clasificar el motivo específico del vacío es interpretativo.
- **A4 y A9 son los casos más ambiguos.** Preguntas evaluativas con respuestas evasivas admiten hasta 5 lecturas distintas.
- **Algunas fronteras son irreducibles.** Z1 (A1.2 ↔ A1.4), Z2 (A1.4 ↔ E2.1), Z3 (A1.2 ↔ E2.1) no se resuelven con más criterios.

---

## 6. Lo que demuestra este proyecto

### 6.1 Capacidades demostradas

| Habilidad | Evidencia |
|---|---|
| **Diseño de instrumento** | Codebook con arquitectura tricapa, 62 códigos, 19 familias |
| **Iteración empírica** | 6 versiones del Codebook, cada una basada en datos |
| **Documentación** | 67 decisiones trazadas con fecha, motivo y evidencia |
| **Coordinación** | 6 evaluadores externos (LLMs) en 5 rondas |
| **Análisis cuantitativo** | Acuerdo bruto, alpha, matrices de confusión |
| **Análisis cualitativo** | Identificación de fracturas interpretativas, zonas de ambigüedad |
| **Rigor metodológico** | Reconocimiento de límites sin forzar soluciones |
| **Transparencia** | Data Availability Statement, Decision Log, script de cálculo |

### 6.2 Por qué es un aporte

1. **Propone una arquitectura replicable** que separa causa, manifestación e impacto. Otros proyectos pueden adoptarla o adaptarla.
2. **Demuestra un método de calibración iterativo** que documenta cada decisión y acepta límites. Es una metodología transferible.
3. **Produce un instrumento auditable** que cualquier tercero puede reproducir. El kit, el script y los datos están disponibles.
4. **Reconoce explícitamente lo que no puede resolver.** Esto es rigor metodológico, no debilidad.

---

## 7. Artefactos del proyecto

### 7.1 Documentos principales

| Documento | Rol | Audiencia |
|---|---|---|
| Codebook_STEV_v1.0.md | Instrumento final | Metodólogos |
| DecisionLog_STEV.md | Registro de 67 decisiones | Auditores |
| Proyecto_STEV_Cierre.md | Documento de cierre | Dirección |
| DataAvailability_STEV.md | Declaración de disponibilidad | Investigadores |
| Etapa5_resultados.md | Resultados finales | Analistas |
| Reporte_Portfolio.md | Este documento | Portfolio |

### 7.2 Datasets

- `stev_tanda1_v0.csv`: corpus original (80 registros).
- `stev_tanda1_v0.3.csv`: recodificación v0.3.
- `Etapa5_consolidado.csv`: corpus final (60 registros).

### 7.3 Herramientas

- `calcular_alpha.py`: script de cálculo de Krippendorff's alpha.
- `Kit_Evaluacion_STEV_v0.6_Etapa5.md`: kit de evaluación final.

---

## 8. Lecciones aprendidas

### 8.1 Sobre el diseño de instrumentos

- **Los tests deterministas inflan el alpha.** Un alpha = 1.0 con tests deterministas no es un logro. La consistencia interna del manual no es confiabilidad inter-evaluador.
- **Los árboles de decisión son más efectivos que las tablas de códigos.** El árbol L1 redujo la dispersión significativamente.
- **Un test demasiado estricto puede sobrecodificar.** El Test 1 v0.4 colapsó 6 de 10 ejercicios en A1.2. La reversión a v0.3 recuperó el acuerdo.

### 8.2 Sobre la validación

- **Los pilotos deben medir lo que se pretende medir.** Los tres primeros pilotos midieron consistencia interna, no confiabilidad inter-evaluador.
- **Iterar tiene un techo.** Después de v0.6, iterar más no mejora las métricas.
- **El rediseño es parte del proceso.** Los pilotos refinaron el Codebook.

### 8.3 Sobre la auditoría

- **Documentar errores es tan importante como documentar aciertos.** El Decision Log registra 67 decisiones, incluyendo correcciones.
- **Los hallazgos negativos son hallazgos.** La sobrecodificación de A1.2 informó v0.5.
- **Los límites del instrumento son parte del instrumento.** Documentarlos es rigor.

---

## 9. Aplicaciones futuras

### 9.1 Uso directo

- **Evaluación de respuestas de LLMs** en dominios específicos.
- **Auditoría de calidad epistémica** en producción de contenido.
- **Investigación sobre sesgos** de modelos de lenguaje.
- **Herramienta de fine-tuning** (usar los vectores STEV como señal de corrección).

### 9.2 Extensiones

- **Aplicar a corpus más grandes** (100+ ejercicios).
- **Aplicar a dominios no cubiertos** (matemática, derecho, medicina).
- **Desarrollar un pipeline automático** que aplique el Codebook vía LLM.
- **Publicar el instrumento** en revista de metodología o NLP.

---

## 10. Cómo citar este proyecto

**Versión resumida:**

> Marina M. Ninno. (2026). *Protocolo STEV: evaluación epistémica tricapa de respuestas de modelos de lenguaje*. Paquete TANDA1-STEV. Codebook v1.0. Corpus: 10 ejercicios × 6 evaluadores externos + referencia humana.

**Versión extendida:**

> Marina M. Ninno. (2026). *Protocolo STEV: diseño, calibración y validación de un sistema de evaluación epistémica para modelos de lenguaje*. Paquete TANDA1-STEV. 6 iteraciones del Codebook (v0.1 a v0.6). Codebook v1.0 final. Decision Log v1.0 (67 decisiones). Corpus final: 60 registros.

---

## 11. Contacto y recursos

**Repositorio:** `STEV_TANDA1/`

**Documentación:** ver `Proyecto_STEV_Cierre.md`

**Data Availability:** ver `DataAvailability_STEV.md`

**Decision Log:** ver `DecisionLog_STEV.md`

---

## 12. Estado del documento

| Sección | Estado |
|---|---|
| 1. Resumen ejecutivo | ✅ |
| 2. El problema | ✅ |
| 3. La solución | ✅ |
| 4. El proceso | ✅ |
| 5. Los resultados | ✅ |
| 6. Lo que demuestra | ✅ |
| 7. Artefactos | ✅ |
| 8. Lecciones aprendidas | ✅ |
| 9. Aplicaciones futuras | ✅ |
| 10. Cómo citar | ✅ |
| 11. Contacto y recursos | ✅ |
| 12. Estado | ✅ |

---

## 13. Próximos pasos

Con el Reporte de portfolio completo:

1. **Paso 4 — Repositorio final** con todos los documentos organizados.