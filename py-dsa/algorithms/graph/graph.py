import networkx as nx

G = nx.Graph()
G.add_node("Mike")
G.add_nodes_from(["Annie", "Nick", "John"])
G.add_edge("Mike", "Annie")

print(list(G.nodes))
print(list(G.edges))

