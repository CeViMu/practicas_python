print("Sistema para calcular el promedio de un alumno")

nombre= input("Escribe tu nombre: ")
matematicas=int(input(nombre + ", ¿Cuál es tu calificación en matemáticas? "))
quimica=int(input(nombre + ", ¿Cuál es tu calificación en química? "))
biologia = int(input(nombre + " ¿Cuál es tu calificación en biología? "))

promedio = (matematicas + quimica + biologia)/3
promedio_entero = int(promedio)
#No se puede concatenar de manera directa un string con un number
#podemos usar una coma
if promedio >= 6 :
    print('Felicidades ' + nombre + '" aprobaste" con un promedio de ', promedio)
    
print("Fin")
