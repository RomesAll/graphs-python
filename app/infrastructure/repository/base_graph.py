from collections import deque
from app.core.domain_services import IGraph
from app.core.entities import Node, Edge

class Graph(IGraph):
    """
    Класс реализации интерфейса IGraph для хранения вершин,
    узлов и дальнейшей работы с ними
    """
    def __init__(self, *, graph: dict[str|int, Node]):
        self._graph = graph

    @property
    def graph(self) -> dict[int, Node]:
        """
        Метод для получения графа
        :return:
        """
        return self._graph.copy() if self._graph else None

    def get_node(self, node_value: int) -> Node:
        return self._graph.get(node_value)

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

    def searching_isolated_node(self) -> list[Node]:
        """
        Метод для поиска изолированных вершин
        :return: tuple[Node]: Кортеж из вершин
        """
        isolated_nodes: set = set()
        for node in self._graph.values():
            if not node.edges and not node.parents:
                isolated_nodes.add(node)
        return list(isolated_nodes)

    def searching_loop_node(self) -> list[Node]:
        """
        Метод для поиска вершин с петлями
        :return: tuple[Node]: Кортеж из вершин
        """
        loop_nodes: set = set()
        for node in self._graph.values():
            for edge in node.edges:
                if edge.adjacent == node:
                    loop_nodes.add(node)
        return list(loop_nodes)

    def get_sorted_degree_nodes(self, desc: bool=True) -> dict:
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

    def get_path(self, start: Node, end: Node) -> list[Node] | None:
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
        return list(path) if path[-1] == end else None