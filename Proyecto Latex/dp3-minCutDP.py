def minCutDP(string):
    n = len(string)

    P = generarPalindromo(string)
    minCortesDP = [float('inf')] * n

    minCortesDP[0] = 0

    for i in range(1, n):
        if P[0][i]:
            minCortesDP[i] = 0
        else:
            for j in range(i, 0, -1):
                if P[j][i]:
                    if minCortesDP[j-1] + 1 < minCortesDP[i]:
                        minCortesDP[i] = minCortesDP[j-1] + 1

    return minCortesDP[n-1]