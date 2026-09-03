import sys
import A1_1 as G_bib

def algoritmoBellmanFord(grafo: G_bib.Grafo, origem: int):
    num_vertices = grafo.qtdVertices()
    
    # inicialização
    # usei como referencia um código em C++, onde dist e pred eram ponteiros
    # adaptei para o uso de decionários do Python
    dist = {i: float('inf') for i in range(1, num_vertices + 1)}
    pred = {i: None for i in range(1, num_vertices + 1)}
    dist[origem] = 0
    
    # relaxamento
    for _ in range(num_vertices - 1):
        for u in range(1, num_vertices + 1):
            # Para cada vértice u olha para os vizinhos v
            for v in grafo.vizinhos(u):
                w = grafo.peso(u, v)
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    pred[v] = u
                    
    #  verificação de ciclos negativos
    # se ainda for possível relaxar alguma aresta significa que há um ciclo negativo
    for u in range(1, num_vertices + 1):
        for v in grafo.vizinhos(u):
            w = grafo.peso(u, v)
            if dist[u] + w < dist[v]:
                print("Erro: O grafo contém um ciclo de peso negativo alcançável a partir da origem.")
                return 
            
    # saida esperada dos resultados
    for destino in range(1, num_vertices + 1):
        if dist[destino] == float('inf'):
            continue
            
        caminho = []
        atual = destino
        
        while atual is not None:
            caminho.append(atual)
            if atual == origem:
                break
            atual = pred[atual]
            
        caminho.reverse()
        str_caminho = ",".join(map(str, caminho))
        
        distancia = int(dist[destino]) if dist[destino].is_integer() else dist[destino] 
        print(f"{destino}: {str_caminho}; d={distancia}")