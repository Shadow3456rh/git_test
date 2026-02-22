def dfs(graph, node, visited=None):
    if(visited is None):
        visited=set()
    visited.add(node)
    print(node, end=" ")
    
    for v in graph[node]:
        if v not in visited:
            dfs(graph,v,visited)



# Graph definition
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal:")
dfs(graph, 'A')