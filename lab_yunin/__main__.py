from lab_yunin.my_graph import GraphLists, GraphListEdges
from lab_yunin.my_disjoint_set import DisjointSetArray
from lab_yunin.my_algorithms import kruskal_algorithm, prime_algorithm, prime_algorithm_2
from lab_yunin.my_binary_heap import BinaryHeap

# DEBUG
# from my_graph import GraphLists, GraphListEdges
# from my_disjoint_set import DisjointSetArray
# from my_algorithms import kruskal_algorithm, prime_algorithm, prime_algorithm_2
# from my_binary_heap import BinaryHeap
# DEBUG

from loguru import logger
import time

def kruskal_work_small_graph_1():
    graph = GraphLists(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    kruskal_algorithm(graph, graph.vertexes)

def kruskal_work_small_graph_2():
    graph = GraphLists(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 8)
    graph.add_edge(1, 2, 11)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 6)
    graph.add_edge(2, 4, 9)
    graph.add_edge(3, 4, 11)
    graph.add_edge(3, 5, 9)
    graph.add_edge(4, 5, 10)
    kruskal_algorithm(graph, graph.vertexes)



def prime_work_small_graph_1():
    graph = GraphLists(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    prime_algorithm(graph, graph.vertexes)

def prime_work_small_graph_1_2():
    graph = GraphListEdges(9)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    prime_algorithm_2(graph, graph.vertexes)

def prime_work_small_graph_2():
    graph = GraphLists(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 8)
    graph.add_edge(1, 2, 11)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 6)
    graph.add_edge(2, 4, 9)
    graph.add_edge(3, 4, 11)
    graph.add_edge(3, 5, 9)
    graph.add_edge(4, 5, 10)
    prime_algorithm(graph, graph.vertexes)

def prime_work_small_graph_2_2():
    graph = GraphListEdges(6)
    graph.add_edge(0, 1, 7)
    graph.add_edge(0, 2, 8)
    graph.add_edge(1, 2, 11)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 6)
    graph.add_edge(2, 4, 9)
    graph.add_edge(3, 4, 11)
    graph.add_edge(3, 5, 9)
    graph.add_edge(4, 5, 10)
    prime_algorithm_2(graph, graph.vertexes)

def prime_work_large_graph():
    test_graph = GraphLists(10000)
    start_time = time.monotonic()
    test_graph.create_edges_naive(5000*500)
    print('The creating edges lasted {0} seconds'.format(time.monotonic() - start_time))
    start_time = time.monotonic()
    prime_algorithm(test_graph, test_graph.vertexes)
    print('The prime algorithm edges lasted {0} seconds'.format(time.monotonic() - start_time))

def kruskal_work_large_graph():
    test_graph = GraphLists(1000)
    start_time = time.monotonic()
    test_graph.create_edges_naive(500*500)
    print('The creating edges lasted {0} seconds'.format(time.monotonic() - start_time))
    start_time = time.monotonic()
    kruskal_algorithm(test_graph, test_graph.vertexes)
    print('The kruskal algorithm edges lasted {0} seconds'.format(time.monotonic() - start_time))

# EXPERIMENTS
# n = 10000, m = 5000*9999
# n = 10000, m = 5000*5
# n = 10000, m = 5000*500

# n = 1000, m = 500*999
# n = 1000, m = 500*5
# n = 1000, m = 500*500

# n = 100, m = 50*99
# n = 100, m = 50*5
# n = 100, m = 50*50


if __name__ == '__main__':
    kruskal_work_small_graph_1()
    prime_work_small_graph_1()
    prime_work_small_graph_1_2()
    # kruskal_work_small_graph_2()
    # prime_work_small_graph_2()
    # kruskal_work_large_graph()
    # prime_work_large_graph()