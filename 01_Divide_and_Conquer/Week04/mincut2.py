import numpy as np
# Example 1
# g = {}
# g[1] = [2,3,4]
# g[2] = [1,3]
# g[3] = [1,2,4]
# g[4] = [1,3]

# print(g)
# c1, c2 = np.random.choice(list(g.keys()), size = 2, replace=False) # Choose vertices to contract
# print(c1,c2)
c = {}
def EdgeContraction(g, j, c):

    c1, c2 = np.random.choice(list(g.keys()), size = 2, replace=False) # Choose vertices to contract
    # print(g)
    # print(c1,c2)
    g[j] = g.get(c1)+g.get(c2)
    c[j] = [c1,c2]
    #g[j] = [i for i in g[j] if i not in c]
    g.pop(c1)
    g.pop(c2)
minVal = []

for i in range(10000):
    g = {}
    with open("kargerMinCut.txt") as fp:
        for line in fp:
            #line = line.split(' ')
            line = line.rstrip().split('\t')
            line = [int(i) for i in line]
            g[line[0]] = line[1:]
    j = len(g)
    #j = len(g)+1
    #print(np.random.choice(g.keys(), size = 2, replace=False))
    while len(g)>2:
        EdgeContraction(g,j,c)

        j = j+1
        # print(g) 

    for key,value in c.items():
        for v in value:
            if v in c.keys():
                c[key] = c[v] + c[key]

    for k,value in c.items():
        if k in g.keys():
            g[k] = [i for i in g[k] if i not in value]

    mincutVal = 10000
    for v in g.values():
        mincutV = len(v)
        if mincutV<mincutVal:
            mincutVal = mincutV


    minVal.append(mincutVal)
    
    minV = 10000
    if i%200==0:
        if min(minVal)<minV:
            minV = min(minVal)
            print(i,minV)

    # print(g)

print(min(minVal))
# print(c)
# print(g)