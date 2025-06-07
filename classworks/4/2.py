edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 6),
    (3, 1),
    (4, 2),
    (4, 3),
    (4, 5),
    (5, 6),
    (6, 4),
]

print("Исходный список дуг:")
for i, edge in enumerate(edges):
    print(f"{i + 1}. {edge}")

print("\nЭтап 1: Сортировка по первой вершине")
edges_stage1 = sorted(edges, key=lambda x: x[0])
for i, edge in enumerate(edges_stage1):
    print(f"{i + 1}. {edge}")

print("\nЭтап 2: Сортировка по второй вершине (при равенстве первой)")
edges_stage2 = sorted(edges, key=lambda x: (x[0], x[1]))
for i, edge in enumerate(edges_stage2):
    print(f"{i + 1}. {edge}")

print("\nЭтап 3: Лексикографическая сортировка")
edges_stage3 = sorted(edges)
for i, edge in enumerate(edges_stage3):
    print(f"{i + 1}. {edge}")

print("\nФинальный упорядоченный список:")
for i, edge in enumerate(edges_stage3):
    print(f"{i + 1}. ({edge[0]}, {edge[1]})")
