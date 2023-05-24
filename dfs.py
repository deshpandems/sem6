"""The depthfirstsearch function takes a graph object, a starting node, and an ending node as arguments, and returns a
list of nodes representing a path from the start node to the end node using depth-first search algorithm."""
def depthfirstsearch(graph, start_node, goal_node):
    visited = set()
    stack = [(start_node, [start_node])]

    while stack:
        (current_node, path) = stack.pop()
        if current_node == goal_node:
            return path
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None
#graph delcared in tuple
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}
#user input
start_node = input("enter the start node :")
goal_node = input("enter the goal node :")

path = depthfirstsearch(graph, start_node, goal_node)
if path is not None:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")