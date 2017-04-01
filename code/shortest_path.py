#coding:utf-8
import networkx as nx
import show_graph
#此段代码解决 1.matplotlib中文显示问题 2 '-'显示为方块问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

N = 100000
k = 0
inf = 0xffffffff
edge = []
head = []
use_id = []
pre = []
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
    global N,k,head
    head = [-1 for i in range(N)]
    k = 0

def spfa(s,t,n):
    global inf,edge,pre,use_id
    vis = [False for i in range(n+1)]
    d = [inf for i in range(n+1)]
    pre = [i for i in range(n+1)]
    use_id = [0 for i in range(n+1)]
    vis[s] = True
    d[s] = 0
    queue = [s]
    while queue:
        u = queue.pop(0)
        vis[u] = False
        now = head[u]
        while now!=-1:
            v = edge[now].v
            w = edge[now].w
            if d[u]+w < d[v]:
                d[v] = d[u]+w
                if not vis[v]:
                    vis[v] = True
                    queue.append(v)
                pre[v] = u
                use_id[v] = now
            now = edge[now].next
    return d[t] if d[t]!=inf else -1

if __name__ == '__main__':
    init()
    datas = [(1,2,1),(1,4,2),(1,3,1),(2,4,6),(2,9,7),(3,1,1),(3,4,5),(3,8,4),(8,3,4),(4,10,4),(4,5,10),(5,6,2),\
    (6,10,6),(8,5,1)]
    pos = 0
    for (u,v,w) in datas:
        pos = max(pos,max(u,v))
        add_edge(u,v,w)
    s = 1
    t = 5
    total = spfa(s,t,pos)
    G = nx.DiGraph()
    _datas = [(u,v) for (u,v,w) in datas]
    G.add_edges_from(_datas,weight=1,label='')
    path = []
    temp = t
    while temp!=s:
        e = edge[use_id[temp]]
        G.remove_edge(e.u,e.v)
        G.add_edge(e.u,e.v,weight=0,label="{2}:{0}<-{1}".format(e.v,e.u,e.w))
        path.append(str(temp))
        temp = pre[temp]
    path.append(str(s))
    e_origin=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] ==1] # 不在最短路中的edge
    e_shortest =[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] ==0] # 最短路中的edge
    #ER随机图
    pos = nx.shell_layout(G)
    title = "SFPA算法:从{0}号点到{1}号点的最短路\nTotal-Length={2}\nPath:{3}".format(s,t,total,"->".join(reversed(path)))

    show_graph.show(G=G,pos=pos,title=title,photo_name='shortest_path')
