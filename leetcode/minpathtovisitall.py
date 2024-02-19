from collections import deque

def shortest_path_length(graph):
    n = len(graph)
    target_mask = (1 << n) - 1
    min_distance = float('inf')

    def dfs(node, visited_mask, steps, memo):
        nonlocal min_distance

        if visited_mask == target_mask:
            min_distance = min(min_distance, steps)
            return

        if (node, visited_mask) in memo:
            return

        for neighbor in graph[node]:
            new_mask = visited_mask | (1 << neighbor)
            dfs(neighbor, new_mask, steps + 1, memo)

        memo.add((node, visited_mask))

    for start_node in range(n):
        dfs(start_node, 1 << start_node, 0, set())

    return min_distance

# Test example
graph = [[1, 2, 3], [0], [0], [0]]
print(shortest_path_length(graph))  # Output: 4

