from common import *

#setInOut('C-small-practice.in','C-small-practice.out')
#setInOut('B-large-practice.in','B-large-practice.out')

import networkx as nx
import matplotlib.pyplot as plt

def maxInPathLen(DG, root):
    pres = DG.predecessors(root)
    if len(pres) == 0:
        return 0
    return 1 + max([maxInPathLen(DG, pre) for pre in pres])

def getTwigLen(DG, cyc):
    DG.remove_edge(cyc[0], cyc[1])
    DG.remove_edge(cyc[1], cyc[0])
    return maxInPathLen(DG, cyc[0]) + maxInPathLen(DG, cyc[1])

T = readInt()
for t in range(T):
    N = readInt()
    BFF = readIntArr()

    DG=nx.DiGraph()
    DG.add_edges_from([(a,BFF[a]-1) for a in range(N)])
    nx.draw(DG)
    plt.show()

    cycles = list(nx.simple_cycles(DG))
    mx = 0
    for cyc in cycles:
        l = len(cyc)
        l = l + getTwigLen(DG.copy(), cyc) if l == 2 else l
        mx = l if l>mx else mx
    writeLine('Case #{}: {}'.format(t+1, mx))