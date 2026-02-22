import heapq
graph = {'A':[('B', 25),('C',65)], 'B':[('D',35),('E',45)],'C':[('F',23),('G',0)],'D':[],'E':[],'F':[],'G':[]}
import heapq

def greedy_best_first_search(graph, start, goal):
    visited = set()

    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    while priority_queue:
        heuristic, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, h_value in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (h_value, neighbor, path + [neighbor]))

    return None

result = greedy_best_first_search(graph, 'A', 'G')
print("Greedy Best First Search Path:", result)

############A*###############
def a_star_search(graph, start, goal):
    visited = set()
    priority_queue = []
    heapq.heappush(priority_queue, (0, 0, start, [start]))

    while priority_queue:
        f_cost, g_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node == goal:
            return path

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, cost in graph[current_node]:
                if neighbor not in visited:
                    new_g = g_cost + cost
                    new_f = new_g + cost
                    heapq.heappush(priority_queue, (new_f, new_g, neighbor, path + [neighbor]))

    return None

result = a_star_search(graph, 'A', 'G')
print("A* Search Path:", result)