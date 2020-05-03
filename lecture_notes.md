# Coursera lecture notes

In math, a graph is made up of:
1. Vertices
Or nodes/hubs.
2. Edges.
Or links.

In practice we extend the model to increase graph functionality.
1. Nodes.
2. Edges.
3. Node types.
4. Assign types to nodes.
5. Edge types.
6. Assign types to edges.
7. Node attributes.
8. Edge attributes.
9. Edge weights.
Edge weights can represent different things. For instance, in a travel graph, where nodes represent destinations, weights can represent the distance between each destination.

Definitions:
1. Multigraph.
When each node can be linked by more than 1 edge.
2. Walk.
An alternate sequence of nodes and edges.
3. Path.
A walk where no nodes except the first and last are allowed to repeat.
4. Cycle.
A path of len >= 3 whose start and end nodes are the same. A graph with no cycles is said to be acyclic.
5. Trail.
A walk with no repeating edge. If the graph is not a multigraph, this will also be a path.
6. Reachability.
Node A is said to be reachable from Node B if a path from A to B exists. Reachability is not always symmetric since edges can be one directional.
7. Diameter.
The diameter of a graph is the largest of the shortest route distances between two nodes within the graph. Distance can be number of edges, or if the edges have weights, the sum of edge weights depending on what is required.

## Path analytics
Path analytics is concerned with the question "What is the best path?"

In general, 4 things need to be taken note of when answering this question:
1. Function to optimize.
In other words, what to maximize or minimize. In a graph of routes as edges and destinations as nodes, we might want to minimize travel distance, for instance.
2. Nodes or edges that must be included.
3. Nodes or edges that must be avoided.
2 & 3 are known as constraints.
4. Preferences.

### Dijkstra's algorithm
An algorithm that systematically calculates the shortest weighted path from the origin node to each other node until the target is reached.
* Poor scaling.
To mitigate this, variants are used.
* Bi-directional variant starts from both ends and ends when both starts meet.
* Goal directed variant uses information about the end destination to modify weights. Significantly improves algorithm speed in practice and is used by many online mapping apps.

## Connectivity analytics
Connectivity analytics is concerned with the question "How robust is the graph." Connectivity being the presence of a path between every connected node, and robustness being how resistant the connectivity of the graph is to the removal of nodes or edges.

### Definitions
1. Strongly connected
Means a directed path exists between every node.
2. Weakly connected
Means path exists between every node assuming all edges are bi-directional.
3. Connectivity
Aside from the definition earlier, the connectivity of a graph can be split into node connectivity and edge connectivity. These are defined as the minimum number of nodes/edges that need to be removed to break the graph into two (or more?) parts, each having multiple components.
4. Connectedness
Connectedness of a node is measured in degrees, which is the number of edges into and out of a node. Splitting the two gets you indegree and outdegree. Nodes with high connectivity are potential network vulnerabilities as their removal leads to many disconnections. Plotting count (y) vs degrees (x) as a histogram can be used to measure the similarity between two graphs. Connectedness can also be plotted as a 2d heatmap of outdegree (y) indegree (x) which can give additional insight to graph distributions.
5. Power law
A model of distributions of node degrees that is commonly found in nature.

## Community analytics
Community analytics is concerned with analysis of clusters within graphs.

### Types

Static analysis
* Number of communities.
* Community members.
* How close each community is.

Temporal (time) analysis
* When a community is formed.
* Community stability.
* Why a community is formed or dissolves.

Predictive analysis
* Community growth potential.
* Community going concern.
* If dominant members will appear in a community.

### Community detection

Communities can be detected by comparing the degree connectivity of cluster members with degree connectivity of cluster member to outsiders. There are two general ways of detecting communities:
1. Distance.
Central to distance based measures is the concept of a clique, defined later.
2. Density.

Clique
A clique is a community whereby all member nodes are linked to each other by edges. In reality, perfect cliques are hard to find, thus near cliques are found instead:
1. n-clique.
A n-clique is one where the maximum distance between each node is not more than n. In a perfect clique, n=1.
2. n-clan.
A n-clan is one where the diameter of the clan is no greater than n. Probably a better measure than n-clique.

k-core
k-core is a method if defining communities through density. In k-core, every node is connected to at least k other nodes in the community. The connection need not be direct. As such, when k=1, the subgraph is completely detached from every other non-community node in the graph.
