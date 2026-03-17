from app.infrastructure.repository import JsonConverterListAdjacency, Graph
from app.core.services import GraphServiceFile
from rich.console import Console
from rich.panel import Panel

class ConsoleUI:
    def __init__(self):
        self.file_path: str | None = None
        self.graph_info: dict | None = None
        self.console: Console = Console()

    def get_progress_bar(self):
        pass

    def get_title_panel(self):
        panel = Panel.fit(
            "\nПрограмма, которая для заданного графа находит матрицу\n"
            "смежности и рассчитывает и выдает на экран следующие характеристики:\n"
            "\n* количество вершин и количество ребер; \n"
            "\n* наличие или отсутствие изолированных вершин и петель c указанием \nномеров "
            "соответствующих вершин; \n"
            "\n* список степеней вершин графа в порядке убывания с указанием \nномеров"
            "соответствующих вершин.\n",
            title="Представление графов в памяти компьютера",
            border_style="green",
            title_align='left',
            subtitle_align='left',
        )
        self.console.print(panel)

    def get_operation_panel(self):
        panel = Panel.fit(
            f"Выбран файл: {self.file_path}\n"
                      f"\n* [Нажмите \"1\"] Для получения информации о графе;"
                      f"\n* [Нажмите \"2\"] Для сохранения матрицы смежности в файл (формат json);"
                      f"\n* [Нажмите \"3\"] Для выхода.",
            title="Меню",
            border_style="green",
            title_align='left',
            subtitle_align='left',
        )
        self.console.print(panel)

    def start(self):
        self.get_title_panel()
        service: GraphServiceFile | None = None
        while self.file_path is None:
            try:
                self.file_path = input('Введите путь к файлу с входными данными в формате json (ctrl+c для выхода): ')
                service = GraphServiceFile(Graph, JsonConverterListAdjacency, self.file_path)
            except KeyboardInterrupt as e:
                self.console.print(e)
                return None
            except Exception as e:
                self.file_path = None
                self.console.print(e)
                continue
        print('\n')
        self.get_operation_panel()
        if service.get_graph() is None:
            return None
        while True:
            try:
                print()
                answer = input('Выберите действие [1-3]: ')
                match answer:
                    case "1":
                        graph_info = service.get_graph_info()
                        self.console.print(graph_info)
                    case "2":
                        if service.save_matrix():
                            self.console.print('Матрица смежностей сохранена в файл')
                            continue
                        self.console.print('Не удалось сохранить матрицу смежностей в файл')
                    case _:
                        break
            except KeyboardInterrupt as e:
                print(e)
                break
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    console = ConsoleUI()
    console.start()