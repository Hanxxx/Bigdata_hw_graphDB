import networkx as nx
import urllib2
import matplotlib.pyplot as plt
homer = urllib2.urlopen('http://people.sc.fsu.edu/~jburkardt/datasets/sgb/homer.dat')
def read_nodes(gfile):
    s = gfile.readline()[0:2]
    #skip the first 4 lines.
    while(s != "AA"):
        s = gfile.readline()[0:2]
    nodes = []
    nodes.append(s)
    while(s != "9Z"):
        s = gfile.readline()[0:2]
        nodes.append(s)
    print "node number after read: ", len(nodes)
    return nodes
def read_edges(gfile):
    gfile.readline()
    e = []
    while(True):
        s  = gfile.readline()
        if(s[0]=="*"):
            break
        #print s
        s = s[:-1]
        s = s.split(":")
        #print s
        s = s[1]
        #print s
        p = s.split(";")
        #print "p is ",p
        for i in p :
            pp =i.split(',')
            #print "this is PP : %s", pp
            pplen = len(pp)
            for j in range(0,pplen):
                for k in range(j+1,pplen):
                    #print "this edge is :", [pp[j],pp[k]]
                    if not (([pp[j],pp[k]] in e)or([pp[k],pp[j]] in e)):
                        e.append([pp[j],pp[k]])

    print "edge num after read: ", len(e)
    return e

G = nx.Graph()
G.add_nodes_from(read_nodes(homer))
G.add_edges_from(read_edges(homer))
sub = nx.ego_graph(G, "HL")
plt.subplot(121)
nx.draw(sub, with_labels=True, font_weight='bold')
plt.show()