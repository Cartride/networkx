#coding:utf-8
import networkx as nx
import show_graph
#此段代码解决 1.matplotlib中文显示问题 2 '-'显示为方块问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
N = 100000
k = 0
linker = []
vis = []
edge = []
head = []
class Edge():
    def __init__(self,u,v,w=1):
        self.u = u
        self.v = v
        self.w = w
        self.next = None

def add_edge(u,v,w=1):
    global k
    e = Edge(u,v,w)
    e.next = head[u]
    edge.append(e)
    head[u] = k
    k+=1

def init():
    global N,k,head,linker
    head = [-1 for i in range(N)]
    linker = [-1 for i in range(N)]
    k = 0

def dfs(u):
    global edge,head,linker,vis
    now = head[u]
    while now!=-1:
        v = edge[now].v
        if not vis[v]:
            vis[v] = True
            if linker[v]==-1 or dfs(linker[v]):
                linker[v]= u
                return True
        now = edge[now].next
    return False
if __name__ == '__main__':
    datas = [(1,5),(3,7),(2,8),(3,6),(3,5),(4,7),(4,8)]
    init()
    n = 0
    for (u,v) in datas:
        n = max(n,max(u,v))
        add_edge(u=u,v=v) #单向边表示从左到右的匹配
    #匈牙利算法
    match = 0
    for i in range(n+1):
        vis = [False for j in range(n+1)]
        if dfs(i): match+=1
    print match
    G = nx.DiGraph()
    G.add_node(1,pos=(1,1))
    G.add_node(2,pos=(1,3))
    G.add_node(3,pos=(1,5))
    G.add_node(4,pos=(1,7))
    G.add_node(5,pos=(3,1))
    G.add_node(6,pos=(3,3))
    G.add_node(7,pos=(3,5))
    G.add_node(8,pos=(3,7))
    G.add_edges_from(datas,weight=1,label="")
    for i in range(n+1):
        if linker[i]!=-1:
            G.remove_edge(linker[i],i)
            G.add_edge(linker[i],i,weight =0,label='match')
    pos = nx.get_node_attributes(G,'pos')
    title = "匈牙利算法:二分图最大匹配\n最大匹配数{0}".format(match)
    show_graph.show(G=G,pos=pos,title=title,photo_name='bigraph_max_match')
