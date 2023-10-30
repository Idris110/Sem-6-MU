from queue import PriorityQueue

# Define the graph as a dictionary of vertices and their neighbors
graph = {
    'S': {'A': 1, 'G': 10},
    'A': {'S': 1, 'C': 1, 'B': 2},
    'B': {'A': 2, 'D': 5},
    'C': {'A': 1, 'D': 3, 'G': 4},
    'D': {'B': 5, 'C': 3, 'G': 2},
    'G': {'D': 2, 'C': 4},
    'F': {}
}

# Define the heuristic values for each vertex
h = {
    'S': 5, 'A': 3, 'B': 4, 'C': 2, 'D': 6, 'G': 0
}

# Take input for the graph
# graph = {}
# num_edges = int(input("Enter the number of edges: "))
# for i in range(num_edges):
#     start, end, weight = input(
#         "Enter edge and its weight separated by space: ").split()
#     if start not in graph:
#         graph[start] = {}
#     if end not in graph:
#         graph[end] = {}
#     graph[start][end] = int(weight)
#     graph[end][start] = int(weight)

print(graph)
# Take input for the heuristic values
# h = {}
# for vertex in graph:
#     h[vertex] = int(input(f"Enter heuristic value for {vertex}: "))

# Define the function for UCS algorithm


def ucs(start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    closed_list = []
    dist = {}
    dist[start] = 0
    while not open_list.empty():
        print("Open List: ", list(open_list.queue))
        print("Closed List: ", closed_list)
        curr = open_list.get()[1]
        if curr == goal:
            print("Shortest path found!")
            path = [curr]
            while curr != start:
                for prev in graph:
                    if curr in graph[prev]:
                        if dist[curr] == graph[prev][curr] + dist[prev]:
                            path.append(prev)
                            curr = prev
                            break
            path.reverse()
            print("Shortest Path: ", path)
            return dist[goal]
        closed_list.append(curr)
        for neighbor in graph[curr]:
            if neighbor not in closed_list:
                new_cost = dist[curr] + graph[curr][neighbor]
                if neighbor not in dist or new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    priority = new_cost
                    open_list.put((priority, neighbor))
    print("No path found!")
    return None


# Test the function with the graph and heuristic defined above
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
print("Shortest distance from", start, "to", goal, "is", ucs(start, goal))