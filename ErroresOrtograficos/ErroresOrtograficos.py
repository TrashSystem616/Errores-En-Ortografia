#comenazamos con la programacion
#importamos la librearias necesarias
import enchant

#cabe recalcar que solo funciona con archivos txt si deseas trabajar con word o pdf recomiendo que pases todo el texto a un formato Txt
#:)

# Crea un diccionario de palabras en inglés
d = enchant.Dict("en_US")

# Lee el archivo de texto y separa las palabras
#te recomiendo que copies todo lo que quieres analizae en el hola.txt que esta en la carpeta principal
with open("C:/Users/chich/OneDrive/Documentos/Programacion/ErroresOrtograficos/Hola.txt", "r") as file:
    words = file.read().split()

# Verifica la ortografía de cada palabra y crea una lista de palabras mal escritas
incorrect_words = []
for word in words:
    if not d.check(word):
        incorrect_words.append(word)

# Imprime la lista de palabras mal escritas
print("Palabras mal escritas:")
for word in incorrect_words:
    print(word)

# Esperar la entrada del usuario
input("Presiona cualquier tecla para cerrar el programa...")

# Salir del programa
exit()

