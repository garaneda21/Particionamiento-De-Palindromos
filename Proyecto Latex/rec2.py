def palPart(string):
    n = len(string)

    C = [[0 for i in range(n)] for i in range(n)]
    P = [[False for i in range(n)] for i in range(n)]

    for i in range(n):
        C[i][i] = 0
        P[i][i] = True

    for L in range(1, n):
        for i in range(0, n - L):
            j = i + L

            if string[i] == string[j] and (P[i+1][j-1] or L == 1):
                C[i][j] = 0
                P[i][j] = True
            else:
                C[i][j] = float("inf")
                for k in range(i, j):
                    C[i][j] = min(C[i][j], 1 + C[i][k] + C[k+1][j])

    return C[0][n-1]