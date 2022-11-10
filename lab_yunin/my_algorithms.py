from lab_yunin.my_disjoint_set import DisjointSet

def kruskal_algorithm(graph, vertexes):
    current_number_edge, number_edges_graph = 0, 0
    my_set = DisjointSet(vertexes)
    graph.graph = sorted(graph.graph, key=lambda item: item[2])
    graph.print_graph()
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
    print('\n\tInforamtion about MST\n')
    print('Struct of subgraph:\n')
    weight_subgraph = 0
    for edge in min_link_tree:
        print('Edge: ({0},{1}) , Weight: {2}'.format(edge[0], edge[1], edge[2]))
        weight_subgraph += edge[2]
    print('\nShort information:\n')
    print('Number edges: {0}\nWeight: {1}'.format(len(min_link_tree), weight_subgraph))
    print('\n\tInforamtion about MST\n')