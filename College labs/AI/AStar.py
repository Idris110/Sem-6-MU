from queue import PriorityQueue

def astar(start, goal, graph, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    g_score = {start: 0}
    f_score = {start: heuristic[start]}
    while not frontier.empty():
        _, node = frontier.get()
        if node == goal:
            return g_score[node]
        if node not in explored:
            explored.add(node)
            for neighbor, weight in graph[node].items():
                tentative_g_score = g_score[node] + weight
                if neighbor in g_score and tentative_g_score >= g_score[neighbor]:
                    continue
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                frontier.put((f_score[neighbor], neighbor))
    return -1


graph = {}
num_vertices = int(input("Enter the number of vertices: "))
for i in range(num_vertices):
    # vertex = input(f"Enter vertex {i+1}: ")
    print(f"For vertex {i+1},")
    vertex = i+1
    num_neighbors = int(input("Enter the number of neighbors: "))
    neighbors = {}
    for j in range(num_neighbors):
        neighbor = input(f"Enter neighbor {j+1}: ")
        weight = int(input(f"Enter the weight of edge ({vertex}, {neighbor}): "))
        neighbors[neighbor] = weight
    graph[vertex] = neighbors

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

print(graph)

# prompt user to enter heuristic information
heuristic = {}
for vertex in graph:
    heuristic[vertex] = int(input(f"Enter the heuristic for {vertex}: "))

# perform A* search
cost = astar(start, goal, graph, heuristic)
if cost == -1:
    print("Path not found.")
else:
    print(f"The minimum cost from {start} to {goal} is {cost}.")

