import heapq
graph = {
    'A': [('B', 2), ('C', 3), ('D', 4)],
    'B': [('E', 1), ('F', 3)],
    'C': [('G', 4)],
    'D': [('H', 2), ('I', 1)],
    'E': [('J', 8)],
    'F': [],
    'G': [('L', 5)],
    'H': [('M', 3)],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 6,
    'F': 7,
    'G': 3,
    'H': 2,
    'I': 4,
    'J': 8,
    'K': 9,
    'L': 2,
    'M': 0
}

def gbfs(start,goal,graph):
    PQ=[(heuristic[start],start,[start])]
    visited=set()
    while PQ:
        heuristics,node,path=heapq.heappop(PQ)
        if node==goal:
            return heuristics,path
        if node not in visited:
            visited.add(node)
        
        for neighbors,cost in graph[node]:
            if neighbors not in visited:
                heapq.heappush(PQ,(heuristic[neighbors], neighbors,path+[neighbors]))

heur,pat=gbfs('A','M',graph)
print(heur)
print(pat)

def astar(start,goal,graph):
    PQ=[(heuristic[start],0,start,[start])]
    visited={}
    while PQ:
        f,g,node,path=heapq.heappop(PQ)
        if node==goal:
            return f,path
        
        if node in visited and visited[node]<=g:
            continue
        
        visited[node]=g

        for neighbors,g_score in graph.get(node,[]):
            new_g=g+g_score
            new_f=new_g+heuristic[neighbors]
            if neighbors not in visited:
                heapq.heappush(PQ,(new_f,new_g,neighbors,path+[neighbors]))

f,path=astar('A','M',graph)
print(f)
print(path)

