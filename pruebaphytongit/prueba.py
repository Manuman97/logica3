# Este es el juego de adivinar el numero

#   numero = 38
#   intentos = 1

#   print("Ingrese un numero del 1 al 50")
#   num = int(input()) # pedimos un numero
#   if(num==numero):
#           print("El numero a sido adivinado")
#           print("utilizaste {intentos}")
#       else:
#       if(num < numero):
#            print("Te has quedado corto")
#    else:
#         print("Te has pasado")

        
        # hola

import random
numero = random.randint(1, 50)
intentos = 5

for _ in range(intentos):
    intentos = int(input("Adivina el numero. Ingrese un numero del 1 al 50, tienes 5 intentos "))
    if intentos < numero:
        print("Te has quedado corto")
    elif intentos > numero:
        print("Te has pasado")
    else:
        print(f"¡¡Ganaste¡¡ El numero a sido adivinado. ")
        break
else:
    print(f"Lo siento perdiste, utilizaste 5 intentos el numero era {numero}.")











