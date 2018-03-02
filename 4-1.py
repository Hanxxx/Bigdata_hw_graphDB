import networkx as nx
import csv
import matplotlib.pyplot as plt
def load_from():
    f = open("from.csv","r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1
        if cnt == 0:
            continue
        G.add_node(line[0])
        
    f.close()
def load_title():
    f = open("title.csv", "r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1 
        if cnt == 0:
            continue
        G.add_node(line[0])
    f.close()

def load_link():
    f = open("pagelinks.csv", "r")
    reader =  csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1
        if cnt == 0:
            continue
        G.add_edge(line[0], line[1])
    f.close()

G = nx.Graph()
load_from()
load_title()
load_link()
plt.subplot(121)
nx.draw(G, with_labels=False, font_weight='bold')
plt.show()