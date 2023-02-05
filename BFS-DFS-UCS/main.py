# BFS
graph = {
    'START': ['d', 'e', 'p'],
    'd': ['b', 'c', 'e'],
    'b': ['a'],
    'c': ['a'],
    'a': [],
    'e': ['r', 'h'],
    'h': ['p', 'q'],
    'p': ['q'],
    'q': [],
    'r': ['f'],
    'f': ['c', 'GOAL'],
    'GOAL': []

}

visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


print("BFS")
bfs(visited, graph, 'START')

print("\n")

# DFS

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("DFS")
dfs(visited, graph, 'START')

print("\n")


# UCS

def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost


def ucs(visited, graph, node):
    Visited = []
    queue = [[(node, 0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop
        x = path[-1][0]
        if node in Visited:
            continue
        Visited.append(x)
        if x == visited:
            return path
        else:
            adj_nodes = graph.get(node, [])
            for (node2, cost) in adj_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


print("UCS")
solution = ucs(visited, graph, 'START')
print(solution)
print('path_cost:', path_cost(solution)[0])
