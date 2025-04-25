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
