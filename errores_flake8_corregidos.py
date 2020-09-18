print("Con el siguiente programa, ")
print("usted obtendrá algún mensaje")
print("dependiendo de dos números que va a ingresar.")
x = int(input("Digite un número: "))
y = int(input("Digite otro número: "))

if y == x**2:
    print("El segundo número es el cuadrado exacto del primero")
elif y < x**2:
    print("El segundo es menor que el cuadrado del primero")
elif y > x**2:
    print("El segundo es mayor que el cuadrado del primero")
