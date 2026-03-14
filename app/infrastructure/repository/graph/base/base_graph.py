from collections import deque
from app.core.domain_services import IGraph
from app.core.entities import Node, Edge

class Graph(IGraph):
    """
    Класс реализации интерфейса IGraph для хранения вершин,
    узлов и дальнейшей работы с ними
    """
    def __init__(self, matrix: list[list[int]]):
        self._matrix: list[list[int]] = matrix
        self._graph: dict | None = None
        self.initialization_graph(matrix)

    @property
    def graph(self) -> dict:
        """
        Свойство для получения защищенного атрибута graph
        :return: dict: хеш-таблица с вершинами и узлами
        """
        return self._graph

    @property
    def matrix(self) -> list[list[int]]:
        """
        Свойство для получения защищенного атрибута matrix
        :return: list[list[int]]: двумерный массив с данными о графе
        """
        return self._matrix

    @matrix.setter
    def matrix(self, matrix: list[list[int]]):
        """
        Свойство для обновления защищенного атрибута matrix. После обновления
        происходит переинициализация графа
        :param matrix: list[list[int]]: новая матрица, двумерный массив
        :return:
        """
        self._matrix = matrix
        self.initialization_graph(matrix)

    def initialization_graph(self, matrix: list[list[int]],
                             is_weighted: bool = False):
        """
        Метод для инициализации графа в памяти компьютера в виде
        хеш-таблицы, классов и списков, как наиболее эффективный
        способ хранения вершин и узлов в памяти.

        В качестве входных данных могут быть использованы
        следующие представления графов в виде матрицы: \n
        - Перечисление множеств;
        - Матрица смежности (по умолчанию в классе Graph);
        - Матрица инцидентности;
        - Перечень рёбер;
        - Векторы смежности;
        - Массивы смежности;
        - Списки смежности;
        - Структура с оглавлением;
        - Список вершин и список рёбер.

        :param matrix: Двумерный массив с описанием вершин и ребер
        :param is_weighted: Граф взвешенный или невзвешенный
        :return:
        """
        self._graph: dict = dict()
        for i, row in enumerate(matrix):
            node: Node = self.__create_or_get_node(i)
            for j, col in enumerate(row):
                # Если элемент строки (col) равен 0, значит связи нет
                if col == 0: continue
                # В ином случае, если у элемента > 0, значит связь есть
                # и нужно либо новый узел возвращать, либо создавать новый
                adjacent_node: Node = self.__create_or_get_node(j)
                new_edge: Edge = Edge(adjacent_node, col) \
                    if is_weighted else Edge(adjacent_node)
                # Если узел ведет к той же вершине из которого он произошел,
                # то это петля, а значить атрибут parents устанавливать не надо
                if new_edge.adjacent is not node:
                    new_edge.adjacent.parents.append(node)
                node.edges.append(new_edge) # добавляем новый узел к вершине
            self._graph.update({i: node})

    def __create_or_get_node(self, node_value: int) -> Node:
        """
        Метод для получения вершины по его значению или создания нового
        :param node_value: Значение вершины
        :return:
        """
        if self._graph.get(node_value) is None:
            self._graph[node_value] = Node(node_value)
        return self._graph[node_value]

    def get_count_node(self) -> int:
        """
        Метод подсчета количества вершин
        :return: int: Кол-во вершин
        """
        return len(self._graph.keys())

    def get_count_edge(self) -> int:
        """
        Метод подсчета количества узлов
        :return: int: Кол-во узлов
        """
        result_count = 0
        passed_node = set()
        for node in self._graph.values():
            for edge in node.edges:
                if edge.adjacent.value not in passed_node:
                    result_count += 1
                    passed_node.add(node.value)
        return result_count

    def searching_isolated_node(self) -> tuple[Node]:
        """
        Метод для поиска изолированных вершин
        :return: tuple[Node]: Кортеж из вершин
        """
        isolated_nodes: set = set()
        for node in self._graph.values():
            if not node.edges and not node.parents:
                isolated_nodes.add(node)
        return tuple(isolated_nodes)

    def searching_loop_node(self) -> tuple[Node]:
        """
        Метод для поиска вершин с петлями
        :return: tuple[Node]: Кортеж из вершин
        """
        loop_nodes: set = set()
        for node in self._graph.values():
            for edge in node.edges:
                if edge.adjacent == node:
                    loop_nodes.add(node)
        return tuple(loop_nodes)

    def get_sorted_degree_nodes(self, desc: bool=False) -> dict:
        """
        Метод для получения степеней вершин
        :param desc: Сортировка по убыванию
        :return: dict: хеш-таблица со степенями вершин
        """
        degree_all_nodes = dict()
        for node in self._graph.values():
            degree_all_nodes[node.value] = len(node.edges)
        return dict(sorted(degree_all_nodes.items(), reverse=desc))

    def dfs(self):
        """
        Метод для перебора графа в глубину
        :return:
        """
        passed: set = set()
        def dfs_inner(node: Node):
            nonlocal passed
            print(node.value, node)
            passed.add(node.value)
            for edge in node.edges:
                if edge.adjacent.value not in passed:
                    dfs_inner(edge.adjacent)
        for current_node in self._graph.values():
            if current_node.value not in passed:
                dfs_inner(current_node)

    def bfs(self):
        """
        Метод для перебора графа в ширину
        :return:
        """
        passed: set = set()
        def bfs_inner(node_start: Node):
            nonlocal passed
            current_level = deque([node_start])
            new_level = deque()
            level = 0
            while current_level:
                node = current_level.popleft()
                passed.add(node.value)
                print(level, node.value, node)
                for edge in node.edges:
                    if edge.adjacent.value not in passed:
                        new_level.append(edge.adjacent)
                if not current_level:
                    current_level = new_level.copy()
                    new_level.clear()
                    level += 1
        for current_node in self._graph.values():
            if current_node.value not in passed:
                bfs_inner(current_node)

    def get_path(self, start: Node, end: Node) -> tuple[Node] | None:
        passed: set = set()
        path: deque = deque([start])
        stack: deque = deque([start])
        while stack:
            current_node = stack[-1]
            passed.add(current_node.value)
            has_children = False
            if current_node == end:
                path = stack.copy()
                stack.clear()
            for edge in current_node.edges:
                if edge.adjacent.value not in passed:
                    stack.append(edge.adjacent)
                    has_children = True
                    break
                has_children = False
            if current_node != end and not has_children:
                stack.pop()
                continue
        return tuple(path) if path[-1] == end else None