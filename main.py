def cykParse(R, w, simboloInicial):
    n = len(w)
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
    # Filling in the table
    for j in range(0, n):
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)
        for i in range(j, -1, -1):
            # Iterate over the range i to j
            for k in range(i, j):  # Change here
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        # If a terminal is found
                        if len(rhs) == 2 and \
                                rhs[0] in T[i][k] and \
                                rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
    # If word can be formed by rules
    # of given grammar
    if simboloInicial in T[0][n - 1]:
        print("yes")
    else:
        print("no")


def main():
    numGramaticas = int(input())
    for _ in range(numGramaticas):
        cantReglasYCadenas = input()
        n = [int(i) for i in cantReglasYCadenas.split()]
        G = {}
        simboloInicio = None
        j = 0
        while j < n[0]:
            regla = input()
            reglaSplit = regla.split()
            if simboloInicio is None:
                simboloInicio = reglaSplit[0]
            G[reglaSplit[0]] = []
            for i in range(1, len(reglaSplit)):
                G[reglaSplit[0]].append(reglaSplit[i])
            j += 1
        i = 0
        while i < n[1]:
            cadena = input()
            cykParse(G, cadena, simboloInicio)  # Pass start_symbol to cykParse
            i += 1


main()
