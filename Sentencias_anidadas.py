#Conversor
print("Conversor")

print("Menú de opciones: \n Presiona 1 para convertir de número a palabra.\n Presiona 2 para convertir de palabra a número")

eleccion = int(input("¿Cuál es tu opción deseada? "))

if eleccion == 2:
    print("Conversor de palabra a número")
    palabra = input("¿Cuál es la palabra que deseas convertir a número? ")
    if palabra == "uno": #poner str entre comillas
        print("El número es 1")
    elif palabra == "dos":
        print("El número es 2")
    elif palabra == "tres":
        print("El número es 3")
    elif palabra == "cuatro":
        print("El número es 4")
    elif palabra == "cinco":
        print("El número es 5")
    else:
        print("Este programa solo puede convertir hasta el número 5")

elif eleccion == 1:
    print("Conversor de número a palabra")
    numero = int(input("¿Cúal es el número que deseas convertir? "))
    if numero == 1: 
        print("El número es uno")
    elif numero ==2:
        print("El número es dos")
    elif numero == 3:
        print("El número es tres")
    elif numero == 4:
        print("El número es cuatro")
    elif numero == 5:
        print("El número es cinco")
    else:
        print("Este programa solo puede convertir hasta el número cinco")

else:
    print("Opción no disponible")
    print("Fin")