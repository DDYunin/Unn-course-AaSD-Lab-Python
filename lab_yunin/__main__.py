# У нас имеется граф, тоесть нужно создать граф
# Как его хранить? (Как он должен быть устроен?) - массив пар вершин графа + вес этого ребра (1,2,50) -
# - (первая вершина, вторая вершина, вес ребра), причём первая вершина будет меньше второй для конкретики.

from lab_yunin.my_graph import Graph

def main():
    test_graph = Graph(6)
    test_graph.create_edges_random(11)
    test_graph.print_graph()
    print(test_graph.graph)

if __name__ == '__main__':
    main()
