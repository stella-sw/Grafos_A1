import sys
from collections import deque
import A1_1 as G_bib

arquivo = sys.argv[1]
indice_s = int(sys.argv[2])

grafo = G_bib.Grafo(arquivo=arquivo)

def hierholzer(grafo: G_bib.Grafo):
    if (grafo.qtdArestas() == 0):
        return (True, [])
    
    num_vertices = grafo.qtdVertices()

    C = [[0 for x in range (num_vertices + 1)] for x in range (num_vertices + 1)]

    for u in range(1, num_vertices + 1):
        for v in range(1, num_vertices + 1):
            C[u][v] = len(grafo.Adj[u][v])
            C[v][u] = len(grafo.Adj[v][u])

    v = None

    for k in range(1, num_vertices + 1):
        if grafo.grau(k) > 0:
            v = k
            break
    
    r, Ciclo = buscarSubciclo(grafo, v, C)

    if (r == False):
        return (False, None)
    
    for u in range(1, num_vertices+1):
        for v in range(1, num_vertices+1):
            if C[u][v] > 0:
                return(False, None)
            
    return(True, Ciclo)

def buscarSubciclo(grafo: G_bib.Grafo, v, C):
    Ciclo = [v]
    t = v

    while (True):
        u = None
        for w in grafo.vizinhos(v):
            if C[v][w] > 0:
                u = w
                break
        if (u is None):
            return (False, None)
        
        C[u][v] -= 1
        C[v][u] -= 1

        v = u
        Ciclo.append(v)

        if (v == t):
            break

    num_vertices = grafo.qtdVertices()

    for u in Ciclo:
        for w in grafo.vizinhos(u):
            if C[u][w] > 0:
                r, Ciclo_interno = buscarSubciclo(grafo=grafo, v=u, C=C)

                if r == False:
                    return (False, None)

                inserir = Ciclo.index(u)

                if Ciclo_interno is not None:
                    for x in Ciclo_interno[1:]:
                        Ciclo.insert(inserir, x)
                        inserir += 1
    return (True, Ciclo)