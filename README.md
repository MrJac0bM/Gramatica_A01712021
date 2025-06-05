# E2 Generación y Limpieza de una Gramática Libre de Contexto Restringida

## Descripción

Las gramáticas son fundamentales en los métodos computacionales para el procesamiento del lenguaje, ya que proporcionan una base formal para comprender, generar y manipular datos lingüísticos. En este proyecto, nos enfocamos en el **noruego** y construimos una gramática que acepta palabras y estructuras específicas de este idioma. Las reglas incluyen:

- **Oraciones principales**: Frase nominal + Frase verbal.
- **Frases nominales**: Construidas con sustantivos, determinantes y pronombres.
- **Frases verbales**: Incluyen verbos, verbos con preposiciones y adverbios.
- **Oraciones subordinadas**: Comienzan con una conjunción seguida de una frase verbal + frase nominal y terminan con una oración principal.
- **Oraciones separadas por comas/conjunciones**: Conjuntos de sustantivos y verbos separados por comas u oraciones principales unidas por conjunciones.

> **Nota**: Todas las oraciones deben terminar con un signo de puntuación (p.ej., `.`).

Para implementar esto, utilizamos un analizador sintáctico **LL(1)**, que procesa la entrada de izquierda a derecha con un token de anticipación, evitando retrocesos.


## Modelo Matemático

El análisis y la implementación de la gramática se basan en conceptos fundamentales de la teoría de lenguajes formales y autómatas. La gramática que hemos construido sigue los principios de una **gramática libre de contexto** (CFG) según la jerarquía de Chomsky. Esta jerarquía se clasifica en cuatro niveles:

1. **Lenguajes Regulares (Nivel 3)**: Generados por gramáticas regulares.
2. **Lenguajes Libres de Contexto (Nivel 2)**: Generados por gramáticas libres de contexto, como la que estamos usando en este proyecto.
3. **Lenguajes Sensibles al Contexto (Nivel 1)**: Generados por gramáticas sensibles al contexto.
4. **Lenguajes Recursivamente Enumerables (Nivel 0)**: Generados por gramáticas Turing-completas.

En nuestro caso, estamos utilizando una **gramática libre de contexto** (Chomsky Nivel 2) para modelar el idioma noruego, lo cual implica que nuestras reglas de producción siguen la forma:

- **A → αBβ**  
  Donde **A** es un no terminal, y **α** y **β** son secuencias de terminales y no terminales. 

## Modelos de la Gramática

### 1. Gramática Inicial (Reconocimiento del Idioma)

En esta fase, definí símbolos no terminales abstractos para representar estructuras noruegas, como `Setning` (oración), `HovedSetning` (oración principal), y `Subjekt` (sujeto). Los terminales incluyen palabras específicas como `"jeg"`, `"spiser"`, y signos de puntuación (`"."`, `","`). La gramática cubre:

- **Oraciones principales**: `Subjekt` + `Predikat`.
- **Subordinadas**: Inician con conjunción (`Konj`) + `Setning`.
- **Listas coordinadas**: Uso de `Konj` y comas (`Skilletegn`).

![image](https://github.com/user-attachments/assets/aef09a47-ffcd-4eba-800c-c3ea51f197fc)


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
  
![image](https://github.com/user-attachments/assets/6253321b-dd89-4e07-b0fe-c89f5e6521e9)



### 3. Eliminación de Recursión Izquierda

La gramática no presenta recursión izquierda, ya que reglas como:

`Subjekt_opt → Konj Subjekt Subjekt_opt | ε`  
usan recursión derecha, lo cual garantiza compatibilidad con **LL(1)** y evita la aparición de recursión izquierda. En caso de haber existido recursión izquierda (p.ej., `A → Aα`), la habría transformado utilizando no terminales auxiliares, siguiendo la forma:  
`A → βA'`  
`A' → αA' | ε`

![image](https://github.com/user-attachments/assets/dcd4d27c-7c57-4b5e-abf9-907140efb20d)


# Implementacion 
![image](https://github.com/user-attachments/assets/1878e736-3171-4267-b672-1efcf7507704)



## Descripción

Se generaron las siguientes tablas basadas en la gramática libre de contexto desarrollada:

- **Tabla First y Follow**: Muestra los conjuntos First y Follow de todos los no terminales, utilizados para guiar la construcción del parser LL(1).
- **Tabla de Parsing LL(1)**: Relaciona pares (no terminal, terminal) con las producciones aplicables, facilitando el proceso de análisis sintáctico.

Ambas tablas se encuentran disponibles en archivos `.xlsx` anexos en este repositorio.



## Casos de Prueba

### Ejemplos Válidos

- **Oración Simple:**

  **Entrada:** `"jeg spiser en eple."`  
  ![image](https://github.com/user-attachments/assets/0f19e2d2-53cf-48bc-9da3-9aedd750220a)


- **Oracion conjunta de dos sujetos**

  **Entrada:** `"en gamle hund og katt elsker solskinnet"`
  ![image](https://github.com/user-attachments/assets/9cf78af6-b38f-4a7e-849f-c7c09946df91)

 - **Oracion conjunta**
   **Entrada:** `"en gamle hund og katt elsker solskinnet raskt og alltid , men hund hater varmen sakte ."`
   ![image](https://github.com/user-attachments/assets/59b1a2f4-d95b-44dc-aaad-240d8ee4f9ec)


### Ejemplos Inválidos

-nkelSubjekt` requiere `Art` antes de `Substantiv`.

- **Orden Incorrecto:**

  **Entrada:** `"Spiser Jeg Mat."`  
  → **Error:** La gramática implementada no tolera Oraciones con Mayúsculas.
  ![image](https://github.com/user-attachments/assets/917b7eac-f88c-47a7-93ac-675b0044fb9c)

  **Entrada:** `"jeg spiser en eple."`  
  



## Complejidad

**Tiempo de parsing:**  
`O(n³)` para una oración de longitud `n`.

## Análisis Final

La gramática es **libre de contexto** (Chomsky Nivel 2) con:

- **No terminales:** `S`, `Setning`, `Subjekt`, `Predikat`.
- **Terminales:** Palabras noruegas y signos de puntuación.
- **Producciones:** 100% libres de ambigüedad y recursión problemática.

## Fuentes 
- Sipser, M. (2013). Introduction to the Theory of Computation (3rd ed.). Cengage Learning.

- Aho, A. V., Lam, M. S., Sethi, R., & Ullman, J. D. (2007). Compilers: Principles, Techniques, and Tools (2nd ed.). Addison-Wesley.

- Jurafsky, D., & Martin, J. H. (2009). Speech and Language Processing (2nd ed.). Prentice Hall.
