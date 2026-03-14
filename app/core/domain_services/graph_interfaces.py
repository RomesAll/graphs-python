from abc import ABC, abstractmethod
from ..entities.graph_objects import Node

class GraphRepository(ABC):
    """
    Интерфейс для класса графа
    """
    @abstractmethod
    def initialization_graph(self, matrix: list[list[int]]):
        """
        Метод для инициализации графа в памяти компьютера в виде
        хеш-таблицы, классов и списков, как наиболее эффективный
        способ хранения вершин и узлов в памяти.

        В качестве входных данных могут быть использованы
        следующие представления графов в виде матрицы: \n
        - Перечисление множеств;
        - Матрица смежности;
        - Матрица инцидентности;
        - Перечень рёбер;
        - Векторы смежности;
        - Массивы смежности;
        - Списки смежности;
        - Структура с оглавлением;
        - Список вершин и список рёбер.

        :param matrix: Двумерный массив с описанием вершин и ребер
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def dfs(self):
        """
        Метод обхода графа в глубину, с помощью рекурсии
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def bfs(self):
        """
        Метод обхода графа в ширину, с помощью итеративного подхода
        :return: None
        """
        raise NotImplementedError

    @abstractmethod
    def get_path(self, start: Node, end: Node) -> tuple[Node]:
        """
        Метод для поиска первого найденного пути от начала до конечного узла
        :param start: Узел начала
        :param end: Узел конца
        :return: tuple[Node]: Кортеж из списка узлов от начала до конечного узла
        """
        raise NotImplementedError

    @abstractmethod
    def get_count_node(self) -> int:
        """
        Метод подсчета количества вершин в графе
        :return: int: кол-во вершин
        """
        pass

    @abstractmethod
    def get_count_edge(self) -> int:
        """
        Метод подсчета количества ребер в графе
        :return: int: кол-во ребер
        """
        pass

    @abstractmethod
    def searching_isolated_node(self) -> tuple[Node]:
        """
         Метод поиска изолированных вершины в графе
         :return: tuple[Node]: Найденные вершины
         """
        pass

    @abstractmethod
    def searching_loop_node(self) -> tuple[Node]:
        """
        Метод для поиска петель у вершин графа
        :return: tuple[Node]: Найденные вершины
        """
        pass

    @abstractmethod
    def get_sorted_degree_nodes(self, desc: bool=False) -> dict:
        """
        Метод для получения отсортированных вершин с их степенями
        :param: desc: Флаг, для сортировки в порядке убывания
        :return: Node: Список вершин
        """
        pass