def get_outgoing_bundles(graph):
    outgoing_bundles = {}
    for vertex, neighbors in graph.items():
        if neighbors:
            outgoing_bundles[vertex] = neighbors
    return outgoing_bundles


def get_incoming_bundles(graph):
    incoming_bundles = {vertex: [] for vertex in graph.keys()}
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            incoming_bundles[neighbor].append(vertex)

    result = {}
    for vertex, sources in incoming_bundles.items():
        if sources:
            result[vertex] = sources
    return result


def analyze_oriented_graph(graph):
    print("Анализ ориентированного графа:")
    print("=" * 40)

    print("Структура графа:")
    for vertex, neighbors in graph.items():
        print(f"Вершина {vertex}: {neighbors}")
    print()

    outgoing = get_outgoing_bundles(graph)
    incoming = get_incoming_bundles(graph)

    print("Пучки исходящих дуг:")
    for vertex, targets in outgoing.items():
        print(f"Из вершины {vertex}: {targets}")
    print()

    print("Пучки входящих дуг:")
    for vertex, sources in incoming.items():
        print(f"В вершину {vertex}: {sources}")
    print()

    print("Детальный список дуг:")
    print("Исходящие дуги:")
    for vertex, targets in outgoing.items():
        for target in targets:
            print(f"  {vertex} → {target}")

    print("Входящие дуги:")
    for vertex, sources in incoming.items():
        for source in sources:
            print(f"  {source} → {vertex}")

    return outgoing, incoming


oriented_graph = {
    0: [1, 2, 4],
    1: [3],
    2: [1, 4],
    3: [2, 4, 5, 6],
    4: [],
    5: [6],
    6: [],
}

print("Программа для анализа пучков дуг ориентированного графа")
print("=" * 60)

outgoing_bundles, incoming_bundles = analyze_oriented_graph(oriented_graph)

print("\n" + "=" * 60)
print("Тест с другим графом:")

test_graph = {0: [1, 2], 1: [2, 3], 2: [3], 3: []}

analyze_oriented_graph(test_graph)
