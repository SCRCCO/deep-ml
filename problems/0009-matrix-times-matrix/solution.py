def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]] | int:

    if not a or not b or not a[0] or not b[0]:
        return -1

    if len(a[0]) != len(b):
        return -1

    if any(len(row) != len(a[0]) for row in a):
        return -1

    if any(len(row) != len(b[0]) for row in b):
        return -1

    m = len(a)
    n = len(b[0])
    p = len(b)

    risultato = []

    for i in range(m):
        nuova_riga = []

        for j in range(n):
            somma = 0

            for k in range(p):
                somma += a[i][k] * b[k][j]

            nuova_riga.append(somma)

        risultato.append(nuova_riga)

    return risultato