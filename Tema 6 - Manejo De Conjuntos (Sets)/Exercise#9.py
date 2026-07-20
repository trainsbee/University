# Ejercicio #9: Dados dos conjuntos numéricos inicializados como {1, 2,
# 3, 4} y {3, 4, 5, 6}, realice los cálculos lógicos correspondientes para
# obtener e imprimir la diferencia matemática estricta entre el primer
# conjunto respecto al segundo.

setOne = {1,2,3,4}
setTwo = {3,4,5,6}

difference = setOne.difference(setTwo)

print(difference)

# Los valores 3 y 4 estan en ambos conjuntos por, lo que se eliminan de la diferencia, solo quedan los que
# no se repiten.

# py "Tema 6 - Manejo De Conjuntos (Sets)\Exercise#9.py"