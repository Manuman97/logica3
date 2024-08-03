# Este es el juego de adivinar el numero
numero = 38
intentos = 1

print("Ingrese un numero del 1 al 50")
num = int(input()) # pedimos un numero
if(num==numero):
    print("El numero a sido adivinado")
    print("utilizaste {intentos}")
else:
    if(num < numero):
            print("Te has quedado corto")
    else:
         print("Te has pasado")



        
        












