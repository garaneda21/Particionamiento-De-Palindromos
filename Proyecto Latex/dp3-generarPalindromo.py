def generarPalindromo(string):
    n = len(string)

    P = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        P[i][i] = True

    for L in range(2, n+1):

        for i in range(n-L+1):
            j = i + L - 1

            if string[i] == string[j] and (P[i+1][j-1] or L == 2):
                P[i][j] = True

    return P
