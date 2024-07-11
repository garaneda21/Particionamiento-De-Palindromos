def generarPalindromo(string):
    n = len(string)

    P = [[False for i in range(n)] for i in range(n)]

    # Inicializar la matriz de palíndromos para un caracter
    for i in range(n):
        P[i][i] = True

    for L in range(2, n+1):

    # Todos los substrings que sean palindromos marcalos como tal
        for i in range(n-L+1):
            j = i + L - 1

            if string[i] == string[j] and (P[i+1][j-1] or L == 2):
                P[i][j] = True

    return P

def minCutDP(string):
    n = len(string)

    # Generar matriz P con substrings palindromos
    P = generarPalindromo(string)
    # Inicializar arreglo de Programacion dinamica
    # Con el número mínimo de cortes, todos como cortes infinitos
    minCortesDP = [float('inf')] * n

    # los substrings de largo 1 son palindromos y no nesesitan cortes.
    minCortesDP[0] = 0

    # iterar sobre todo el string desde el caracter 1 hasta el final
    for i in range(1, n):
        # comprobar si el substring desde 0 hasta i es palindromo
        # si es asi no nesesitca cortes, sino comprobar los sufijos
        if P[0][i]:
            minCortesDP[i] = 0
        else:
            # recorrer los sufijos desde el caracter actual i hasta 0
            # (el inicio del string) en reversa
            for j in range(i, 0, -1):
                # comprobar si el sufijo actual es palindromo, sino pasar al siguiente
                if P[j][i]:
                    # si es palindromo, comprobar si la cantidad de cortes nueva es optima
                    # si es asi, obtener la cantidad de cortes del substring anterior y sumarle un corte
                    if minCortesDP[j-1] + 1 < minCortesDP[i]:
                        minCortesDP[i] = minCortesDP[j-1] + 1

    # retornar cantidad minima de cortes almacenada en la pos [largo del string - 1]
    return minCortesDP[n-1]
