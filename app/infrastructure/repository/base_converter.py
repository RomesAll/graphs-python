from app.core import Node, Edge
from app.core.domain_services import IConverterInputData
import json, enum

class FlagInputData(enum.Enum):
    input = 'input_data'
    output = 'output_data'

class JsonConverterListAdjacency(IConverterInputData):
    """
    Класс для конвертации входных данных из текстового фйла в формате json со списком смежностей
    в python хеш-таблицу, внутри которой храниться список смежностей, где ключ - это
    название вершины, а значение - это класс Node
    """
    def __init__(self, *, file_path: str):
        self.file_path = file_path
        self._file_data: dict | None = self.read_file()
        self._matrix_adjacent: list[list[int]] | None = self.get_matrix_adjacent()

    @staticmethod
    def __get_or_create_node(graph: dict, value):
        if graph.get(value) is None:
            return Node(value)
        return graph.get(value)

    @property
    def matrix_adjacent(self):
        return self._matrix_adjacent.copy() if self._matrix_adjacent else None

    def load(self) -> dict[str, Node] | None:
        if not (self._matrix_adjacent and self._file_data):
            return None
        graph: dict = dict()
        for node, list_edge in self._file_data.get(FlagInputData.input.value).items():
            current_node = self.__get_or_create_node(graph, node)
            graph[current_node.value] = current_node
            for node_edge in list_edge:
                adjacent_node = self.__get_or_create_node(graph, node_edge)
                graph[adjacent_node.value] = adjacent_node
                edge = Edge(adjacent_node)
                current_node.edges.append(edge)
                if current_node != edge.adjacent:
                    edge.adjacent.parents.append(current_node)
        if len(graph) == 0:
            return None
        return graph

    def read_file(self):
        try:
            file_data = None
            with open(self.file_path, 'r', encoding='utf-8') as file:
                file_data = json.load(file)
            return file_data
        except FileNotFoundError as e:
            raise FileNotFoundError('Файл не найден') from e
        except Exception as e:
            raise Exception('Не удалось прочитать файл') from e

    def get_matrix_adjacent(self) -> list[list[int]] | None:
        try:
            matrix = []
            if self._file_data is None:
                return None
            graph: dict = self._file_data.get('input_data')
            row_len = len(graph.keys())
            mapping: dict = {k: i for i, k in enumerate(graph.keys(), start=0)}
            for ind_row, row in enumerate(graph.values(), start=0):
                matrix.append([0] * row_len)
                for col in row:
                    index = mapping.get(col, None)
                    matrix[ind_row][index] = 1
            return matrix
        except IndexError as e:
            raise IndexError('Не удалось преобразовать входные данные в матрицу смежностей') from e
        except TypeError as e:
            raise TypeError('Некорректный тип входных данных') from e

    def save(self, data: list[list[int]]) -> bool:
        try:
            self._file_data.update({FlagInputData.output.value: {'matrix_adjacent': data}})
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(self._file_data, file, ensure_ascii=False)
            return True
        except FileNotFoundError as e:
            raise FileNotFoundError('Файл не найден') from e
        except Exception as e:
            raise Exception('Не удалось сохранить матрицу смежностей в файл') from e