from heapq import heappop, heappush

def minimumFuel(N, Roads, K):
    graph = [[] for _ in range(N)]
    for road in Roads:
        cityA, cityB, weight = road
        graph[cityA].append((cityB, weight))

    distance = [float('inf')] * N
    distance[0] = 0

    fuel = [-1] * N
    fuel[0] = 0

    pq = [(0, 0)]  # (distance, city)
    while pq:
        dist, city = heappop(pq)

        if city == N - 1:
            return dist

        if fuel[city] < 0 or fuel[city] > K:
            continue

        for neighbor, road_length in graph[city]:
            remaining_fuel = fuel[city] - road_length
            if remaining_fuel < 0 or remaining_fuel > K:
                continue

            if remaining_fuel > fuel[neighbor]:
                fuel[neighbor] = remaining_fuel
                distance[neighbor] = dist + road_length
                heappush(pq, (distance[neighbor], neighbor))

    return -1 

# Example usage:
N = 3
Roads = [[0, 1, 10], [1, 2, 51], [2, 3, 5]]
K = 1
print(minimumFuel(N, Roads, K))
