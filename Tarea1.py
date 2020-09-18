# Tarea 1 Microprocesadores y Microcontroladores


def basic_ops(A, B, operacion):

    try:
        a = int(A)                                  # A y B deben ser enteros
        b = int(B)
        x = A - a
        y = B - b

        if(x == 0 and y == 0):

            # A y B entre -127 y 127

            if (a > -128 and b > -128 and a < 128 and b < 128):

                # Elige la operacion

                if (operacion == 's' or operacion == 'S'):
                    C = int(A) + int(B)
                    return C                            # Hace la suma
                elif (operacion == 'r' or operacion == 'R'):
                    D = int(A) - int(B)
                    return D                            # Hace la resta
                elif (operacion == 'a' or operacion == 'A'):
                    E = int(A)
                    F = int(B)
                    G = E & F
                    return G                            # Hace el AND
                elif (operacion == 'o' or operacion == 'O'):
                    H = int(A)
                    Q = int(B)
                    J = H | Q
                    return J                            # Hace el OR
                else:
                    # Si la operacion no existe
                    print("La operacion seleccionada no existe")
                    # Se elige "OP" como codigo de error
                    return ("ERROR! OP")

            else:
                # Si está fuera del rango
                print("Los numeros estan fuera del rango entre -127 y 127")
                # Se elige "FR" como codigo de error
                return ("ERROR! FR")
        else:
            # Si A y B no son enteros
            print("No es un numero entero")
            # Se elige "NE" como codigo de error
            return ("ERROR! NE")

    except ValueError:
        # Si A y B no son enteros
        print("No es un numero entero")
        # Se elige "NE" como codigo de error
        return ("ERROR! NE")
