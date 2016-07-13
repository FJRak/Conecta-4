# Conecta-4
Implementación de conecta 4 con heurística propia
Primer trabajo de curso: Búsqueda con oponente

En este programa hemos implementado una heurística que consiste en hacer un recorrido por todos los movimientos legales de cada estado e ir devolviendo unas puntuaciones calculadas contando las fichas del jugador y las del rival. 

Hemos establecido unos criterios para darle valor a cada recorrido (horizontal, vertical y diagonal) y asignando a cada jugador un contador, inicializado a 0.

Si en el recorrido, aparece una ficha del jugador, el contador se incrementa en 10 (puntos)
Si en el recorrido, aparece una ficha del adversario, el contador se resetea a 0 (puntos)
Si en el recorrido, aparece un espacio libre, el contador se incrementa en 1 (puntos)

El valor heurístico final es la suma de las puntuaciones obtenidas tras haber hecho el recorrido en vertical, horizontal y diagonal.

También hemos implementado dos opciones para darle emoción al juego. Una de ellas es la posibilidad de elegir quien empieza primero moviendo. La otra opción es elegir un nivel de dificultad, que puede ser: fácil, medio o difícil. 

Fácil—> profundidad 1
Media —> profundidad 2
Difícil —> profundidad 4

Entendiendo que, a mayor número de estados recorra, mejor elige el movimiento.


David Morales Robaina 
Francisco Javier Socorro Martín
