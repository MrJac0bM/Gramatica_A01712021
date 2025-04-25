# E2 Generación y Limpieza de una Gramática Libre de Contexto Restringida

## Descripción

Las gramáticas son fundamentales en los métodos computacionales para el procesamiento del lenguaje, ya que proporcionan una base formal para comprender, generar y manipular datos lingüísticos. En este proyecto, nos enfocamos en el **noruego** y construimos una gramática que acepta palabras y estructuras específicas de este idioma. Las reglas incluyen:

- **Oraciones principales**: Frase nominal + Frase verbal.
- **Frases nominales**: Construidas con sustantivos, determinantes y pronombres.
- **Frases verbales**: Incluyen verbos, verbos con preposiciones y adverbios.
- **Oraciones subordinadas**: Comienzan con una conjunción seguida de una frase verbal + frase nominal y terminan con una oración principal.
- **Oraciones separadas por comas/conjunciones**: Conjuntos de sustantivos y verbos separados por comas u oraciones principales unidas por conjunciones.

> **Nota**: Todas las oraciones deben terminar con un signo de puntuación (p.ej., `.`).

Para implementar esto, utilizamos un analizador sintáctico **LL(1)**, que procesa la entrada de izquierda a derecha con un token de anticipación, evitando retrocesos ([GeeksforGeeks, 2023](https://www.geeksforgeeks.org/)).


## Modelos de la Gramática

### 1. Gramática Inicial (Reconocimiento del Idioma)

En esta fase, definí símbolos no terminales abstractos para representar estructuras noruegas, como `Setning` (oración), `HovedSetning` (oración principal), y `Subjekt` (sujeto). Los terminales incluyen palabras específicas como `"jeg"`, `"spiser"`, y signos de puntuación (`"."`, `","`). La gramática cubre:

- **Oraciones principales**: `Subjekt` + `Predikat`.
- **Subordinadas**: Inician con conjunción (`Konj`) + `Setning`.
- **Listas coordinadas**: Uso de `Konj` y comas (`Skilletegn`).

**Imagen 1**: Diagrama de la Gramática Inicial  
_(Jerarquía de reglas: `S → Setning Setning_opt`, `Setning → HovedSetning Skilletegn_opt`, `HovedSetning → Subjekt Predikat`)_


### 2. Eliminación de Ambigüedad

La ambigüedad se resolvió reestructurando reglas con múltiples interpretaciones. Por ejemplo:

**Regla original ambigua:**

`EnkelSubjekt → Pronomen | Art Substantiv | Art AdjE Substantiv`  
Permitía interpretaciones conflictivas para frases como `"den gamle mann"` (el hombre viejo).

**Solución:** Introducir no terminales intermedios (`AdjE_opt`) y priorizar derivaciones únicas.

**Imagen 2**: Gramática sin Ambigüedad  
_(Flujo de `EnkelSubjekt` con reglas jerárquicas: `EnkelSubjekt → Art AdjE Substantiv | Art Substantiv`)_

### 3. Eliminación de Recursión Izquierda

La gramática no presentaba recursión izquierda, ya que reglas como:

`Subjekt_opt → Konj Subjekt Subjekt_opt | ε`  
usan recursión derecha, lo cual garantiza compatibilidad con **LL(1)** y evita la aparición de recursión izquierda. En caso de haber existido recursión izquierda (p.ej., `A → Aα`), la habría transformado utilizando no terminales auxiliares, siguiendo la forma:  
`A → βA'`  
`A' → αA' | ε`

**Imagen 3**: Estructura de Recursión Derecha  
_(Diagrama de `Subjekt_opt` mostrando derivaciones anidadas sin bucles infinitos)_

# Implementacion 
### Aqui se mostrara la implementación de la gramatica final 

