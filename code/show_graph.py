#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
import os
#此段代码解决 1.matplotlib中文显示问题 2 '-'显示为方块问题
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def show(G,pos=None,title=None,photo_name='picture'):
    if pos is None:
        pos = nx.shell_layout(G)
    e_1 =[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] ==1] # 普通边
    e_2 =[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] ==0] # 利用的边
    # Draw nodes
    nx.draw_networkx_nodes(G,pos,node_size=300, node_color='orange')
    # Draw Edges
    nx.draw_networkx_edges(G,pos,edgelist=e_1,width=1, alpha = 1,edge_color='g',style='dashed')
    nx.draw_networkx_edges(G,pos,edgelist=e_2, width=3,alpha=0.6,edge_color='b')
    edge_labels =dict([((u, v), d['label']) for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(G,pos,font_size=10)
    plt.title(title)
    plt.axis('off')
    plt.savefig(photo_name)
    plt.show()
