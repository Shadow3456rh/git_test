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

def UCS(start, goal, graph):
    # Initialize Priority Queue
    PQ = [(0, start, [start])]
    visited = {}

    while PQ:
        cost, node, path = heapq.heappop(PQ)

        if node == goal:
            return cost, path

        # Check if node was visited with lower cost
        if node in visited and visited[node] <= cost:
            continue

        # Update visited with current cost
        visited[node] = cost

        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            heapq.heappush(PQ, (new_cost, neighbor, path + [neighbor]))

    return None


cost, path = UCS('A', 'M', graph)

print("Cost:", cost)
print("Path:", path)