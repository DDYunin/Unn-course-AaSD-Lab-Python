class DisjointSetArray():
    # массив содержит значение какому множеству принадлежит вершина
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.value_set = []
        for vertex in range(vertexes):
            self.value_set.append(vertex)

    def find(self, vertex):
        return self.value_set[vertex]

    def union(self, first_value_set, second_value_set):
        for current_vertex in range(self.vertexes):
            if self.value_set[current_vertex] == first_value_set:
                self.value_set[current_vertex] = second_value_set
