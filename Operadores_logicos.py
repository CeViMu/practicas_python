print("Conjunción (and)")

num_1 = int(input("Escribe un número mayor a dos y menor a 5: "));

if num_1>2 and num_1<5:
    print("El número ", num_1, " cumple con la condición. \n")
else:
    print("El número", num_1, " no cumple con la condición.\n") 
    
    
    
print("Disyunción (or)")

palabra=input("Para cumplir con la condición escribe 'si' o 'yes'")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido")
else:
    print("La condición no se ha cumplido")
    

print("\nNegación (not)")

num_1=int(input("Introduce un número igual a 5: "))
if not num_1 == 5:
    print("El número es diferente a cinco y se cumple la condición")
else:
    print("El número es igual a cinco")