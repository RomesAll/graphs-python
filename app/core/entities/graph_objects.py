class Node:
    """
    Класс для хранения узлов графа
    """
    # todo: Для хранения узлов в edges и parents лучше всего использовать связные списки
    def __init__(self, value: object):
        self.value: object = value
        self.edges: list['Edge'] = [] # ребра узла
        self.parents: list['Node'] = [] # родители узла

class Edge:
    """
    Класс для хранения ребер, версия с взвешенным и невзвешенный графом
    """
    def __init__(self, adjacent, weight: int = 0):
        self.weight: int = weight
        self.adjacent: Node | None = None
        self.add_adjacent(adjacent)

    def add_adjacent(self, node: 'Node'):
        if not isinstance(node, Node):
            raise TypeError()
        self.adjacent = node