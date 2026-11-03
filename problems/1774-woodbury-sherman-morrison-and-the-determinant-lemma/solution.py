import numpy as np

def woodbury_solve(sigma_diag, X, B):
    # Sigma è diagonale, quindi la sua inversa si ottiene
    # facendo 1 diviso ogni elemento della diagonale
    sigma_inv = 1 / np.asarray(sigma_diag)

    # Se B è un vettore lo trasformo in una colonna
    B = np.asarray(B)
    vettore = B.ndim == 1

    if vettore:
        B = B.reshape(-1, 1)

    # Moltiplico Sigma^-1 per X e per B
    # Uso [:, None] per applicare ogni valore alla rispettiva riga
    sigma_X = sigma_inv[:, None] * X
    sigma_B = sigma_inv[:, None] * B

    # Formula di Woodbury:
    # (Sigma + X X^T)^-1 =
    # Sigma^-1 - Sigma^-1 X (I + X^T Sigma^-1 X)^-1 X^T Sigma^-1

    # Costruisco la matrice più piccola da invertire
    I = np.eye(X.shape[1])
    S = I + X.T @ sigma_X

    # Risolvo il sistema usando la matrice più piccola
    temp = np.linalg.solve(S, X.T @ sigma_B)

    # Applico la correzione di Woodbury
    result = sigma_B - sigma_X @ temp

    # Se B era un vettore restituisco un vettore
    if vettore:
        return result.ravel()

    return result


def sherman_morrison(A_inv, u, v):
    # Conosco già A^-1 e voglio trovare l'inversa di A + u v^T
    # Uso Sherman-Morrison per non invertire tutta la matrice

    u = np.asarray(u).reshape(-1, 1)
    v = np.asarray(v).reshape(-1, 1)

    # Formula:
    # (A + u v^T)^-1 = A^-1 - (A^-1 u v^T A^-1) / (1 + v^T A^-1 u)

    # Calcolo i prodotti che mi servono
    primo = A_inv @ u
    secondo = v.T @ A_inv

    # Calcolo il denominatore della formula
    denominatore = 1 + (v.T @ primo).item()

    # Se il denominatore è zero la nuova matrice non è invertibile
    if abs(denominatore) < 1e-12:
        raise ValueError("Matrix is singular")

    # Calcolo il termine da sottrarre alla vecchia inversa
    correzione = (primo @ secondo) / denominatore

    # Ottengo la nuova inversa
    result = A_inv - correzione

    return result


def logdet_rank_one_update(logdet_A, A_inv, u, v):
    # Voglio aggiornare il logaritmo del determinante
    # dopo aver aggiunto u v^T alla matrice A

    u = np.asarray(u).reshape(-1, 1)
    v = np.asarray(v).reshape(-1, 1)

    # Formula del determinante:
    # |A + u v^T| = (1 + v^T A^-1 u) * |A|
    #
    # Con il logaritmo il prodotto diventa una somma:
    # log|A + u v^T| = log|A| + log(1 + v^T A^-1 u)

    # Calcolo prima A^-1 u
    temp = A_inv @ u

    # Calcolo il fattore che modifica il determinante
    fattore = 1 + (v.T @ temp).item()

    # Il logaritmo reale del fattore richiede un valore positivo
    if fattore <= 0:
        raise ValueError("Invalid determinant update")

    # Sommo il logaritmo del fattore al vecchio log-determinante
    result = logdet_A + np.log(fattore)

    return result