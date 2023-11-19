print("Introduce dos números a comparar");

num_1 = int(input("Introduce el primer número: "));
num_2= int(input("Introduce el segundo número: "));

print("Los números a comprara son ", num_1, " y ", num_2);

if num_1 == num_2:
    print("Es igual")
if num_1 != num_2:
    print("Es diferente")
if num_1 > num_2:
    print("Es mayor")
if num_1 >= num_2:
    print("Es mayor o igual")
if num_2 > num_1:
    print("Es menor")
if num_2 >= num_1:
    print("Es menor o igual")