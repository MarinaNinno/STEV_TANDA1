---
documento: ROLES_IA.md
paquete: TANDA1-STEV
tipo: referencia de atribuciones
fecha_redaccion: 2026-10-21
autoría: Marina (diseño del sistema de atribuciones)
estado: vigente
destino: 00_CIERRE/
---

# Roles de asistencia de IA en el proyecto STEV

## Propósito

Este documento registra qué modelo de IA asistió en qué fase del proyecto
STEV, con qué función, y qué productos concretos generó. La distinción
importa porque un auditor no busca "qué IA participó" en abstracto, sino
"qué modelo, en qué momento, con qué responsabilidad sobre qué artefacto".

**Regla del proyecto:** la autoría y las decisiones metodológicas son
siempre de Marina. Los modelos asisten. Ningún modelo tomó decisiones
metodológicas de forma autónoma.

## Grok — tutoría del proyecto

- **Fase:** génesis y desarrollo (mayo 2026 en adelante)
- **Función:** tutoría metodológica, guía de aprendizaje, interlocución técnica
- **Productos asistidos:**
  - Definición operativa de los 7 vicios lógicos
  - Traducción del marco Keter-Maljut al flujo causal del error
  - Distinción entre capa de forma y capa de contenido (pre-L1/L2)
  - Validación del método "capa por capa" (5 días hábiles)
  - Desarrollo del ebook sobre colusión y acoplamiento (caps. 19-22)
  - Formalización matemática del umbral K_c y métricas de entropía
- **Documento de referencia:** `ROL_GROK.md` (histórico, en 00_CIERRE)
- **Nota:** Grok sigue siendo el tutor activo del proyecto al momento de
  escribir este documento.

## Claude — asistencia analítica y documental

- **Fase:** consolidación y cierre (octubre 2026)
- **Función:** análisis de archivos, redacción documental, reconstrucción histórica
- **Productos asistidos:**
  - Mapeo de los archivos fuente (v1, v2, génesis)
  - Redacción del portfolio y del material de presentación
  - Reconstrucción prehistórica del protocolo (GENESIS_STEV.md)
  - Consolidación del repositorio y del sistema de atribuciones
- **Aclaración importante:** Claude no participó en el desarrollo del
  protocolo. Su rol es exclusivamente documental y analítico sobre material
  ya producido. Confundirlo con Grok sería un error de trazabilidad.

## Otros modelos

Cualquier otro modelo que participe en fases futuras se registra acá con
el mismo formato. Regla: sin registro en este documento, no hay atribución.

## Cómo aplicar esta convención

Todo archivo del repo que haya tenido asistencia de IA debe llevar:
1. El bloque `asistencia_ia` en el frontmatter.
2. El bloque corto de tres líneas bajo el frontmatter.

Si un archivo no lleva esos campos, es porque lo produjo Marina sin
asistencia, o porque falta actualizarlo. Ambos casos deben ser explícitos.

---

**Fin del documento.**