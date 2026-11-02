def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    risultato = []
    m = len(a)
    n = len(a[0])

    for r in range(n):
        nuova_riga = []

        for el in range(m):
            nuova_riga.append(a[el][r])

        risultato.append(nuova_riga)

    return risultato
 
