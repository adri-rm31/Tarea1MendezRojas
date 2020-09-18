import Tarea1


def test_basic_ops():

    # Caso EXITO

    assert Tarea1.basic_ops(-3, 2, "s") == -1
    assert Tarea1.basic_ops(1, 2, "r") == -1
    assert Tarea1.basic_ops(5, 13, "a") == 5
    assert Tarea1.basic_ops(5, 13, "o") == 13

    # Caso ERROR fuera del rango

    assert Tarea1.basic_ops(-710, 2, "s") == "ERROR! FR"
    assert Tarea1.basic_ops(1, 420, "r") == "ERROR! FR"

    # Caso ERROR operacion no existe

    assert Tarea1.basic_ops(3, 2, "W") == "ERROR! OP"
    assert Tarea1.basic_ops(9, 2, 2) == "ERROR! OP"

    # Caso ERROR no es entero

    assert Tarea1.basic_ops("a", 2, "s") == "ERROR! NE"
    assert Tarea1.basic_ops(2.2, 3, "r") == "ERROR! NE"
