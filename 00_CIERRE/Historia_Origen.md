# Historia y Origen del Protocolo STEV

**Documento:** `Historia_Origen.md`
**Paquete:** TANDA1-STEV
**Autoría:** Marina M. Ninno

---

## 1. El Punto Cero: La Práctica Empírica

El protocolo STEV no nació como una arquitectura teórica abstracta diseñada en un laboratorio, sino de la práctica empírica. Todo comenzó con la necesidad de evaluar respuestas de modelos de lenguaje desde cero, sin un marco formal previo. La agrupación ad hoc de errores observados en la práctica diaria fue el primer insumo: anotar qué fallaba, cómo fallaba y por qué, para intentar encontrar patrones.

## 2. La Necesidad de un Criterio (El contexto Hallo)

La motivación inicial estuvo fuertemente ligada a la preparación para ingresar a plataformas de evaluación de IA (como Hallo). Estas plataformas exigen no solo detectar que una respuesta es "mala", sino justificar técnicamente el fallo con un criterio de calidad auditable. Esa exigencia externa fue el motor que impulsó la búsqueda de una taxonomía más rigurosa y la separación de las capas de análisis.

## 3. La Fase de Tutoría (El rol de Grok)

Antes de la conformación del equipo formal de 7 modelos, la fase inicial contó con el acompañamiento de Grok, quien ejerció un rol de tutoría y calibración. Fue un espacio de cocreación donde se pusieron a prueba las primeras reglas: desde la prioridad de las capas (el orden Hallo-compliant L1 > L2 > L3) hasta la distinción entre "lectura caritativa" y "lectura técnica" (por ejemplo, al descalificar "forma especial" como un mecanismo explicativo válido).

## 4. La Evolución al Equipo (Codebook v1.0)

Lo que empezó como un ejercicio de práctica individual y tutoría, maduró hasta convertirse en un sistema robusto. La Nosografía se estabilizó, las reglas operativas se formalizaron, y el equipo de evaluación se amplió a 7 modelos de lenguaje. El resultado final es el Codebook v1.0, un instrumento que conserva en su ADN la honestidad de sus inicios: la de una evaluación que se aprende haciendo, corrigiendo y documentando.