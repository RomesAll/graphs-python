class Node:
    """
    Класс для хранения узлов графа
    """
    # todo: Для хранения узлов в edges
    #  и parents лучше всего использовать связные списки
    def __init__(self, value: object):
        self.value: object = value
        self.edges: list[Node] = [] # ребра узла
        self.parents: list[Node] = [] # родители узла

class Edge:
    """
    Класс для хранения ребер, версия с взвешанным и невзвешенный графом
    """
    def __init__(self, adjacent, weight: int=0):
        self.weight: int = weight
        self.adjacent: Node = adjacent