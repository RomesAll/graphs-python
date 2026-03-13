class Node:
    """
    Класс для хранения узлов графа
    """
    # todo Для хранения узлов в edges
    #  и parents лучше всего использовать связные списки
    def __init__(self, value):
        self.value = value
        self.edges = [] # ребра узла
        self.parents = [] # родитель узла
