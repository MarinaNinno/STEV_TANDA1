# Codebook STEV v1.0

**Documento:** `Codebook_STEV_v1.0.md`
**Paquete:** TANDA1-STEV
**Versión anterior:** v0.6
**Fecha:** 2026-10-07
**Autoría:** Marina M. Ninno (diseño) + Claude (redacción)
**Estado:** versión final del instrumento

---

## 1. Arquitectura tricapa

El instrumento evalúa las respuestas de modelos de lenguaje separando tres dimensiones:

| Capa | Pregunta | Tipo |
|---|---|---|
| **L1** | ¿Cuál es la causa técnico-ontológica del fallo? | Interpretativa |
| **L2** | ¿Cómo se manifiesta el fallo en el texto? | Determinista |
| **L3** | ¿Qué impacto cognitivo genera? | Determinista |

Cada capa responde una pregunta distinta y no compite con las otras.

---

## 2. Componentes operativos

### 2.1 Regla del Verbo
El tipo de pregunta orienta la búsqueda inicial en L1:
- "¿Qué es X?" (definicional) → D1.x, T1.x.
- "¿Por qué X?" (causal) → F1.x, C1.x.
- "¿Cómo funciona X?" (mecanismo) → F1.x, C1.x.
- "¿Es X bueno/malo?" (evaluativa) → A4, F1, A1.

### 2.2 Prueba de Algodón
Distingue falso de vacío antes de asignar código:
- **Falso** (dice algo incorrecto) → familia F, C, I, D.
- **Vacío** (no dice nada, o dice algo incompleto) → A8.2 o vacío en L1.
- **Verdadero pero insuficiente** → evaluar L1.

### 2.3 Árbol L1
Para determinar si L1 está vacío o tiene un código de causa:

```text
¿Intenta responder el tipo de pregunta?
NO → evasion_pura
SÍ → ¿Hay fallo técnico identificable?
     NO → ausencia_fallo_tecnico
     SÍ → ¿La respuesta describe sin pretensión causal?
          SÍ → ausencia_pretension_causal
          NO → ¿La expresión clave es reemplazable sin pérdida?
               SÍ → etiqueta_sin_contenido
               NO → contenido_correcto_insuficiente