# Travel Salesman Problem

## Reportes

La ejecucion de grasp sobre todos los archivos de prueba se realizo con un maximo de iteraciones de 5000, 200 como cantidad maxima de mejoras minimas y un ratio de 2% de mejora minima aceptable.

Para el grafico de scoring completo se guarda la iteracion en la que se obtuvo la mejor solucion, junto con el costo de la misma. De esta manera vemos como algunos grafos alcanzan la mejor solucion encontrada en relativamente pocas iteraciones.
Tambien se realizaron graficos evolutivos a traves de las etapas para cada grafo, se pueden observar en esta seccion.

![scoring](https://github.com/MauroB3/tsp_grasp/blob/main/images/scoring%20completo.jpg?raw=true)


## Como ejecutarlo

En el archivo main.py existen dos funciones, una para ejecutar grasp sobre un grafo concreto y otra para ejecutar grasp sobre la bateria de test completa. En caso de querer ejecutar para un solo grafo se debe indicar el nombre del mismo.

Como resultado de ambas funciones se genera un archivo '.txt' dentro de la carpeta 'resultados' que contiene el camino hamiltoniano de la solucion y el costo del mismo. Ademas, dentro de la carpeta 'images' se generará un grafico evolutivo a traves de las etapas de grasp para cada grafo o para el grafo elegido.

### Importante

Existen 4 constantes dentro de main.py:
  - **MAX_ITERACIONES**: Es el maximo de iteraciones para el algoritmo grasp.
  - **MAX_MEJORAS_MINIMAS**: Es la cantidad de veces que vamos a aceptar mejorar 'poco'.
  - **RATIO_MEJORA_MINIMA**: Es el porcentaje minimo de mejora que vamos a aceptar.
  - **POS_INICIAL**: Es el nodo desde el que partimos.

Estos 4 valores pueden ser modificados a gusto. Yo considere estos valores iniciales ya que luego de varias pruebas considere que son los que mejores soluciones generan.
