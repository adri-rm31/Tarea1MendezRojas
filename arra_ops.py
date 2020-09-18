# Tarea 1 Microprocesadores y Microcontroladores

from Tarea1 import basic_ops


def array_ops(A, B, operacion):
    if (len(A) == len(B)):                  # Array del mismo largo
        n = len(A)
        r = []
        c = 0
        flg = 0
        while (n > c):
            # Llamada a la funcion basic_ops
            h = basic_ops(A[c], B[c], operacion)
            r.append(h)
            if (r[c] == "ERROR! OP") or (r[c] == "ERROR! FR") or (r[c] == "ERROR! NE"):         # Evalua que cada posicion del array no incumpla las condiciones
                r[0] = r[c]
                c = n
                flg = 1
            c = c + 1
        if (flg == 0):
            return r
        else:
            return r[0]
    else:
        # Si los array son de distinto tamaño
        print("los array son de tamaño distinto")
        # Se elige "AD" como codigo de error
        return ("ERROR! AD")
