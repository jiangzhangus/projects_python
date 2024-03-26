#breadth_first_search
from collections import deque
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()
# queue = []
queue = deque()

def bfs(visited, graph, node):
    visited.add(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end = " ")
        for next in graph[vertex]:
            if next not in visited:
                visited.add(next)
                queue.append(next)

print("Following is the Breadth-First Search")
bfs(visited, graph, '5')

# Output: 5 3 7 2 4 8