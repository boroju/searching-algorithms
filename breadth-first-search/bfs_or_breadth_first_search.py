from queue import Queue

if __name__ == '__main__':

    # BFS sample
    adj_list = {
        "A": ["B", "D"],
        "B": ["A", "C"],
        "C": ["B"],
        "D": ["A", "E", "F"],
        "E": ["D", "F", "G"],
        "F": ["D", "E", "H"],
        "G": ["E", "H"],
        "H": ["G", "F"]
    }

    # BFS init
    visited = {}
    level = {}  # distance dictionary
    parent = {}
    bfs_traversal_output = []
    queue = Queue()

    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1  # or infinite

    source_node = "A"
    visited[source_node] = True
    level[source_node] = 0
    queue.put(source_node)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)

    print('BFS Output:')
    print(bfs_traversal_output)
    print()
    # shortest distance of all nodes from source node
    print('Level:')
    print(level)
    print()
    # shortest distance of G node from source node
    print('Level G:')
    print(level["G"])
    print()
    # shortest path of any node from source code
    v = "G"
    path = []
    while v is not None:
        path.append(v)
        v = parent[v]
    path.reverse()
    print('Path:')
    print(path)

