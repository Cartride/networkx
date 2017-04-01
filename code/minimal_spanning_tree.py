#coding:utf-8
import networkx as nx
import show_graph
#此段代码解决 1.matplotlib中文显示问题 2 '-'显示为方块问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
inf = 0xffffffff
graph = []
N = 200

def init():
    global graph
    [graph.append([inf for i in range(N)]) for j in range(N)]

def prim(s,n,G):
    d = [graph[s][i] for i in range(n+1)]
    vis = [False for i in range(n+1)]
    pre = [s for i in range(n+1)]
    cost = 0
    d[s] = 0
    vis[s] = True
    for i in range(n):
        MIN = inf
        for j in range(n+1):
            if MIN > d[j] and not vis[j]:
                MIN = d[j]
                s = j
        G.remove_edge(pre[s],s)
        G.add_edge(pre[s],s,weight=0,label=MIN)
        vis[s] = True
        cost+=MIN
        for j in range(n+1):
            if graph[s][j] < d[j] and not vis[j]:
                d[j] = graph[s][j]
                pre[j] = s
    return cost

if __name__=='__main__':
    datas = [(0,1,1),(0,9,6),(0,8,5),(0,2,2),(1,2,3),(2,3,1),(3,4,2),(3,6,2),(4,5,2)\
    ,(5,6,1),(6,8,4),(7,8,1),(7,9,2)]
    G = nx.Graph()
    edge_datas = [(u,v) for (u,v,w) in datas]
    G.add_edges_from(edge_datas,weight = 1,label='')
    init()
    n = 0
    s = inf
    for (u,v,w) in datas:
        s = min(s,min(u,v))
        n = max(n,max(u,v))
        graph[u][v] = graph[v][u] = w
    cost = prim(s,n,G)
    title = "prim算法:最小生成树\n最小生成树权值{0}".format(cost)
    pos = nx.spring_layout(G)
    show_graph.show(G=G,pos=pos,title=title,photo_name='minimal_spanning_tree')
