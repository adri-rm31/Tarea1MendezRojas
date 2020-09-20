# ERR4
print("Con el siguiente programa, usted obtendrá algún mensaje dependiendo de dos números que va a ingresar.")
x=int(input("Digite un número"))
y=int(input("Digite otro número"))

if y==x**2:
   print("El segundo número es el cuadrado exacto del primero")
elif y<x**2:
   print("El segundo es menor que el cuadrado del primero")
elif y>x**2:
   print("El segundo es mayor que el cuadrado del primero")

# Errores
# Primera linea muy larga
# No hay espacios despues de los operadores
# Mala indentacion en los print
