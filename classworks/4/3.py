def sort_edges_by_stages(edges):
    print("Исходный список дуг:")
    for i, edge in enumerate(edges):
        print(f"{i + 1}. {edge}")

    print("\nЭтап 1: Сортировка по первой вершине")
    stage1 = sorted(edges, key=lambda x: x[0])
    for i, edge in enumerate(stage1):
        print(f"{i + 1}. {edge}")

    print("\nЭтап 2: Сортировка по первой, затем по второй вершине")
    stage2 = sorted(edges, key=lambda x: (x[0], x[1]))
    for i, edge in enumerate(stage2):
        print(f"{i + 1}. {edge}")

    print("\nЭтап 3: Полная лексикографическая сортировка")
    stage3 = sorted(edges)
    for i, edge in enumerate(stage3):
        print(f"{i + 1}. {edge}")

    return stage3


def create_edge_list_from_graph(graph):
    edges = []
    for vertex in graph:
        for neighbor in graph[vertex]:
            edges.append((vertex, neighbor))
    return edges


graph_example = {0: [1, 2], 1: [6], 2: [3, 4], 3: [4], 4: [5, 6], 5: [6], 6: []}

print("Пример работы программы:")
print("=" * 50)

edges = create_edge_list_from_graph(graph_example)
sorted_edges = sort_edges_by_stages(edges)

print("\n" + "=" * 50)
print("Программа для любого списка дуг:")


def sort_any_edges(edge_list):
    return sort_edges_by_stages(edge_list)


test_edges = [(3, 1), (1, 2), (2, 3), (1, 3), (0, 1)]
print(f"\nТест с произвольным списком: {test_edges}")
sort_any_edges(test_edges)
