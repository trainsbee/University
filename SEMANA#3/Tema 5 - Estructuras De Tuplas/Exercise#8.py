# Ejercicio #8: Defina una tupla base conteniendo los hilos ("rojo",
# "verde", "azul"). Realice una conversión explícita a formato de lista para
# poder alterar el segundo elemento a "Amarillo", y devuelva el arreglo
# final convertido nuevamente en tupla para su impresión.

colors = ("rojo", "verde", "azul")

color_list = list(colors)

color_list[1] = "amarillo"

colors = tuple(color_list)

print(colors)

# py "SEMANA#3\Tema 5 - Estructuras De Tuplas\Exercise#8.py"