import heapq

def dijkstra(graph, start, end):
    # Create a priority queue to keep track of nodes and their tentative distances
    priority_queue = [(0, start)]  # (distance, node)
    print(priority_queue)
    visited = set()
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    print(distances)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)


        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Return the minimum cost to reach the 'end' node
    print(priority_queue)
    return distances[end]

# Example usage:
graph = {
    'A': [('U', 1.45)],
    'U': [('J', 1.10), ('A', 1.45)],
    'J': [('U', 1.10),('G',0.70)],
    'G': [('J', 0.70)],
}
#priority_queue = [(0, 'A')]
#visited = set()


start_node = 'J'
end_node = 'G'

min_cost = dijkstra(graph, start_node, end_node)
if min_cost != float('inf'):
    print(f"The minimum cost to move from {start_node} to {end_node} is {min_cost}")
else:
    print(f"There is no path from {start_node} to {end_node}")

#create a priority queue to keep track of nodes and their tentative distances


def dijkstra(graph,start,end):

    qu