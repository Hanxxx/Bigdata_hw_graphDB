import networkx as nx
import numpy
import csv
def checkif():
    f = open("/home/hl3069/HW3/movie_vertice.csv", "r")
    f2 = open("/home/hl3069/HW3/director_vertice.csv", "r")
    r1 = csv.reader(f)
    r2 = csv.reader(f2)
    cnt = -1
    id1 = []
    for line in r1:
        cnt += 1
        if cnt == 0:
            continue
        id1.append(line[2])
    f.close()
    cnt = -1
    id2 = []
    for line in r2:
        cnt += 1
        if cnt == 0:
            continue
        id2.append(line[0])
    f2.close()
    for i in id1:
        for j in id2:
            if i == j:
                print i
                return
def load_movie():
    f = open("/home/hl3069/HW3/movie_vertice.csv", "r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1
        if cnt == 0:
            continue
        G.add_node(line[2], budget = int(line[0]), genres = line[1], keywords = line[3], 
                popularity = float(line[4]), revenue = int(line[5]), runtime = int(line[6]), 
                title = line[7], vote_average = float(line[8]), vote_count = int(line[9]), label = "MOVIE")

    f.close()
def load_actor():
    f = open("/home/hl3069/HW3/actor_vertice.csv", "r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1
        if cnt == 0:
            continue
        G.add_node(line[0], name = line[1], gender = line[2], label = "ACTOR")
    
    f.close()

def load_director():
    f = open("/home/hl3069/HW3/director_vertice.csv", "r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1
        if cnt == 0:
            continue
        G.add_node(line[0], name = line[1], gender = line[2], label = "DIRECTOR")
    f.close()
def load_act_edge():
    f = open("/home/hl3069/HW3/actor_edge.csv", "r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt =+ 1
        if cnt == 0:
            continue
        if (line[0] in G.nodes) and (line[1] in G.nodes):
            if (G.node[line[0]]["label"] == "MOVIE") and (G.node[line[1]]["label"] == "ACTOR"):
                G.add_edge(line[0], line[1], label = 'ACT')
    f.close()
def load_dir_edge():
    f = open("/home/hl3069/HW3/director_edge.csv", "r")
    reader = csv.reader(f)
    cnt = -1
    for line in reader:
        cnt += 1
        if cnt == 0:
            continue
        if (line[0] in G.nodes) and (line[1] in G.nodes):
            if (G.node[line[0]]["label"] == "MOVIE") and (G.node[line[1]]["label"] == "DIRECTOR"):
                G.add_edge(line[0], line[1], label = 'DIR')
    f.close()
G = nx.Graph()
#checkif()
load_movie()
load_actor()
load_director()
load_act_edge()
load_dir_edge()

#print '43434' in G.nodes
max_profit = 0
mp_actor = []
for node in G.nodes:
    if G.node[node]["label"] == "ACTOR":
        total_p = 0
        for p in G.neighbors(node):
            if G.node[p]["label"] == "MOVIE":
                profit = G.node[p]["revenue"] - G.node[p]["budget"]
                total_p += profit
        G.node[node]["profit"] = total_p
        if max_profit < total_p:
            max_profit = total_p
            mp_actor = [node]
        elif max_profit == total_p:
            mp_actor.append(node)
print "----Actor with the most total profit----"
for i in mp_actor:
    print "Name:", G.node[i]["name"], "Profit:", G.node[i]["profit"]
print "Use james cameron as center to build a ego net with Depth = 3"
sub_g = nx.ego_graph(G, "2710", 3)
n = nx.betweenness_centrality(sub_g)
max_b = 0
mb_dir = []
print "----Director with the most betweenness----"
for i in n:
    if G.node[i]["label"] == "DIRECTOR":
        if n[i] > max_b:
            max_b = n[i]
            mb_dir = [i]
        elif n[i] == max_b:
            mb_dir.append(i)
for i in mb_dir:
    print "Name:", G.node[i]["name"]
print "----Director with the most closeness----"
n = nx.closeness_centrality(sub_g)
max_c = 0
mc_dir = []
for i in n:
    if G.node[i]["label"] == "DIRECTOR":
        if n[i] > max_c:
            max_c = n[i]
            mc_dir = [i]
        elif n[i] == max_c:
            mc_dir.append(i)
for i in mc_dir:
    print "Name:", G.node[i]["name"]
