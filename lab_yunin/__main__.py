# У нас имеется граф, тоесть нужно создать граф
# Как его хранить? (Как он должен быть устроен?) - массив пар вершин графа + вес этого ребра (1,2,50) -
# - (первая вершина, вторая вершина, вес ребра), причём первая вершина будет меньше второй для конкретики.

from lab_yunin.my_graph import Graph
from lab_yunin.my_disjoint_set import DisjointSet
from lab_yunin.my_algorithms import kruskal_algorithm

def main():
    test_graph = Graph(5)
    test_graph.add_edge(0, 1, 5)
    test_graph.add_edge(0, 2, 13)
    test_graph.add_edge(0, 4, 15)
    test_graph.add_edge(1, 3, 8)
    test_graph.add_edge(1, 2, 10)
    test_graph.add_edge(2, 3, 6)
    test_graph.add_edge(2, 4, 20)
    
    # test_graph.create_edges_random(11)
    test_graph.print_graph()
    kruskal_algorithm(test_graph, test_graph.vertexes)
    # print(test_graph.graph)
    # test_set = DisjointSet(6)
    # test_set.union(1,3)
    # print(test_set.find(1), test_set.find(3))
    # print(test_set.value_set)

if __name__ == '__main__':
    main()
