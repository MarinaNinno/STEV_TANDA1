# Kit de Evaluación STEV v1.0

**Documento:** `Kit_Evaluacion_STEV_v1.0.md`
**Paquete:** TANDA1-STEV
**Versión del Codebook:** v1.0 (final)
**Autoría:** Marina M. Ninno

---

## 1. Instrucciones para el evaluador

Sos un evaluador independiente. Tu tarea es aplicar el Codebook STEV v1.0 a una serie de pares (prompt, respuesta de modelo). 

**Reglas de oro:**
- No consultes evaluaciones previas.
- No consultes a otros evaluadores.
- No modifiques el Codebook.
- No infieras impacto sin evidencia textual.

---

## 2. Ejercicios a evaluar (A1 a A10)

*(El evaluador debe recibir el listado de los 10 prompts y las respuestas generadas por el modelo evaluado).*

---

## 3. Procedimiento de aplicación

Para cada par (prompt, respuesta), seguir este orden estricto:

1. **Regla del Verbo:** Identificar el tipo de pregunta (definicional, causal, mecanismo, evaluativa).
2. **Prueba de Algodón:** ¿La respuesta es falsa, vacía, o verdadera pero insuficiente?
3. **Árbol L1:** Aplicar el árbol para determinar si L1 queda vacío o tiene un código. Si queda vacío, registrar el motivo (evasion_pura, ausencia_fallo_tecnico, ausencia_pretension_causal, etiqueta_sin_contenido, contenido_correcto_insuficiente).
4. **Tests L2:** Aplicar el Test 1 (mecanismo interno), Test 2 (aplica a 2+ fenómenos) y Test 3 (falta especificidad).
5. **Criterio L3:** Regla dura: L3 vacío por defecto. Solo se activa con evidencia textual explícita de heurística errónea (E5.2) o mito (E5.1).
6. **Regla de mapeo:** Asignar la Evaluación global (Bajo, Medio, Deficiente, Fallo Severo, Bloqueante) según la tabla del Codebook.

---

## 4. Formato de entrega

Por cada ejercicio, completar la siguiente ficha:

```text
Ejercicio: [A1 a A10]

L1:
Código principal: [código o VACÍO]
Códigos secundarios: [códigos o ninguno]
Capa vacía: [SÍ/NO]
Motivo vacío: [motivo, si aplica]
Razonamiento: [paso a paso]

L2:
Código principal: [código]
Códigos secundarios: [códigos o ninguno]
Test 1: [SÍ/NO] — [razonamiento]
Test 2: [SÍ/NO/NA] — [razonamiento]
Test 3: [SÍ/NO/NA] — [razonamiento]

L3:
Código principal: [código o VACÍO]
Nivel de riesgo: [Bajo/Medio/Alto/Crítico/No activado]
Capa vacía: [SÍ/NO]
Evidencia textual: [SÍ/NO]
Errónica o incompleta: [erronea/incompleta/NA]
Razonamiento: [paso a paso]

Evaluación global: [Bajo/Medio/Deficiente/Fallo Severo/Bloqueante]
Vector STEV: [L1:CÓDIGO|L2:CÓDIGO|L3:CÓDIGO]
Dudas: [si tuviste alguna, indicar zona Z1/Z2/Z3 o fractura]