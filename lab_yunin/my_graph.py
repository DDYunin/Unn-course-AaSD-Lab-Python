# Класс, который формирует граф, на экземпляре которого будут тестироваться алгоритмы
import random

class Graph:

    # Инициализация полей графа
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.graph = []
        print('Максимальное число ребёр в графе = {0}'.format(int(self.vertexes * (self.vertexes - 1) / 2)))
        print('Минимальное число ребёр в графе = {0}'.format(self.vertexes - 1))

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

    # TODO Доработать этот метод (Усовершенствовать)
    # Метод создаёт рёбра в графе случайно
    def create_edges_random(self, number_edges):
        # Проверим на количество ребёр - min и max числа, их мы узнаем при строительстве графа,
        # Так как мы работаем только с графами с компонентами связности - 1, поэтому нам нужно построить
        # Именно такой граф.
        # Сделаем минимальный граф, в нём будет n-1 ребро
        for current_number in range(self.vertexes - 1):
            self.graph.append((current_number, current_number + 1, random.randint(1, 50)))
        # Дополним граф до нужного числа ребёр
        for current_number_edge in range(number_edges - self.vertexes + 1):
            while True:
                current_edge = []
                first_edge = random.randint(0, self.vertexes-1)
                second_edge = random.randint(0, self.vertexes-1)
                if first_edge < second_edge:
                    current_edge.append(first_edge)
                    current_edge.append(second_edge)
                else:
                    continue
                if(not self.edge_is(current_edge)):
                    current_edge.append(random.randint(1, 50))
                    self.graph.append(tuple(current_edge))
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
