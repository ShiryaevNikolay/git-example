from input import inputTargetVerteces

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

# Алгоритм поиск в глубину
def dfs(start_vertex, end_vertex, depth = []):
    global graph, depths

    depth.append(start_vertex)

    graph[start_vertex][key_visited] = True

    if start_vertex == end_vertex:
        return

    for neighbor in graph[start_vertex][key_neighbors]:
        if not graph[neighbor][key_visited]:
            dfs(neighbor, end_vertex, depth)
            depths.append(depth.copy())
            graph[neighbor][key_visited] = False
            depth.remove(start_vertex)

# input = "4 2, 1 3, 2 4"

# Пользовательский ввод
input_edges = input("Введите пары смежных вершин через ',': ")
start_vertex, end_vertex = inputTargetVerteces()

# Преобразовывает пользовательский ввод в массив смежных вершин
edges = [edge.strip().split(' ') for edge in input_edges.split(',')]

# Создается граф
graph = createGraph(edges)

# Содержит массивы, полученные при обходе в глубину
depths = []

# Поиск в глубину
dfs(start_vertex, end_vertex)

# Находит максимальную глубину
max_depth = []
for depth in depths:
    if len(depth) > len(max_depth):
        max_depth = depth

print(f'Результат: {len(max_depth) - 1}')
