print("Sistema de solicitud de vacaciones");
nombre=input("Ingresa tu nombre: ");
clave=int(input("Ingresa tu clave: "));
antiguedad=int(input("Ingresa tu antiguedad en la empresa: "));


if clave==1:
    if antiguedad==1:
        dias_vacaciones = 6
    elif antiguedad<=6 and antiguedad>=2:
        dias_vacaciones = 14
    elif antiguedad>=7:
        dias_vacaciones = 20
    else:
        dias_vacaciones = 0
elif clave ==2:
    if antiguedad==1:
        dias_vacaciones = 7
    elif antiguedad<=6 and antiguedad>=2:
        dias_vacaciones = 15
    elif antiguedad>=7:
        dias_vacaciones = 22
    else:
        dias_vacaciones = 0
elif clave ==3:
    if antiguedad==1:
        dias_vacaciones = 10
    elif antiguedad<=6 and antiguedad>=2:
        dias_vacaciones = 20
    elif antiguedad>=7:
        dias_vacaciones = 30
    else:
        dias_vacaciones = 0
else:
    dias_vacaciones=0

print("Nombre: " + nombre);
print('Clave: ', clave);
print("Días de vacaciones: ", dias_vacaciones);