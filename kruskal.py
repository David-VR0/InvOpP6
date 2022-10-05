Nodo = dict()
resultado = {}

def Make_set(vertice):
    #Array para almacenar aristas marcadas
    Nodo[vertice] = vertice

def Find_set(vertice):
    #busca si los vertices ya estan conectados
    if Nodo[vertice] != vertice:
        Nodo[vertice] = Find_set(Nodo[vertice])
    return Nodo[vertice]

def Union(u, v):
    Dato1 = Find_set(u)
    Dato2 = Find_set(v)
    Nodo[Dato1] = Dato2 # marca una arista

def Kruskal(grafo):
    resultante = []
    cont = 1

    for vertice in grafo['A']:
        Make_set(vertice)

    # Se ordena la lista por las millas de menor a mayor
    Ordenada = list(grafo['B'])
    Ordenada.sort()
    Ordenada = [(a,b,c) for c,a,b in Ordenada]
    print ("==============================")
    print ("Datos Ordenados")
    print ("==============================")
    print ("Ordenados:",Ordenada)
    Ordenada = [(c,a,b) for a,b,c in Ordenada]


    for Dato in Ordenada:

        peso, u, v = Dato    #dato = ( Millas, Area, Area)
        if Find_set(u) != Find_set(v):  # Verifica que no se forme un ciclo
            resultante.append(Dato)
            print ("==============================")
            print ("Paso:",cont)
            print ("==============================")
            resultante = [(a,b,c) for c,a,b in resultante]
            print ("Resultante: ",resultante)
            resultante = [(c,a,b) for a,b,c in resultante]
            cont+=1
            Union(u, v)# guarda los nodos unidos
    return resultante

grafo = {
        # A = Nombre de los nodos
        # B  (Millas , Nodo , Nodo)
        'A': ['1','2','3','4','5','6'],
        'B': [(1, '1', '2'),
              (9, '1', '5'),
              (7, '1', '4'),
              (4, '2', '4'),
              (3, '2', '5'),
              (5, '3', '4'),
              (6, '2', '3'),
              (10, '3', '6'),
              (5, '1', '3'),
              (3, '4', '6'),
              (8, '4', '5')
            ]
        }

resultante = Kruskal(grafo)
resultante = [(a,b,c) for c,a,b in resultante]
millas=0
lista=[]
for origen,destino,milla in resultante:
    millas=milla+millas

print ("\n=========Resultados=========")
print ("Longitud optima del cableado sera:")
print(millas, " [Millas]")
print ("==============================")