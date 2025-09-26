def hanoi(n, a, b, c):
    if n == 1:
        print(f"Mover disco 1 de {a} a {c}")
        return 1
    movimientos = hanoi(n - 1, a, c, b)
    print(f"Mover disco {n} de {a} a {c}")
    movimientos += 1
    movimientos += hanoi(n - 1, b, a, c)
    return movimientos
