import arra_ops

# Caso EXITO


def test_array_ops():

    # Caso EXITO

    assert arra_ops.array_ops([1, 2, 0], [3, 1, 0], "s") == [4, 3, 0]
    assert arra_ops.array_ops([1, 2, 0], [3, 1, 0], "r") == [-2, 1, 0]
    assert arra_ops.array_ops([5, 2, 2], [13, 1, 3], "a") == [5, 0, 2]
    assert arra_ops.array_ops([5, 2, 2], [13, 1, 3], "o") == [13, 3, 3]

    # Caso ERROR no es entero
    assert arra_ops.array_ops(["a", "b", "c"], [13, 1, 3], "s") == "ERROR! NE"
    assert arra_ops.array_ops([1, 2], [3.2, 1], "r") == "ERROR! NE"

    # Caso ERROR fuera del rango
    assert arra_ops.array_ops([-350, 2, 2], [13, 1, 3], "s") == "ERROR! FR"
    assert arra_ops.array_ops([5, 2, 2], [420, 1, 3], "r") == "ERROR! FR"

    # Caso ERROR operacion no existe
    assert arra_ops.array_ops([5, 2, 2], [13, 1, 3], "W") == "ERROR! OP"
    assert arra_ops.array_ops([5, 2, 2], [13, 1, 3], 2) == "ERROR! OP"

    # Caso largos de array distintos
    assert arra_ops.array_ops([5, 2, 2], [13, 1], "s") == "ERROR! AD"
