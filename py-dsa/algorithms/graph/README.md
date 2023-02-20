# Graph Algorithms
- There is a class of computational problems that can be best represented in terms of graphs. Such problems can be solved using a class of algorithms called **graph algorithms**.
- Using graph algorithms is one of the most efficient ways of searching for information in complex, interconnected data structures that are linked through meaning full relationships.
- In the era of big data, social media, and distributed data, such techniques are becoming increasingly important and useful.

## Representations of graphs
- A graph is a structure that represents data in terms of vertices and edges. A graph is represented as `aGraph = (𝓥, 𝓔)`, where `𝓥` represents a set of vertices and `𝓔` represents a set of edges. Note that `aGraph` has `|𝓥|` vertices and `|𝓔|` edges.
- A vertex, `𝓋 ∈ 𝓥`, represents a real-world object, such as a person, a computer, or an activity. An edge, `𝓋 ∈ 𝓔`, connects two vertices in a network:
  - `e(𝓋1, 𝓋2)|(e ∈ 𝓔) & (𝓋i ∈ 𝓥)`
- The preceding equation indicates that in a graph, all edges belong to a set `𝓔`, and all vertices belong to a set `𝓥`.

### Types of graphs
- Graphs can be classified into four kinds, namely the following:
  - Undirected graphs
  - Directed graphs
  - Undirected multi-graphs
  - Directed multi-graphs
#### Undirected graphs
- In most cases, the relationships that the constituent nodes of a graph represent can be thought of as undirectional.
- Such relationships do not impose any order on the relationship. Such edges are called **undirected edges** and the resultant graph is called an **undirected graph**

![undirected_graphs.png](_resources/images/undirected_graphs.png)
- For example:
  - Mike and Annie know each other
  - Node **A** and Node **B** are connected (this is a peer-to-peer connection)

#### Directed graphs
- A graph where the relationship between the nodes in the graph has some sense of direction is called a **directed graph**.
![directed_graphs.png](_resources/images/directed_graphs.png)
- For example
  - Mike and his house (Mike lives in a house, but his house does not live in Mike)
  - John manages Paul (John is manager of Paul)

#### Undirected multi-graphs
- Nodes have more than one type of relationship between them. In that case, there can be more than one edge connecting the same two nodes.
- These kinds of graphs, where multiples parallel edges are allowed on the same nodes, are called **multigraphs**. We have to explicitly indicate whether a particular graph is a multigraph or not. Parallel edges may represent different types of relationships between the nodes.
![undirected_multigraphs.png](_resources/images/undirected_multigraphs.png)
- For example, Mike and John are classmates are well as co-workers.

#### Directed multi-graphs
- If there is a directional relationship between nodes in a multigraph, we call it a **directed multigraph**.
![directed_multigraphs.png](_resources/images/directed_multigraphs.png)
- For example, Mike reports to John in the office, and John teaches Mike the Python programming language.

### Special types of edges
- Edges connect various vertices of a graph together and represent the relationship between themselves. In addition to simple edges, they can be of the following special types:
  - **Self-edge**: A particular vertex can have a relationship with itself. For example, John transfer money from his business account to his personal account. Such a special relationship can be represented by a self-directed edge.
  - **Hyper-edge**: More than one vertex is connected by the same edge. An edge that connects more than one vertex to represent such a relationship is called a hyper-edge. For example, suppose all three of Mike, John, and Sarah are working on one specific project.
![self_and_hyper_edge.png](_resources/images/self_and_hyper_edge.png)

### Ego-centered networks

## Introducing network analysis theory

## Understanding graph traversals

## Case study - fraud analytics