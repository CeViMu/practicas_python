#COONDICIONALES COMPUESTAS
print("Sistema para calcular el promedio de un alumno");

nombre = input("Para comenzar ¿cuál es tu nombre? ");

matematicas = float(input(nombre + " ¿Cuál es tu calificación en matemáticas? "));
quimica = float(input(nombre + " ¿Cuál es tu calificación en quimica? "));
biologia = float(input(nombre + " ¿Cuál es tu calificación en biología? "));

promedio = (matematicas + quimica + biologia)/3;

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de ', promedio);
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de ', round(promedio, 2));
else:
    print('Lo sentimos ' + nombre + ' has "reprobado" con un promedio de ', promedio)


#elseif
print("¡Convertidor de números a letras");
num_uno = int(input("¿Cuál es el número que deseas convertir? "));

if num_uno == 1: 
    print("El número es uno")
elif num_uno ==2:
    print("El número es dos")
elif num_uno == 3:
    print("El número es tres")
elif num_uno == 4:
    print("El número es cuatro")
elif num_uno == 5:
    print("El número es cinco")
else:
    print("Este programa solo puede convertir hasta el número cinco")