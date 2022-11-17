from lab_yunin.my_disjoint_set import DisjointSetArray
from lab_yunin.my_binary_heap import BinaryHeap


def kruskal_algorithm(graph, vertexes):
    current_number_edge, number_edges_graph = 0, 0
    my_set = DisjointSetArray(vertexes)
    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    min_link_tree = []
    while number_edges_graph < vertexes - 1:
        first_vertex, second_vertex, weight = graph.graph[current_number_edge]
        current_number_edge += 1
        value_set_first_vertex = my_set.find(first_vertex)
        value_set_second_vertex = my_set.find(second_vertex)
        if value_set_first_vertex != value_set_second_vertex:
            number_edges_graph += 1
            min_link_tree.append([first_vertex,second_vertex,weight])
            my_set.union(value_set_first_vertex,value_set_second_vertex)
    # print('\n\tInforamtion about MST\n')
    # print('Struct of subgraph:\n')
    # weight_subgraph = 0
    # for edge in min_link_tree:
    #     print('Edge: ({0},{1}) , Weight: {2}'.format(edge[0], edge[1], edge[2]))
    #     weight_subgraph += edge[2]
    # print('\nShort information:\n')
    # print('Number edges: {0}\nWeight: {1}'.format(len(min_link_tree), weight_subgraph))
    # print('\n\tInforamtion about MST\n')

# TODO Мне кажется, что что-то тут не так
def prime_algorithm(graph, vertexes):
    # Суть алгоритма в том, чтобы на каждом шаге искать ребро с минимальным весом и присоединять его к дереву
    # Причём поиск этого минимального ребра должен быть на двоичной куче
    min_link_tree = {} # mst
    key = []
    min_heap = BinaryHeap()
    # ЗАПОЛНЕНИЕ КУЧИ
    for vertex in range(vertexes):
        min_link_tree.setdefault(vertex, [])
        key.append(float('inf'))
        min_heap.heap_list.append([vertex, key[vertex]])
        min_heap.position.append(vertex)
    min_heap.position[0] = 0
    key[0] = 0
    min_heap.decrease_key(0, key[0])
    min_heap.heap_size = vertexes
    while min_heap.heap_size != 0:
        node = min_heap.get_min_node()
        current_vertex = node[0]
        for current_edge in graph.graph[current_vertex]:
            second_vertex = current_edge[0]
            if min_heap.is_in_min_heap(second_vertex) and current_edge[1] < key[second_vertex]:
                key[second_vertex] = current_edge[1]
                min_link_tree[second_vertex] = [current_vertex, current_edge[1]]
                min_heap.decrease_key(second_vertex, key[second_vertex])
    # print('\n\tInforamtion about MST\n')
    # print('Struct of subgraph:\n')
    # weight_subgraph = 0
    # for vertex in range(vertexes):
    #     if not min_link_tree[vertex]:
    #         print('пропускаю')
    #         continue
    #     print('Edge: ({0},{1}) , Weight: {2}'.format(vertex, min_link_tree[vertex][0], min_link_tree[vertex][1]))
    #     weight_subgraph += min_link_tree[vertex][1]
    # print('\nShort information:\n')
    # print('Number edges: {0}\nWeight: {1}'.format(len(min_link_tree) - 1, weight_subgraph))
    # print('\n\tInforamtion about MST\n')
