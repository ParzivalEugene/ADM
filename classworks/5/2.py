oriented_graph = {
    0: [1, 2, 4],
    1: [3],
    2: [1, 4],
    3: [2, 4, 5, 6],
    4: [],
    5: [6],
    6: [],
}


def convert_to_undirected(oriented_graph):
    undirected_graph = {vertex: set() for vertex in oriented_graph.keys()}

    for vertex, neighbors in oriented_graph.items():
        for neighbor in neighbors:
            undirected_graph[vertex].add(neighbor)
            undirected_graph[neighbor].add(vertex)

    result = {}
    for vertex in undirected_graph:
        result[vertex] = sorted(list(undirected_graph[vertex]))

    return result


def get_edge_bundles(graph):
    edge_bundles = {}
    for vertex, neighbors in graph.items():
        if neighbors:
            edge_bundles[vertex] = neighbors
    return edge_bundles


undirected_graph = convert_to_undirected(oriented_graph)

print("Неориентированный граф (преобразованный из ориентированного):")
for vertex, neighbors in undirected_graph.items():
    print(f"Вершина {vertex}: {neighbors}")
print()

edge_bundles = get_edge_bundles(undirected_graph)

print("Пучки рёбер для каждой вершины:")
for vertex, neighbors in edge_bundles.items():
    print(f"Вершина {vertex} соединена с: {neighbors}")
print()

print("Список всех рёбер (неориентированных):")
edges = set()
for vertex, neighbors in undirected_graph.items():
    for neighbor in neighbors:
        edge = tuple(sorted([vertex, neighbor]))
        edges.add(edge)

edges = sorted(list(edges))
for i, edge in enumerate(edges, 1):
    print(f"{i}. {edge[0]} — {edge[1]}")

print(f"\nВсего рёбер: {len(edges)}")

print("\nПучки рёбер по вершинам:")
for vertex, neighbors in edge_bundles.items():
    print(f"Из вершины {vertex}:")
    for neighbor in neighbors:
        print(f"  {vertex} — {neighbor}")
