from abc import ABC, abstractmethod

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
    def initialization_graph(self, matrix: Matrix) -> dict[int, Node]:
        """
        Функция создания графа.\n
        Для представления графа используется хеш-таблицы, списки, классы,
        как наиболее эффективный способ хранения данных в памяти компьютера.

        Входные данные: Двумерный массив один из двух вариантов:
        \n Матрица смежности для невзвешенного графа
        \n Пример: [[0,1], [1,0]];
        \n Матрица с перечислением вершин и ребер для взвешенного графа
        \n Пример: [[1,2,5], [2,1,9]], где:
        - 0-ой индекс от какой вершины идем;
        - 1-й индекс к какой вершине идем;
        - 2-й индекс вес ребра.
        :param matrix: Двумерный массив,
        :return: dict[int, Node]: хеш-таблица, где ключ имя - вершина, а значение - объект узла Node
        """
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