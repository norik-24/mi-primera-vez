
#variables y tipos
#string o cadenas de caracteres (str)
#char o character str
#numbers: enteros(int) decimales(float)
#booleanos (true or false)
name = "esteban"
age = 16
heigth = 1.78
trainer = False
#conjuntos de datos
hobbies = list()
hobbies = ["boxear","dormir", "jugar", "comer" ]
#imprimir la posicion 1 en la lista
print (hobbies[1])
#imprimir la cantidad de texto de hobbies
print(len(hobbies))

#añadir datos a la lista
hobbies.append(input("ingrese sus pasatiempos"))
#imprimir datos en pantalla de la lista hobbies
print (hobbies)
#eliminamos el texto en la posicion 2
hobbies.pop(2)
#imprimimos en pantalla los cambios
print(hobbies)