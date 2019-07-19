import numpy as np

# class Graph:

#     def __init__(self,g):

#         self.g = g

# class Vertice:


# class Edge

# g = {}
# g[1] = [2,3,4]
# g[2] = [1,3]
# g[3] = [1,2,4]
# g[4] = [1,3]

minV = []

def choose2nodes(nodes,ConnectedTo):
    
    c1 = int(np.random.choice(nodes, size = 1))
    c2 = int(np.random.choice(ConnectedTo[c1],size = 1))

    return c1,c2

def EdgeContraction(g,g_,contracted,j):
    # print(j,g)
    # # print(g)
    # print('Here',g_)
    # print(contracted)
    c1, c2 = choose2nodes(list(g.keys()),contracted)
    # print(c1,c2)
    g[j] = g[c1] + g[c2]
    if c1 in g.keys():
        l1 = [c1]
    else:
        l1 = g_[c1]

    if c2 in g.keys():
        l2 = [c2]
    else:
        l2 = g_[c2]
    contracted[j] = contracted[c1]+contracted[c2]
    g.pop(c1)
    g.pop(c2)
    contracted.pop(c1)
    contracted.pop(c2)
    
    #contracted = g.copy()

    # print(g)
    
    for k,value in contracted.items():
        if k == j:
            value = [v for v in value if (v!=c1)&(v!=c2)]
            contracted[k] = value
        else:
            value = [v if (v!=c1)&(v!=c2) else j for v in value]
            contracted[k] = value
    # print('Contraction',contracted)
    g_[j] = l1 + l2

    # print('Hereafter', (g_))
    list_of_vertices = g_[j]
    g[j] = [i for i in g[j] if i not in list_of_vertices]

for k in range(50000): 
    g = {}
    with open("kargerMinCut.txt") as fp:
        for line in fp:
            #line = line.split(' ')
            line = line.rstrip().split('\t')
            line = [int(i) for i in line]
            g[line[0]] = line[1:]
    # g = {}
    # g[1] = [2,3,4]
    # g[2] = [1,3]
    # g[3] = [1,2,4]
    # g[4] = [1,3]
    j = len(g) +1
    g_ = g.copy()
    contracted = g.copy()
    BigG = len(g)
    while len(g)>2:
        EdgeContraction(g,g_,contracted,j)
        j = j + 1

    A = int(list(g.keys())[0])
    B = int(list(g.keys())[1])

    # if A>BigG:
    #     value = [i for i in g[A] if i not in g[B]]
    #     g[A] = value
    
    # if B > BigG:
    #     value = [i for i in g[B] if i not in g[A]]
    #     g[B] = value

    
    minval=5000
    for i in contracted.values():
        if len(i)<minval:
            minval=len(i)
    minV.append(minval)
    
    if k%5000==0:
        print(k,min(minV))

print(min(minV))
# print(g_)
# print(contracted)
# print(g)