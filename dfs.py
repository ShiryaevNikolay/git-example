key_visited = 'visited'
key_neighbors = 'neighbors'

# Создает список смежностей по парам вершин
def createGraph(edges):
    # Инициализирует вершину в списке смежностей
    def initVertexData():
        return {
            key_visited: False,
            key_neighbors: []
        }

    graph = {}
    for edge in edges:
        from_vertex = edge[0]
        to_vertex = edge[1]
        if from_vertex not in graph:
            graph[from_vertex] = initVertexData()
        if to_vertex not in graph:
            graph[to_vertex] = initVertexData()
        graph[from_vertex][key_neighbors].append(to_vertex)
    return graph

# Поиска в глубину
def dfs(vertex, depth = []):
    global graph, depths

    depth.append(vertex)

    graph[vertex][key_visited] = True
    for neighbor in graph[vertex][key_neighbors]:
        if not graph[neighbor][key_visited]:
            dfs(neighbor, depth)
            depths.append(depth.copy())
            graph[neighbor][key_visited] = False
            depth.remove(vertex)

# input = "4 2, 1 3, 2 4"

input_edges = input("Введите пары смежных вершин через ',': ")

edges = [edge.strip().split(' ') for edge in input_edges.split(',')]

graph = createGraph(edges)

depths = []

dfs('1')

print(f'Результат: {depths}')
