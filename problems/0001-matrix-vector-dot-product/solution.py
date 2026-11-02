def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
	if (len(a) != len (b)):
		return -1
	risultato = []
	for i in range(len(a)):
		riga = a[i]
		prodotto=0
		for el in range(len(riga)):
			prodotto = prodotto + riga[el] * b[el]
		risultato.append(prodotto)
	return risultato

	



			