num1= int(input("Ingresa el primer número: "));
num2 = int(input("Ingresa el segundo número: "));
num3 = int(input("Ingresa el segundo número: "));

if num1>num2:
    max=num1;
    if num1>num3:
        print("El número ", max, " es el más grande de los tres");
    else:
        print("El número ", num3, " es el más grande de los tres");
else:
    max=num2;
    if max>num3:
        print("El número ", max, " es el más grande de los tres");
    else:
        print("El número ", num3, " es el más grande de los tres");
        
