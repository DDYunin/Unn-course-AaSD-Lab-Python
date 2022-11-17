# Класс, который формирует граф, на экземпляре которого будут тестироваться алгоритмы
import random
from collections import defaultdict

class GraphLists:
    # граф представлен будет списками смежности
    # Инициализация полей графа
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.graph = defaultdict(list)
        self.edges = 0
        # print('Максимальное число ребёр в графе = {0}'.format(int(self.vertexes * (self.vertexes - 1) / 2)))
        # print('Минимальное число ребёр в графе = {0}'.format(self.vertexes - 1))

    # Метод добавляет ребро в граф
    def add_edge(self, first_vertex, second_vertex, weight):
        self.graph[first_vertex].append((second_vertex, weight))
        self.graph[second_vertex].append((first_vertex, weight))
        self.edges += 1

    def create_edges_naive(self, number_edges):
        self.edges = number_edges
        num_edges = 0
        edge_weight = 0
        for current_number in range(self.vertexes - 1):
            edge_weight = random.randint(1, 50)
            self.graph[current_number].append((current_number + 1, edge_weight))
            self.graph[current_number + 1].append((current_number, edge_weight))
            num_edges += 1
        for first_vertex in range(self.vertexes):
            for second_vertex in range(first_vertex+2, self.vertexes):
                num_edges += 1
                edge_weight = random.randint(1, 50)
                self.graph[first_vertex].append((second_vertex, edge_weight))
                self.graph[second_vertex].append((first_vertex, edge_weight))
                if (number_edges == num_edges):
                    break
            if (number_edges == num_edges):
                break

    # Метод печатает информацию о графе
    def print_graph(self):
        print('\n\tInformation about graph\n')
        print('Vertexes: {0}\n'.format(self.vertexes))
        print('Edges: {0}\n'.format(self.edges))
        for current_vertex in range(self.vertexes):
            print('\nVertex - ({0})\n'.format(current_vertex))
            print('\tEdges: {0}\n'.format(len(self.graph[current_vertex])))
            for current_edge in self.graph[current_vertex]:
                print('Edge: ({0},{1}) - Weight: {2}'.format(current_vertex, current_edge[0], current_edge[1]))            
        print('\n\tInformation about graph\n')

class GraphListEdges:

    # Инициализация полей графа
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.graph = []
        # print('Максимальное число ребёр в графе = {0}'.format(int(self.vertexes * (self.vertexes - 1) / 2)))
        # print('Минимальное число ребёр в графе = {0}'.format(self.vertexes - 1))

    # Метод добавляет ребро в граф
    def add_edge(self, first_vertex, second_vertex, weight):
        if(not self.edge_is((first_vertex, second_vertex, weight))):
            self.graph.append((first_vertex, second_vertex, weight))

    # Метод добавляет несколько ребёр в граф
    def add_edges(self, edges):
        for edge in edges:
            if(not self.edge_is(edge)):
                self.graph.append(edge)

    # TODO Доработать этот метод (Усовершенствовать)
    # Метод проверяет, существует ли такое ребро в графе и возвращает булево значение
    def edge_is(self, edge):
        for current_edge in self.graph:
            if ((current_edge[0], current_edge[1]) == (edge[0], edge[1]) or (current_edge[0], current_edge[1]) == (edge[1], edge[0])):
                return True
        return False

    def create_edges_naive(self, number_edges):
        # Проверим на количество ребёр - min и max числа, их мы узнаем при строительстве графа,
        # Так как мы работаем только с графами с компонентами связности - 1, поэтому нам нужно построить
        # Именно такой граф.
        # Сделаем минимальный граф, в нём будет n-1 ребро
        edges = 0
        for current_number in range(self.vertexes - 1):
            self.graph.append((current_number, current_number + 1, random.randint(1, 50)))
            edges += 1
        # Дополним граф до нужного числа ребёр
        for first_vertex in range(self.vertexes):
            for second_vertex in range(first_vertex + 2, self.vertexes):
                self.graph.append((first_vertex, second_vertex, random.randint(1, 50)))
                edges += 1
                if (edges == number_edges):
                    break
            if (edges == number_edges):
                    break

    # Метод печатает информацию о графе
    def print_graph(self):
        print('\n\tInformation about graph\n')
        print('Vertexes: {}\n'.format(self.vertexes))
        for current_vertex in range(self.vertexes):
            print('Vertex - ({0})'.format(current_vertex))
        print('\nEdges: {0}\n'.format(len(self.graph)))
        for current_edge in self.graph:
            print('Edge: ({0},{1}) - Weight: {2}'.format(current_edge[0], current_edge[1], current_edge[2]))
        print('\n\tInformation about graph\n')