import networkx as nx

vertices = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]
G = nx.Graph()
G.add_nodes_from(vertices)
G.add_edges_from(edges)
nx.draw(G, with_labels=True, node_color='y', node_size=800)

degree_centrality = nx.degree_centrality(G)
print("degree_centrality", degree_centrality)

betweenness_centrality = nx.betweenness_centrality(G)
print("betweenness_centrality", betweenness_centrality)

closeness_centrality = nx.closeness_centrality(G)
print("closeness_centrality", closeness_centrality)

centrality = nx.eigenvector_centrality(G)
result = sorted((v, '{:0.2f}'.format(c)) for v, c in centrality.items())

print("result", result)
