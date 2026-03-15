from app.core import Node, Edge
from app.core.domain_services import IConverterInputData
import json

class JsonConverterListAdjacency(IConverterInputData):
    """
    Класс для конвертации входных данных из текстового фйла в формате json со списком смежностей
    в python хеш-таблицу, внутри которой храниться список смежностей, где ключ - это
    название вершины, а значение - это класс Node
    """
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_data: dict | None = None
        self.read_file()

    @staticmethod
    def get_or_create_node(graph: dict, value):
        if graph.get(value) is None:
            return Node(value)
        return graph.get(value)

    def load(self) -> dict[int, Node] | None:
        graph: dict = dict()
        if self.file_data is None:
            return None
        for node, list_edge in self.file_data.get('input_data').items():
            current_node = self.get_or_create_node(graph, node)
            graph[current_node.value] = current_node
            for node_edge in list_edge:
                adjacent_node = self.get_or_create_node(graph, node_edge)
                graph[adjacent_node.value] = adjacent_node
                edge = Edge(adjacent_node)
                current_node.edges.append(edge)
                if current_node != edge.adjacent:
                    edge.adjacent.parents.append(current_node)
            # graph[current_node.value] = current_node
        if len(graph) == 0:
            return None
        return graph

    def read_file(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.file_data = json.load(file)
        return self.file_data

    def save(self, data):
        self.file_data.update(data)
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.file_data, file, ensure_ascii=False)