def convert_to_undirected(oriented_graph):
    undirected_graph = {}
    for vertex in oriented_graph.keys():
        undirected_graph[vertex] = set()

    for vertex, neighbors in oriented_graph.items():
        for neighbor in neighbors:
            undirected_graph[vertex].add(neighbor)
            undirected_graph[neighbor].add(vertex)

    result = {}
    for vertex, neighbors in undirected_graph.items():
        result[vertex] = sorted(list(neighbors))

    return result


def get_edge_bundles(graph):
    edge_bundles = {}
    for vertex, neighbors in graph.items():
        if neighbors:
            edge_bundles[vertex] = neighbors
    return edge_bundles


def get_unique_edges(graph):
    edges = set()
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            edge = tuple(sorted([vertex, neighbor]))
            edges.add(edge)
    return sorted(list(edges))


def analyze_undirected_graph(oriented_graph):
    print("Анализ неориентированного графа:")
    print("=" * 40)

    undirected_graph = convert_to_undirected(oriented_graph)

    print("Исходный ориентированный граф:")
    for vertex, neighbors in oriented_graph.items():
        print(f"Вершина {vertex}: {neighbors}")
    print()

    print("Преобразованный неориентированный граф:")
    for vertex, neighbors in undirected_graph.items():
        print(f"Вершина {vertex}: {neighbors}")
    print()

    edge_bundles = get_edge_bundles(undirected_graph)

    print("Пучки рёбер для каждой вершины:")
    for vertex, neighbors in edge_bundles.items():
        print(f"Вершина {vertex} соединена с: {neighbors}")
    print()

    unique_edges = get_unique_edges(undirected_graph)

    print("Список всех рёбер (неориентированных):")
    for i, edge in enumerate(unique_edges, 1):
        print(f"{i}. {edge[0]} — {edge[1]}")

    print(f"\nВсего рёбер: {len(unique_edges)}")

    print("\nДетальные пучки рёбер по вершинам:")
    for vertex, neighbors in edge_bundles.items():
        print(f"Из вершины {vertex}:")
        for neighbor in neighbors:
            print(f"  {vertex} — {neighbor}")

    return undirected_graph, edge_bundles, unique_edges


oriented_graph = {
    0: [1, 2, 4],
    1: [3],
    2: [1, 4],
    3: [2, 4, 5, 6],
    4: [],
    5: [6],
    6: [],
}

print("Программа для анализа пучков рёбер неориентированного графа")
print("=" * 65)

undirected, bundles, edges = analyze_undirected_graph(oriented_graph)

print("\n" + "=" * 65)
print("Тест с другим графом:")

test_graph = {0: [1, 2], 1: [2], 2: [], 3: [1]}

analyze_undirected_graph(test_graph)
