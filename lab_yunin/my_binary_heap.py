# Двоичная куча - двоичное дерево со свойством кучеобразности (приоритет узла, не меньше (не больше) приоритета его потомков)
class BinaryHeap():

    def __init__(self):
        self.heap_list = []
        self.heap_size = 0
        self.position = []
    
    def get_min_node(self):
        result = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.heap_size - 1]
        self.position[self.heap_list[self.heap_size - 1][0]] = 0
        self.position[result[0]] = self.heap_size - 1
        self.heap_size -= 1
        self.heapify(0)
        return result
    
    def is_in_min_heap(self, vertex):
        if self.position[vertex] < self.heap_size:
            return True
        return False
    
    def decrease_key(self, vertex, weight):
        index = self.position[vertex] # получаем позицию вершины в куче
        self.heap_list[index][1] = weight # обновляем расстояние до строящего оставного дерева
        while index > 0 and self.heap_list[index][1] < self.heap_list[(index - 1) // 2][1]:
            self.position[self.heap_list[index][0]] = (index - 1) // 2 # мы меняем местами позиции текущего элемента и его родителя
            self.position[self.heap_list[(index - 1) // 2][0]] = index
            self.heap_list[(index - 1) // 2], self.heap_list[index] = self.heap_list[index], self.heap_list[(index - 1) // 2] # поменяли
            # местами элементы в куче
            index = (index - 1) // 2
        
    
    def add_node(self, node):
        self.heap_list.append(node)
        index = self.heap_size - 1
        parent_index = (index - 1) // 2
        while index > 0 and self.heap_list[parent_index] > self.heap_list[index]:
            self.heap_list[parent_index], self.heap_list[index] = self.heap_list[index], self.heap_list[parent_index]
            index = parent_index
            parent_index = (index - 1) // 2
    
    def heapify(self, index):
        while(True):
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            current_min_index = index
            if (left_child_index < self.heap_size and self.heap_list[left_child_index][1] < self.heap_list[current_min_index][1]):
                current_min_index = left_child_index
            if (right_child_index < self.heap_size and self.heap_list[right_child_index][1] < self.heap_list[current_min_index][1]):
                current_min_index = right_child_index
            if current_min_index == index:
                break
            self.position[self.heap_list[current_min_index][0]] = index
            self.position[self.heap_list[index][0]] = current_min_index
            self.heap_list[index], self.heap_list[current_min_index] = self.heap_list[current_min_index], self.heap_list[index]
            index = current_min_index
    
    # Нарисовать кучу
    def draw_heap(self):
        index_current_node = 0
        index_left_child = 1
        while (index_current_node < self.size):
            while((index_current_node < index_left_child) and (index_current_node < self.size)):
                print(self.storage[index_current_node], end="\t")
                index_current_node += 1
            print()
            index_left_child = index_left_child * 2 + 1
        print()
