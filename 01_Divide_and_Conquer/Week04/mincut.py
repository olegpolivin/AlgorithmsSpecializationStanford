import numpy as np
# Example 1
g = {}
g[1] = [2,3,4]
g[2] = [1,3]
g[3] = [1,2,4]
g[4] = [1,3]

minVal = []

def EdgeContraction(g,j):
    print(g)
    c1, c2 = np.random.choice(list(g.keys()), size = 2, replace=False) # Choose vertices to contract
    print(c1,c2)
    g[j] = list(set(g.get(c1,[])+g.get(c2,[])))
    for k,v in g.items():
        g[k] = [i for i in v if (i==c1)| (i==c2)]
    g.pop(c1)
    g.pop(c2)

for i in range(2):
    g = {}
    g[1] = [2,3,4]
    g[2] = [1,3]
    g[3] = [1,2,4]
    g[4] = [1,3]

    # g[1] = [2,3,4]
    # g[2] = [1,3]
    # g[3] = [1,2,4]
    # g[4] = [1,3]
    # g[1] = [2,5]
    # g[2] = [1,3]
    # g[3] = [2,4]
    # g[4] = [3,5]
    # g[5] = [4,6]

    # f = open("kargerMinCut.txt", "r")
    # g = {}
    # with open("kargerMinCut.txt") as fp:
    #     for line in fp:
    #         line = fp.readline().rstrip().split('\t')
    #         line = [int(i) for i in line]
    #         g[line[0]] = line[1:]

    #print(np.random.choice(g.keys(), size = 2, replace=False))

    j = len(g) + 1

    while len(g) > 2:
        EdgeContraction(g,j)
        j = j+1
    print(g)
    mincutVal = 10000
    for v in g.values():
        mincutV = len(v)
        if mincutV<mincutVal:
            mincutVal = mincutV
        
    minVal.append(mincutVal)

# print(minVal)
print(min(minVal))
print(g)