# Ejercicio #3: Defina una estructura inmutable de tupla con los
# elementos enteros (1, 2, 3). Intente realizar una modificación directa
# alterando el primer elemento a un valor de 10 y verifique/documente el
# comportamiento del compilador mediante un comentario analítico en su
# código explicando la inmutabilidad.

numbers = (1,2,3)

numbers[0] = 10

print(numbers)

#Es inmutable porque, una vez que se crea, sus valores no pueden ser modificados.
#Esto es para evitar cambios accidentales. 

# Anteriormente en un bot que construí para capturar informacion de
# un CRM autenticado para automatizar un proceso el bot recibia unos parametros que no deben ser modificados
# por ningun motivo file_id,phone estos dos valores si se modiifcaba un numero podria ocasionar no enviar
# informacion o enviar la informacion de otro clientes lo cual seria falta en el proceso

#Ejemplo de mi bot
# umbrella= {
#     "file_id": "FILE_12345",
#     "phone": "50498765432"
# }


#data = (umbrella["file_id"], umbrella["phone"])

# py "Tema 5 - Estructuras De Tuplas\Exercise#3.py"