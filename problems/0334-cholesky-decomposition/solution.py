
import numpy as np

def cholesky_decomposition(A):
    """
    Scompone una matrice A nel prodotto L @ L.T,
    dove L è una matrice triangolare inferiore.

    Restituisce L come lista di liste oppure -1
    se la decomposizione non è possibile.
    """

    # Converto la matrice in un array di float.
    # Se contiene valori non validi, restituisco -1.
    try:
        A = np.array(A, dtype=float)
    except (ValueError, TypeError):
        return -1

    # Controllo che sia una matrice quadrata e non vuota.
    if A.ndim != 2 or A.shape[0] == 0:
        return -1

    n = A.shape[0]

    if A.shape[1] != n:
        return -1

    # La matrice deve contenere solo numeri finiti
    # e deve essere simmetrica, cioè A = A.T.
    if not np.all(np.isfinite(A)):
        return -1

    if not np.allclose(A, A.T):
        return -1

    # Inizializzo L con tutti zeri.
    # Riempirò solo la diagonale e la parte inferiore.
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):

            # Calcolo la somma dei prodotti degli elementi
            # delle righe i e j già trovati.
            somma = 0
            for k in range(j):
                somma += L[i, k] * L[j, k]

            if i == j:
                # Sulla diagonale devo calcolare la radice
                # dell'elemento originale meno la somma.
                valore = A[i, i] - somma

                # Se il valore non è positivo, la matrice
                # non è definita positiva.
                if valore <= 0:
                    return -1

                L[i, j] = np.sqrt(valore)

            else:
                # Sotto la diagonale sottraggo la somma
                # e divido per l'elemento diagonale
                # della colonna che sto calcolando.
                L[i, j] = (A[i, j] - somma) / L[j, j]

    # L'esercizio richiede una lista di liste, non un array.
    return L.tolist()
