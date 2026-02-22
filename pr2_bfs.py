
graph = {
'A': ('B', 'C'),
'B': ('D', 'E'),
'C': ('F'),
'D': (),
'E': ('F'),
'F': ()
}



from collections import deque

def BFS(graph, start):
    queue=deque()
    visited=set()

    visited.add(start)
    queue.append(start)
    while queue:
        node =queue.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

BFS(graph, 'A')