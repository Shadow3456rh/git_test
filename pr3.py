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
def ucs(start,goal,graph):
    PQ=[(0,start,[start])]
    visited={}
    while PQ:
        cost,node,path=heapq.heappop(PQ)
        if(node==goal):
            return cost,path
        
        if node in visited and visited[node]<=cost:
            continue
        visited[node]=cost

        for neighbors,cumcost in graph.get(node,[]):
            new_cost=cost+cumcost
            if neighbors not in visited or new_cost<=visited[neighbors]:
                heapq.heappush(PQ,(new_cost,neighbors,path+[neighbors]))
cost,path = ucs('A','M',graph)
print("Cost is: ",cost)
print("Path is: ",path)
