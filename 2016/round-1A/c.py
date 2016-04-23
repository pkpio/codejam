from common import *
import networkx as nx

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

    cycles = list(nx.simple_cycles(DG))
    mx = 0
    mx2 = 0
    for cyc in cycles:
        l = len(cyc)
        if l == 2:
            mx2 += l + getTwigLen(DG.copy(), cyc)
        else:
            mx = max(l, mx)
    writeLine('Case #{}: {}'.format(t+1, max(mx, mx2)))
done()