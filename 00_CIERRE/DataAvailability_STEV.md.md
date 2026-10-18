# Data Availability Statement — Proyecto STEV

**Documento:** `DataAvailability_STEV.md`
**Paquete:** TANDA1-STEV
**Versión del Codebook:** v1.0 (final)
**Fecha:** 2026-10-07
**Autoría:** Marina M. Ninno (diseño) + Claude (redacción)
**Estado:** declaración final de disponibilidad

---

## 1. Propósito

Este documento declara qué datos fueron producidos en el marco del proyecto STEV, cómo están estructurados, cómo se accede a ellos y bajo qué condiciones pueden ser usados, citados o auditados.

Su función es cumplir con el principio de **transparencia y auditabilidad** que el proyecto asume desde el diseño.

Esta es la **versión final** (v1.0), actualizada con los datos de etapa 5.

---

## 2. Inventario de datos

### 2.1 Datos primarios

| Archivo | Formato | Contenido | Estado |
|---|---|---|---|
| stev_tanda1_v0.csv | CSV | Corpus original: 80 evaluaciones (10 ejercicios × 8 evaluadores) | ✅ |
| stev_tanda1_v0.json | JSON | Fichas originales con justificaciones | ✅ |
| stev_tanda1_v0.3.csv | CSV | Recodificación con Codebook v0.3 | ✅ |
| stev_tanda1_v0.3.json | JSON | Recodificación con justificaciones | ✅ |
| Etapa5_consolidado.csv | CSV | **Corpus final: 60 registros** (10 ejercicios × 6 evaluadores externos) | ✅ |
| Etapa5_consolidado.json | JSON | **Corpus final con justificaciones completas** | ✅ |

### 2.2 Documentos metodológicos

| Archivo | Formato | Contenido | Estado |
|---|---|---|---|
| Codebook_STEV_v0.1.md | Markdown | Primera iteración | ✅ |
| Codebook_STEV_v0.2.md | Markdown | Segunda iteración | ✅ |
| Codebook_STEV_v0.3.md | Markdown | Tercera iteración | ✅ |
| Codebook_STEV_v0.4.md | Markdown | Cuarta iteración | ✅ |
| Codebook_STEV_v0.5.md | Markdown | Quinta iteración | ✅ |
| Codebook_STEV_v0.6.md | Markdown | Sexta iteración | ✅ |
| Codebook_STEV_v1.0.md | Markdown | **Versión final** | ✅ |
| DecisionLog_STEV.md | Markdown | **Registro de 67 decisiones** | ✅ |
| Proyecto_STEV_Cierre.md | Markdown | Documento de cierre del proyecto | ✅ |
| DataAvailability_STEV.md | Markdown | Este documento | ✅ |
| Protocolo_STEV_tricapa.md | Markdown | Descripción del protocolo | ✅ |
| Nosografia_STEV_v0.md | Markdown | Catálogo: 62 códigos, 19 familias | ✅ |

### 2.3 Análisis derivados

| Archivo | Formato | Contenido | Estado |
|---|---|---|---|
| Capa2_AnalisisTransversal.md | Markdown | Análisis transversal del corpus original | ✅ |
| Piloto_v0.1_resultados.md | Markdown | Resultados del primer piloto | ✅ |
| Piloto_v0.2_resultados.md | Markdown | Resultados del segundo piloto | ✅ |
| Piloto_v0.3_resultados.md | Markdown | Resultados del tercer piloto | ✅ |
| Piloto_v0.3_rediseno_desacuerdos.md | Markdown | Análisis de desacuerdos del piloto rediseñado | ✅ |
| Piloto_v0.3_rediseno_desacuerdos_addendum.md | Markdown | Addendum con criterio v0.4 | ✅ |
| Piloto_v0.4_resultados.md | Markdown | Resultados del piloto v0.4 | ✅ |
| Piloto_v0.5_resultados.md | Markdown | Resultados del piloto v0.5 | ✅ |
| Piloto_v0.6_resultados.md | Markdown | Resultados del piloto v0.6 | ✅ |
| Etapa5_resultados.md | Markdown | **Resultados finales de etapa 5** | ✅ |

### 2.4 Material para evaluadores externos

| Archivo | Formato | Contenido | Estado |
|---|---|---|---|
| Kit_Evaluacion_STEV_v0.3.md | Markdown | Kit v0.3 (histórico) | ✅ |
| Kit_Evaluacion_STEV_v0.4.md | Markdown | Kit v0.4 (histórico) | ✅ |
| Kit_Evaluacion_STEV_v0.5.md | Markdown | Kit v0.5 (histórico) | ✅ |
| Kit_Evaluacion_STEV_v0.6.md | Markdown | Kit v0.6 (histórico) | ✅ |
| Kit_Evaluacion_STEV_v0.6_Etapa5.md | Markdown | **Kit final para 10 ejercicios** | ✅ |
| Recoleccion_externa_template.csv | CSV | Plantilla vacía para evaluadores | ✅ |
| calcular_alpha.py | Python | Script de cálculo de Krippendorff's alpha | ✅ |

### 2.5 Documentos de portfolio

| Archivo | Formato | Contenido | Estado |
|---|---|---|---|
| Reporte_Portfolio.md | Markdown | Reporte adaptado para presentación | ✅ |

---

## 3. Estructura de identificadores

### 3.1 Identificador de caso

Cada evaluación tiene un identificador único con el formato:

```
CASO-YYYY-NNN
```

Donde `YYYY` es el año y `NNN` es un número correlativo.

**Mapeo del corpus original:**

| Rango | Ejercicio | Evaluadores |
|---|---|---|
| CASO-2026-001 a 008 | A1 | 7 modelos + Marina |
| CASO-2026-009 a 016 | A2 | 7 modelos + Marina |
| ... | ... | ... |
| CASO-2026-073 a 080 | A10 | 7 modelos + Marina |

**Mapeo de etapa 5:**

| Rango | Ejercicio | Evaluadores |
|---|---|---|
| E5-2026-001 a 006 | A1 | 6 externos |
| E5-2026-007 a 012 | A2 | 6 externos |
| ... | ... | ... |
| E5-2026-055 a 060 | A10 | 6 externos |

### 3.2 Identificador de paquete

```
TANDA1-STEV
```

Todos los registros del corpus actual pertenecen a este paquete.

### 3.3 Vector STEV

Representación canónica del diagnóstico:

```
[L1:CÓDIGO|L2:CÓDIGO|L3:CÓDIGO]
```

Ejemplo:

```
[L1:|L2:A1.2|L3:]
```

Si una capa está vacía, se deja en blanco.

Si hay múltiples códigos en una capa:

```
[L1:D1.2+T1.4|L2:A1.2|L3:]
```

---

## 4. Estructura del dataset

### 4.1 CSV — columnas

**Corpus final (Etapa 5):**

| Columna | Tipo | Descripción |
|---|---|---|
| id_caso | string | Identificador único |
| id_paquete | string | Identificador del lote |
| timestamp | ISO 8601 | Fecha de evaluación |
| ejercicio | string | A1 a A10 |
| dominio | string | Área disciplinar |
| evaluador | string | Nombre del evaluador |
| tipo_evaluador | enum | modelo / referencia |
| l1_codigo_principal | string o vacío | Código L1 (generalmente VACÍO) |
| l1_codigos_secundarios | string | Códigos adicionales |
| l1_capa_vacia | boolean | TRUE / FALSE |
| l1_motivo_vacio | enum | Motivo si L1 está vacío |
| l1_codigos_no_homologados | string | Códigos fuera del catálogo |
| l2_codigo_principal | string | Código L2 |
| l2_codigos_secundarios | string | Códigos adicionales |
| l3_codigo_principal | string o vacío | Código L3 |
| l3_nivel_riesgo | enum | Bajo / Medio / Alto / Crítico / No activado |
| l3_capa_vacia | boolean | TRUE / FALSE |
| evaluacion_global | enum | Bajo / Medio / Deficiente / Fallo Severo / Bloqueante |
| vector_stev | string | Vector canónico |
| dudas | string | Zonas reportadas |

### 4.2 JSON — esquema

El JSON `Etapa5_consolidado.json` sigue el esquema:

```json
{
  "id_caso": "string",
  "id_paquete": "string",
  "timestamp": "ISO 8601",
  "ejercicio": "string",
  "dominio": "string",
  "prompt_entrada": "string",
  "salida_modelo": "string",
  "evaluador": "string",
  "tipo_evaluador": "string",
  "capa_1_causa": {
    "codigo_principal": "string o null",
    "codigos_secundarios": ["string"],
    "justificacion": "string",
    "capa_vacia": "boolean",
    "motivo_vacio": "string o null"
  },
  "capa_2_manifestacion": {
    "codigo_principal": "string",
    "codigos_secundarios": ["string"],
    "justificacion": "string"
  },
  "capa_3_impacto": {
    "codigo_principal": "string o null",
    "nivel_riesgo": "string",
    "justificacion": "string",
    "capa_vacia": "boolean"
  },
  "evaluacion_global": "string",
  "vector_stev": "string",
  "dudas": "string"
}
```

### 4.3 Claves de cruce

| Clave | Uso |
|---|---|
| id_caso | Clave primaria |
| ejercicio + evaluador | Clave compuesta alternativa |
| vector_stev | Cruce rápido con análisis transversal |
| l1_motivo_vacio | Agregación por motivo |
| l2_codigo_principal | Agregación por manifestación |
| l3_codigo_principal | Agregación por impacto |

---

## 5. Métricas derivadas

A partir del dataset se pueden calcular:

| Métrica | Fórmula | Uso |
|---|---|---|
| **Acuerdo bruto L1 (¿vacío?)** | casos con L1 vacío / total | Estabilidad de la capa |
| **Acuerdo bruto L1 (motivo)** | casos con motivo de moda / total | Estabilidad fina |
| **Acuerdo bruto L2** | casos con código de moda / total | Estabilidad de la manifestación |
| **Acuerdo bruto L3** | casos con código de moda / total | Estabilidad del impacto |
| **Krippendorff's alpha** | ver script calcular_alpha.py | Acuerdo corregido por azar |
| **Distribución de motivos de vacío** | frecuencia de cada motivo | Análisis de patrones |
| **Frecuencia de códigos por capa** | conteo por código | Análisis de concentración |
| **Uso de zonas (Z1/Z2/Z3)** | casos con zona reportada / total | Validación del kit |
| **Fracturas residuales** | casos con fractura reportada / total | Documentación de límites |

---

## 6. Disponibilidad

### 6.1 Acceso

El dataset completo está disponible en:

- **Repositorio local:** carpeta `STEV_TANDA1/`
- **Formato de entrega:** CSV + JSON + Markdown
- **Licencia:** documentos y datos bajo CC BY 4.0; código bajo MIT. Ver `LICENSE-CONTENT.md` y `LICENSE-CODE.md`.

### 6.2 Condiciones de uso

El dataset puede ser usado para:

- **Auditoría metodológica** del protocolo STEV.
- **Replicación** de los análisis presentados.
- **Extensión** a nuevos corpus con el mismo protocolo.
- **Investigación** sobre evaluación de LLMs.
- **Docencia** en metodología de evaluación.

**Requisitos:**

- **Citación** del proyecto y de la autora.
- **No modificación** de los datos originales sin documentar.
- **Atribución** de cualquier análisis derivado.

### 6.3 Restricciones

- No se publican los prompts completos de las evaluaciones externas (privacidad de participantes).
- No se publican evaluaciones de terceros sin consentimiento.
- Los datos derivados de las evaluaciones externas se publican anonimizados.

---

## 7. Cómo citar

**Versión resumida:**

> Marina M. Ninno. (2026). *Protocolo STEV: evaluación epistémica tricapa de respuestas de modelos de lenguaje*. Paquete TANDA1-STEV. Codebook v1.0. Corpus: 10 ejercicios × 6 evaluadores externos + referencia humana.

**Versión extendida (académica):**

> Marina M. Ninno. (2026). *Protocolo STEV: diseño, calibración y validación de un sistema de evaluación epistémica para modelos de lenguaje*. Paquete TANDA1-STEV (10 ejercicios, 6 evaluadores externos + 1 referencia humana). 6 iteraciones del Codebook (v0.1 a v0.6). Codebook v1.0 final. Decision Log v1.0 (67 decisiones). Corpus final: 60 registros.

---

## 8. Trazabilidad

### 8.1 Ciclo de vida del dato

| Etapa | Producto | Estado |
|---|---|---|
| 1. Recolección cruda | 80 evaluaciones en v0 | ✅ |
| 2. Consolidación | Documento Capa 2 + CSV/JSON v0 | ✅ |
| 3. Homologación | Codebook v0.1 | ✅ |
| 4. Calibración | Codebook v0.2, v0.3, v0.4, v0.5, v0.6 | ✅ |
| 5. Recodificación | Dataset v0.3 | ✅ |
| 6. Pilotos de confiabilidad | 5 pilotos (v0.3 a etapa 5) | ✅ |
| 7. Documentación | Decision Log (67 decisiones) | ✅ |
| 8. Publicación | Data Availability Statement | ✅ |
| 9. Validación final | Codebook v1.0 | ✅ |

### 8.2 Versionado del dataset

| Versión | Fecha | Descripción | Estado |
|---|---|---|---|
| v0 | (previa) | Recolección cruda | ✅ |
| v0.1 | 2026-09-29 | Primera homologación | ✅ |
| v0.2 | 2026-09-29 | Ajuste de fronteras | ✅ |
| v0.3 | 2026-09-29 | Recodificación completa con tests v0.3 | ✅ |
| v0.4 | 2026-10-02 | Recodificación con ajuste 6 | ✅ |
| v0.5 | 2026-10-06 | Recodificación con reversión del Test 1 | ✅ |
| v0.6 | 2026-10-06 | Recodificación con fracturas documentadas | ✅ |
| **Etapa 5** | **2026-10-07** | **Corpus final: 60 registros** | ✅ **vigente** |
| v1.0 | 2026-10-07 | Declaración de versión final | ✅ |

### 8.3 Versionado del Codebook

| Versión | Fecha | Iteración |
|---|---|---|
| v0.1 | 2026-09-29 | Homologación inicial |
| v0.2 | 2026-09-29 | Árbol L1 explícito |
| v0.3 | 2026-09-29 | Test 1 reformulado |
| v0.4 | 2026-10-02 | Definiciones operacionales + Test 1 en 3 casos |
| v0.5 | 2026-10-06 | Reversión del Test 1 + zonas de ambigüedad |
| v0.6 | 2026-10-06 | Fila faltante + fractura A6 documentada |
| **v1.0** | **2026-10-07** | **Versión final** |

---

## 9. Reproducibilidad

Para reproducir los análisis del proyecto, se requiere:

### 9.1 Dataset

- Descargar `Etapa5_consolidado.csv` o `Etapa5_consolidado.json`.

### 9.2 Documentos metodológicos

- Leer `Codebook_STEV_v1.0.md` para entender las reglas de codificación.
- Leer `DecisionLog_STEV.md` para entender las decisiones estructurales.
- Leer `Proyecto_STEV_Cierre.md` para entender el recorrido completo.

### 9.3 Scripts

- Ejecutar `calcular_alpha.py` para replicar el cálculo de Krippendorff's alpha.

### 9.4 Pasos de reproducción

1. Cargar el dataset en Python, R o herramienta equivalente.
2. Agrupar por ejercicio y capa.
3. Calcular acuerdos brutos.
4. Calcular Krippendorff's alpha.
5. Comparar con los resultados de `Etapa5_resultados.md`.

---

## 10. Limitaciones de disponibilidad

### 10.1 Datos no disponibles

- **Prompts completos de evaluaciones externas:** se publican anonimizados.
- **Evaluaciones individuales de Marina:** disponibles como referencia, no como parte del cálculo de alpha.
- **Correcciones intermedias durante el proceso:** documentadas en el Decision Log, no en el dataset.

### 10.2 Datos sensibles

No hay datos personales sensibles. Los evaluadores son modelos de lenguaje o la autora del proyecto.

### 10.3 Datos con restricción temporal

No hay restricciones temporales. El dataset completo está disponible desde 2026-10-07.

---

## 11. Compatibilidad

### 11.1 Herramientas

El dataset es compatible con:

- Python (pandas, numpy)
- R (tidyverse, irr)
- Excel / Google Sheets
- SQL (importable)
- Herramientas de análisis de confiabilidad inter-evaluador

### 11.2 Formatos de exportación

- CSV
- JSON
- Excel (bajo demanda)
- SQL dump (bajo demanda)

---

## 12. Estado del documento

| Sección | Estado |
|---|---|
| 1. Propósito | ✅ |
| 2. Inventario | ✅ |
| 3. Identificadores | ✅ |
| 4. Estructura del dataset | ✅ |
| 5. Métricas derivadas | ✅ |
| 6. Disponibilidad | ✅ |
| 7. Cómo citar | ✅ |
| 8. Trazabilidad | ✅ |
| 9. Reproducibilidad | ✅ |
| 10. Limitaciones | ✅ |
| 11. Compatibilidad | ✅ |
| 12. Estado | ✅ |

---

## 13. Próximos pasos

Con el Data Availability Statement actualizado:

1. **Paso 3 — Reporte de portfolio** adaptado para presentación.
2. **Paso 4 — Repositorio final** con todos los documentos organizados.