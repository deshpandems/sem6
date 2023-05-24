from collections import deque
import graphlib
def breadthfirstsearch(graph, start_node, goal_node):
    queue = deque([(start_node, [start_node])])

    while queue:
        current_node, path = queue.popleft()
        print(f"Exploring node {current_node}: Explored nodes so far: {path}")
        if current_node == goal_node:
            return path
        for neighbor in graph[current_node]:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
    return None
print(graphlib)
start_node = input("Enter Start Node: ")
goal_node = input("Enter Goal Node: ")

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}
path = breadthfirstsearch(graph, start_node, goal_node)
if path is not None:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")
