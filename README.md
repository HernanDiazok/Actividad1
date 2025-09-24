# SIMULACION DE EVALUACIÓN PARA LA FERIA DE CIENCIAS
    Este programa permite calcular los puntajes totales de cada equipo en 
    distintas rondas de evaluación, determinar el Mejor Equipo de la Ronda 
    (MER) y generar un ranking final de los equipos.
    Cada equipo recibe puntos según: Innovación: +3 puntos por unidad
    Presentación: +1 punto por unidad -Errores: -1 punto si comete errores
    El programa suma automáticamente los puntajes de todas las rondas
    y muestra el ranking actualizado después de cada ronda por equipo 
    de forma descendente, así como el ranking final al terminar todas las rondas.

## Requisitos previos 
    Antes de empezar con el programa, asegúrate de tener instalado lo siguiente:
    Python 3.12.2 o superior (puedes verificar tu versión ejecutando:
    python --version` en la terminal).
    Jupyter Notebook
    Visual Studio Code (opcional)
    No requiere instalar librerías adicionales.

## Estructura de Archivos

Para que el programa funcione correctamente, los archivos deben estar organizados de la
siguiente manera:
├── src/
│   └── funciones.py      # Contiene las funciones de cálculo
│    └── base_de_datos.py # Contiene la lista de diccionarios con la base de datos
├── notebooks/
│   └── main.ipynb         # Ejecuta la simulación y muestra resultados
└── README.md              # Este archivo


main.ipynb: ejecuta la lógica del programa y muestra los resultados de cada ronda.
funciones.py: contiene funciones como calcular_puntos, determinar_mer y mostrar_ranking.

## Cómo usar el Programa

Para ver los resultados de la simulación:
Asegurate de que los archivos estén en la estructura correcta (ver sección Estructura de Archivos).
Abrir y ejecutar el Notebook principal:
Abrí notebooks/main.ipynb en un entorno que pueda ejecutar Jupyter (como Jupyter Notebook o JupyterLab).
Esto se realiza a través del CDM - 
Windows: buscá “CMD”
Buscas en donde esta guardada la ruta del proyecto:
(en mi caso)
C:\Users\HernanDiaz\Desktop\Python
En la terminal escribís:
cd C:\Users\HernanDiaz\Desktop\Python
Una vez que verificas que estás en la ruta del proyecto, ejecutas
jupyter lab
En JupyterLab, navegá a notebooks/main.ipynb y hacé doble clic para abrirlo.
Ejecutá cada celda del código. Al finalizar, se mostrarán:
La ronda que se está evaluando
El “Mejor Equipo de la Ronda” y su puntaje
Un ranking actualizado con los puntajes acumulados de todos los equipos
Opcional: Ejecutar desde VS Code:
Abrí VS Code y seleccioná File > Open Folder para abrir la carpeta del proyecto.
Abrí notebooks/main.ipynb y ejecutalo usando la extensión de Jupyter de VS Code (ejecutando cada celda).

## Notas Adicionales 

El programa suma automáticamente los puntajes de todas las rondas para cada equipo.
El ranking incluye:
Innovación total
Presentación total
Errores cometidos
Cantidad de MER
Puntos totales
La simulación permite ver cómo se comportan los equipos en cada ronda y cuál sería el ganador al final de la competencia.
