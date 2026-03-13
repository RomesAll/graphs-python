from abc import ABC, abstractmethod
from collections import deque

Matrix = list[list[int]]

class Node:
    """
    Класс для хранения узлов графа
    """
    # todo: Для хранения узлов в edges
    #  и parents лучше всего использовать связные списки
    def __init__(self, value: object):
        self.value: object = value
        self.edges: list[Edge] = [] # ребра узла
        self.parents: list[Node] = [] # родители узла

class Edge:
    """
    Класс для хранения ребер, версия с взвешенным и невзвешенный графом
    """
    def __init__(self, adjacent, weight: int=0):
        self.weight: int = weight
        self.adjacent: Node = adjacent

class InterfaceGraph(ABC):
    @abstractmethod
    def initialization_graph(self, matrix: Matrix):
        raise NotImplementedError

    @abstractmethod
    def dfs(self, node: Node, passed: set):
        """
        Функция обхода графа в глубину, с помощью рекурсии
        :param node: Узел начала
        :param passed: Список узлов, которые мы прошли
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def bfs(self, node: Node, passed: set):
        """
        Функция обхода графа в ширину, с помощью итеративного подхода
        :param node: Узел начала
        :param passed: Список узлов, которые мы прошли
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def get_path(self, start: Node, end: Node, passed: set, path: list) -> bool:
        """
        Функция для поиска первого пути
        :param start: Узел начала
        :param end: Узел конца
        :param passed: Список узлов, которые мы прошли
        :param path: Список узлов найденного пути от начала до конца
        :return: bool
        """
        raise NotImplementedError

    @abstractmethod
    def get_app_path(self, start: Node, end: Node, passed: set, path: list[list]):
        """
        Функция для поиска всех путей
        :param start: Узел начала
        :param end: Узел конца
        :param passed: Список узлов, которые мы прошли
        :param path: Список узлов найденного пути от начала до конца
        :return: bool
        """
        raise NotImplementedError

    @abstractmethod
    def calculate_node(self) -> int:
        """
        Функция подсчета кол-ва вершин
        :return:
        """
        pass

    @abstractmethod
    def calculate_edge(self) -> int:
        """
        Функция подсчета кол-ва ребер
        :return:
        """
        pass

    @abstractmethod
    def searching_isolated_node(self) -> Node | list[Node] | None:
        """
         Функция поиска изолированной вершины
         :return: Node: Найденная вершина(ы), либо None
         """
        pass

    @abstractmethod
    def searching_loop_node(self) -> Node | list[Node] | None:
        """
        Функция для поиска петли у вершин
        :return: Node: Найденная вершина(ы), либо None
        """
        pass

    @abstractmethod
    def get_degree_all_nodes(self) -> list[Node] | None:
        """
        Функция для вывода всех степеней вершин в порядке убывания
        :return: Node: Список вершин
        """
        pass


class Graph:

    def __init__(self, matrix: Matrix):
        self._matrix: Matrix = matrix
        self._graph: dict | None = None
        self.initialization_graph(matrix)

    @property
    def graph(self):
        return self._graph

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: Matrix):
        self._matrix = matrix
        self.initialization_graph(matrix)

    def initialization_graph(self, matrix: Matrix):
        self._graph: dict = dict()
        for row_ind, row in enumerate(matrix):
            node: Node = self.create_or_get_node(row_ind)
            for col_ind, col in enumerate(row):
                if col == 0:
                    continue
                node_edge: Edge | None = None
                if col == 1 and col_ind != row_ind:
                    node_adjacent: Node = self.create_or_get_node(col_ind)
                    node_adjacent.parents.append(node)
                    node_edge: Edge = Edge(node_adjacent)
                if col == 2 and col_ind == row_ind:
                    node_edge: Edge = Edge(node)
                node.edges.append(node_edge)
            self._graph.update({row_ind: node})

    def create_or_get_node(self, value: int):
        if self._graph.get(value) is None:
            self._graph[value] = Node(value)
        return self._graph[value]


g = Graph(matrix=[
    [2, 1, 1, 0, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
])