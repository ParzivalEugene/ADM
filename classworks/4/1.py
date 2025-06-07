graph = {0: [1, 2, 3, 4], 1: [6], 2: [], 3: [1], 4: [2, 3, 5], 5: [6], 6: [4]}

edges = []
for vertex in graph:
    for neighbor in graph[vertex]:
        edges.append((vertex, neighbor))

print("Список дуг (неупорядоченный):")
for i, edge in enumerate(edges):
    print(f"{i + 1}. ({edge[0]}, {edge[1]})")

print(f"\nВсего дуг: {len(edges)}")

