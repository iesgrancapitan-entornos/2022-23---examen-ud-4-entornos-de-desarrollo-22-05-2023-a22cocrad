[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/53x4un59)
# Examen Tema 4 Entornos de Desarrollo - 1DAW

***Refactorización, Documentación y control de versiones***

El examen se divide en 3 bloques claramente diferenciados: Refactorización, Documentación y control de versiones. Cada uno de ellos con una puntuación sobre 10. **Para dar por superado el RA relacionado con el tema 4, se deben aprobar las 3 partes**.

En cada apartado se indica la puntuación y que parte corresponden. Las 3 se puntúan sobre 10

Sigue detalladamente las instrucciones del examen. Cualquier duda, pregunta a tu profesor.

1. En el repositorio tienes en código fuente que será la base sobre la cual desarrollaremos el examen. Dividiremos el examen en 3 partes, y las utilizaremos para desarrollar las versiones de git y github. Evidentemente, usaremos las buenas prácticas de git y github que hemos estado trabajando durante el curso

### Ramas y Merge I

1. Para el workflow del examen, utilizaremos las siguientes ramas: desarrollo, refactorización, documentación. Crealas cuando se te indique.

2. Crea la rama "desarrollo"

## Refactorización

3. Crea la rama "refactorizacion" a partir de la rama desarrollo y cambiate a esa rama ***(CV - 0.25 puntos)***

4. Haz las refactorizaciones que necesites para que "Guau" sea un campo de la clase Perro llamado "ladra" y se inicialize en el constructor. ***(RF - 4 puntos)***
   
5. Compromete el estado actual con el mensaje "Refactorizacion 1 Perro - Nombre y Apellidos" ***(CV - 0.25 puntos)***

6. Extrae una superclase a partir de la clase "Coche" llamada "Vehículo" con los campos:

   1. num_serie
   2. fabricante
   3. color

7. Compromete el estado actual con el mensaje "Refactorizacion 2 Superclase Vehículo - Nombre y Apellidos". ***(RF - 6 puntos)***

8. Fusiona la rama "refactorizacion" en la rama "desarrollo" ***(CV - 0.5 puntos)***

## Documentación

8. Crea la rama "documentacion" a partir de la rama desarrollo y cambiate a esa rama ***(CV - 0.25 puntos)***

9. Documenta con el formato Docstring "reStructuredText" las clases y los métodos para que aparezcan sus descripciones, autor, y descripción de los parámetros y devoluciones de cada método. Compromete el estado actual con el mensaje "Documentación 1 - Nombre y Apellidos" ***(DOC - 2.5 puntos)***

10. Añade todos los rst necesarios para que aparezca la documentación de todos las clases ***(DOC - 1 punto)***

11. Añade en el index un rst para que haya un enlace donde aparezca el enunciado completo del examen ***(DOC - 1 punto)***

12. Añade en la documentación: ***(DOC - 3 puntos)***
    1. Autor: Tu nombre y apellidos
    2. Nombre del proyecto "Examen Entornos"
    3. Versión: una versión con notación ***"versionado semántico"***
    4. copyright: El que tu quieras
    5. Añade las extensiones "autodoc, intersphinx, todo, mathjax, napoleon, autosummary
    6. Usa el tema "sphinx_rtd_theme"

11. Genera la documentación html usando la generación de documentación sphinx y guárdalo en tu repositorio en una carpeta que se llame "doc". Compromete el estado actual con el mensaje "Documentación 2 Javadoc - Nombre y Apellidos" ***(DOC - 2.5 puntos)***

## Control de Versiones

10. Fusiona la rama "documentacion" en la rama "desarrollo" ***(CV - 0.5 puntos)***

### Pull Request

13. Actualiza tu repositorio, si no lo has hecho ya.

14. Realiza un fork del repositorio del examen a tu cuenta de github. ***(CV - 0.5 puntos)***

15. En el repositorio forkado, ve a la rama de documentación y modifica la etiqueta title del index.html con tu nombre y apellidos

16. Compromete los cambios con la etiqueta "pull request Nombre y apellidos" ***(CV - 0.25 puntos)***

17. Realiza un pull request de la rama **documentacion** de tu repositorio forkado sobre la rama **desarrollo** del repositorio del examen ***(CV - 2.5 puntos)***

18. Acepta los cambios y haz un merge de tu pull request ***(CV - 0.5 puntos)***

19. **No borres el repositorio de tu cuenta hasta que el examen esté corregido**

### Issues

19. Observa los issues que deberías tener en tu repositorio de examen.

20. Cierralos con un solo commit que contenga en la etiqueta "Cerrando Issues - Nombre y Apellidos" ***(CV - 1.5 puntos)***

### Ramas y Merge II

21.  Fusiona la rama desarrollo en la rama main ***(CV - 0.5 puntos)***

### Github Pages

22.  Crea una página con tu repositorio de la rama main. En la url "iesgrancapitan-entornos.github.io/repositorioexamen/doc" debe aparecer tu documentación sphinx ***(CV - 0.5 puntos)***

### Tags y Releases

23. Añade un tag en el primer commit del repositorio de la rama main con la v0.0.1 y la descripción "Primera versión alpha - Nombre y Apellidos" ***(CV - 0.5 puntos)***

24. Añade otro tag en el último commit (sin crear otro commit nuevo) con la v1.0.0 "Primera Release Candidate - Nombre y Apellidos" ***(CV - 0.5 puntos)***

25. Sube sólo los tags al repositorio. Estos tags deben aparecer también en la pestaña release ***(CV - 0.5 puntos)***

###  Gitlab

26. Crea un repositorio en el grupo de Entornos de gitlab. Añadelo a tu repositorio local y súbelo. Deberás tener el mismo repositorio tanto en github como gitlab ***(CV - 0.5 puntos)***

##  Nota

***En caso de cualquier duda y/o errata, será resuelta durante la realización del examen***
