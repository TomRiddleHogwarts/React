import sys
import matplotlib.pyplot as plt
import networkx as nx

def dijkstra(graph, start, destination):
    V = len(graph)
    
    # Initialize distance, visited, and predecessor lists
    distance = [sys.maxsize] * V
    visited = [False] * V
    predecessor = [-1] * V
    
    # Distance from the start node to itself is 0
    distance[start] = 0
    
    for _ in range(V):
        # Find the vertex with the minimum distance that has not been visited
        min_distance = sys.maxsize
        for v in range(V):
            if distance[v] < min_distance and not visited[v]:
                min_distance = distance[v]
                min_vertex = v
        
        # Mark the selected vertex as visited
        visited[min_vertex] = True
        
        # Update the distance and predecessor of adjacent vertices
        for v in range(V):
            if not visited[v] and graph[min_vertex][v] > 0:
                if distance[min_vertex] + graph[min_vertex][v] < distance[v]:
                    distance[v] = distance[min_vertex] + graph[min_vertex][v]
                    predecessor[v] = min_vertex
    
    # Construct the path from start to destination
    path = []
    current_node = destination
    while current_node != -1:
        path.insert(0, current_node)
        current_node = predecessor[current_node]
    
    return distance[destination], path


# Example usage
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]

start_node = 1
destination_node = 6

shortest_distance, path = dijkstra(graph, start_node, destination_node)

if shortest_distance < sys.maxsize:
    print(f"Shortest distance from node {start_node} to node {destination_node} is {shortest_distance}")
    print("Shortest path:", " -> ".join(map(str, path)))
else:
    print(f"No path found from node {start_node} to node {destination_node}")
    
# Create a graph for visualization
G = nx.Graph()
for i in range(len(graph)):
    for j in range(i + 1, len(graph)):
        if graph[i][j] > 0:
            G.add_edge(i, j, weight=graph[i][j])

# Create positions for the nodes with a specified random_state
pos = nx.spring_layout(G, seed=42)  # Specify a valid seed value

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue")
edge_labels = {(i, j): graph[i][j] for i, j in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="red")

# Highlight the shortest path
shortest_path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color="green", width=3)

plt.show()





