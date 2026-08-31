import sys
from collections import deque
import A1_1 as G_bib

arquivo = sys.argv[1]
indice_s = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)

def buscaLargura(grafo: G_bib.Grafo, origem):
    C = [False]*(grafo.qtdVertices() + 1)
    D = [float('inf')]*(grafo.qtdVertices() + 1)
    A = [None]*(grafo.qtdVertices() + 1)
    C[origem] = True
    D[origem] = 0
    print(f'0: {origem}')
    Q = deque()
    Q.append(origem)
    while (len(Q) > 0):
        u = Q.popleft()
        nivel = []
        for v in grafo.vizinhos(u):
            if (C[v] == False):
                C[v] = True
                D[v] = D[u] + 1
                A[v] = u
                Q.append(v)
                nivel.append(v)
        print(f'{D[u]+1}: {", ".join(nivel)}')
    return (D, A)

D, A = buscaLargura(grafo, indice_s)
