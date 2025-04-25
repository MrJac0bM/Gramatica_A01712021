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


## Modelo Matemático

El análisis y la implementación de la gramática se basan en conceptos fundamentales de la teoría de lenguajes formales y autómatas. La gramática que hemos construido sigue los principios de una **gramática libre de contexto** (CFG), que es una de las clases más poderosas de gramáticas, según la jerarquía de Chomsky. Esta jerarquía se clasifica en cuatro niveles:

1. **Lenguajes Regulares (Nivel 3)**: Generados por gramáticas regulares.
2. **Lenguajes Libres de Contexto (Nivel 2)**: Generados por gramáticas libres de contexto, como la que estamos usando en este proyecto.
3. **Lenguajes Sensibles al Contexto (Nivel 1)**: Generados por gramáticas sensibles al contexto.
4. **Lenguajes Recursivamente Enumerables (Nivel 0)**: Generados por gramáticas Turing-completas.

En nuestro caso, estamos utilizando una **gramática libre de contexto** (Chomsky Nivel 2) para modelar el idioma noruego, lo cual implica que nuestras reglas de producción siguen la forma:

- **A → αBβ**  
  Donde **A** es un no terminal, y **α** y **β** son secuencias de terminales y no terminales. La producción asegura que las reglas sean aplicables en un contexto no restringido, permitiendo una amplia variedad de estructuras.


## Modelos de la Gramática

### 1. Gramática Inicial (Reconocimiento del Idioma)

En esta fase, definí símbolos no terminales abstractos para representar estructuras noruegas, como `Setning` (oración), `HovedSetning` (oración principal), y `Subjekt` (sujeto). Los terminales incluyen palabras específicas como `"jeg"`, `"spiser"`, y signos de puntuación (`"."`, `","`). La gramática cubre:

- **Oraciones principales**: `Subjekt` + `Predikat`.
- **Subordinadas**: Inician con conjunción (`Konj`) + `Setning`.
- **Listas coordinadas**: Uso de `Konj` y comas (`Skilletegn`).

**Imagen 1**: Diagrama de la Gramática Inicial  
_(Jerarquía de reglas: `S → Setning Setning_opt`, `Setning → HovedSetning Skilletegn_opt`, `HovedSetning → Subjekt Predikat`)_


## 2. Eliminación de Ambigüedad

La ambigüedad se resolvió reestructurando reglas con múltiples interpretaciones. Para ello, se implementaron las siguientes modificaciones en las reglas de producción:

- **EnkelSubjekt → Pronomen | Art Substantiv | Substantiv | Art DetN | Art AdjE Substantiv | AdjE Substantiv**  
  Esto asegura que no haya ambigüedad al procesar frases como `"den gamle mann"` (el hombre viejo). La introducción de variantes como `DetN` y `AdjE` permite un análisis más claro y preciso de las frases nominales en noruego, eliminando las posibles interpretaciones conflictivas.

- **Predikat → Verb ObjektDel AdverbDel PPDel**  
  Esta regla resuelve la ambigüedad al permitir una mayor flexibilidad en las estructuras verbales. Además, se añadió la opción de incluir elementos como adverbios y frases preposicionales, lo que facilita una representación más precisa de las frases verbales en el idioma.

- **ObjektDel → Objekt | ε**  
  Esto ofrece una opción adicional para representar objetos dentro de la frase, permitiendo tanto la presencia como la ausencia de un objeto directo. Esto ayuda a representar tanto oraciones transitivas como intransitivas de forma más flexible.

- **AdverbDel → AdverbE | ε**  
  Similar a `ObjektDel`, esta producción permite la inclusión o exclusión de adverbios en la estructura. Esto es importante para representar de manera adecuada las oraciones con o sin modificadores adverbiales.

- **PPDel → PP | ε**  
  Para las preposiciones, se permite tanto la presencia como la ausencia de una preposición, lo que otorga mayor flexibilidad sintáctica al procesar oraciones preposicionales.

**Imagen 2**: **Gramática sin Ambigüedad**  
_(Flujo de `EnkelSubjekt` con reglas jerárquicas: `EnkelSubjekt → Art AdjE Substantiv | Art Substantiv`)_


### 3. Eliminación de Recursión Izquierda

La gramática no presenta recursión izquierda, ya que reglas como:

`Subjekt_opt → Konj Subjekt Subjekt_opt | ε`  
usan recursión derecha, lo cual garantiza compatibilidad con **LL(1)** y evita la aparición de recursión izquierda. En caso de haber existido recursión izquierda (p.ej., `A → Aα`), la habría transformado utilizando no terminales auxiliares, siguiendo la forma:  
`A → βA'`  
`A' → αA' | ε`

**Imagen 3**: Estructura de Recursión Derecha  
_(Diagrama de `Subjekt_opt` mostrando derivaciones anidadas sin bucles infinitos)_

# Implementacion 
### Aqui se mostrara la implementación de la gramatica final 


## Casos de Prueba

### Ejemplos Válidos

- **Oración Simple:**

  **Entrada:** `"Jeg spiser et eple."`  
  **Imagen 4**: Árbol de análisis sintáctico generado.

- **Subordinada con Conjunción:**

  **Entrada:** `"Fordi det regner, blir jeg hjemme."`

### Ejemplos Inválidos

- **Falta Artículo:**

  **Entrada:** `"Gutt løper fort."`  
  → **Error:** `EnkelSubjekt` requiere `Art` antes de `Substantiv`.

- **Orden Incorrecto:**

  **Entrada:** `"Spiser jeg mat."`  
  → **Error:** `Predikat` no puede preceder a `Subjekt`.

**Imagen 5**: Mensaje de error para una entrada inválida.


## Complejidad

**Tiempo de parsing:**  
`O(n³)` para una oración de longitud `n`.

## Análisis Final

La gramática es **libre de contexto** (Chomsky Nivel 2) con:

- **No terminales:** `S`, `Setning`, `Subjekt`, `Predikat`.
- **Terminales:** Palabras noruegas y signos de puntuación.
- **Producciones:** 100% libres de ambigüedad y recursión problemática.



