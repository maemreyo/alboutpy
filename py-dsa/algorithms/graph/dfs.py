def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)

    for _next in graph[start] - visited:
        dfs(graph, _next, visited)
    return visited
