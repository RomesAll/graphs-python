from abc import ABC, abstractmethod
from ..entities.graph_objects import Node

class IGraph(ABC):
    """
    Интерфейс для класса графа с основными операциями
    """
    @abstractmethod
    def get_graph(self) -> dict[int, Node]:
        """
        Метод получения графа
        :return: None
        """
        raise NotImplementedError()

    @abstractmethod
    def dfs(self):
        """
        Метод обхода графа в глубину, с помощью рекурсии
        :return: None
        """
        raise NotImplementedError()

    @abstractmethod
    def bfs(self):
        """
        Метод обхода графа в ширину, с помощью итеративного подхода
        :return: None
        """
        raise NotImplementedError()

    @abstractmethod
    def get_path(self, start: Node, end: Node) -> tuple[Node] | None:
        """
        Метод для поиска первого найденного пути от начала до конечного узла
        :param start: Узел начала
        :param end: Узел конца
        :return: tuple[Node]: Кортеж из списка узлов от начала до конечного узла
        """
        raise NotImplementedError()

    @abstractmethod
    def get_count_node(self) -> int:
        """
        Метод подсчета количества вершин в графе
        :return: int: кол-во вершин
        """
        raise NotImplementedError()

    @abstractmethod
    def get_count_edge(self) -> int:
        """
        Метод подсчета количества ребер в графе
        :return: int: кол-во ребер
        """
        raise NotImplementedError()

    @abstractmethod
    def searching_isolated_node(self) -> list[Node]:
        """
         Метод поиска изолированных вершины в графе
         :return: tuple[Node]: Найденные вершины
         """
        raise NotImplementedError()

    @abstractmethod
    def searching_loop_node(self) -> list[Node]:
        """
        Метод для поиска петель у вершин графа
        :return: tuple[Node]: Найденные вершины
        """
        raise NotImplementedError()

    @abstractmethod
    def get_sorted_degree_nodes(self, desc: bool=False) -> dict:
        """
        Метод для получения отсортированных вершин с их степенями
        :param: desc: Флаг, для сортировки в порядке убывания
        :return: Node: Список вершин
        """
        raise NotImplementedError()