# Bigdata_hw_graphDB

**Part 1: Graph Database Warm Up**

1-1: Create Movie-Actor-Director Graph

\- Download HW3 homework material from link provided by TA.

[https://drive.google.com/open?id=0B9FZwuS86xaIRHBqQ1o5MHRkSDg Links to an external site.](https://drive.google.com/open?id=0B9FZwuS86xaIRHBqQ1o5MHRkSDg)

\- Open Graphen Database User Interface to build Movie-Actor-Director graph, and inject movie-actor-director datasets into graph database.

\- Try to use SearchByProperty, EgoNet, ShortestPath, GetSubgraph function to explore the graph.

1-2: Graph Query Language:

\- Try three graph queries to find relevant terms. Currently, the Graphen Database supports one-hop PGQL.

**Part 2: Graph Topology Analysis**

2-1: Calculate Centralities

\- Vertex Degree: Find out who is the most prolific actor(s).

\- Vertex Neighbors: Find the actor(s) whose movies earns highest profit in total.

•Profit = Revenue - Budget

Use ego_net to choose a subgraph (around 50 vertices), in this subgraph:

\- Find out who is the most "important" director(s) by measuring his/her betweenness.

\- Find out who is the most "important" director(s) by measuring his/her closeness.

**Part 3: Graph ML Learning API**

\- Use Machine Learning API to train a rating predictor model fed with movie vertices data.

• Add at least two new features extracted from the graph.

**Part 4: Build your own graph**

4-1: Wikipedia knowledge graph

-Download Wikipedia pagelink dataset from this link. [https://dumps.wikimedia.org/enwiki/20171001/  (Links to an external site.)Links to an external site.](https://dumps.wikimedia.org/enwiki/20171001/%20)

-Inject it into graph database.

-Show some result/visualizations of your analysis or queries.

-Note: Due to huge size of this dataset, you are allowed to

\1. Use wikipedia pagelink dataset of other language.

\2. Choose a part of English pagelink dataset.

4-2: Use your own dataset Download your own datasets.

-Inject it into graph database.

-Show some result/visualizations of your analysis or queries.