oriented_graph = {
    0: [1, 2, 4],
    1: [3],
    2: [1, 4],
    3: [2, 4, 5, 6],
    4: [],
    5: [6],
    6: [],
}


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

    incoming_bundles = {
        v: sources for v, sources in incoming_bundles.items() if sources
    }
    return incoming_bundles


print("Ориентированный граф:")
for vertex, neighbors in oriented_graph.items():
    print(f"Вершина {vertex}: {neighbors}")
print()

outgoing = get_outgoing_bundles(oriented_graph)
incoming = get_incoming_bundles(oriented_graph)

print("Пучки исходящих дуг:")
for vertex, targets in outgoing.items():
    print(f"Из вершины {vertex}: {targets}")
print()

print("Пучки входящих дуг:")
for vertex, sources in incoming.items():
    print(f"В вершину {vertex}: {sources}")
print()

print("Полный список пучков дуг:")
print("Исходящие пучки:")
for vertex, targets in outgoing.items():
    for target in targets:
        print(f"  {vertex} → {target}")

print("Входящие пучки:")
for vertex, sources in incoming.items():
    for source in sources:
        print(f"  {source} → {vertex}")
