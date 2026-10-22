from pathlib import Path
import csv

from docxtpl import DocxTemplate

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from utils.output_rich import Rich


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ui_path = Path('src/gui/ui/main_window.ui').as_posix()
        loadUi(ui_path, self)

        self.buttonBuildReport.clicked.connect(self.build_report)


    def build_report(self) -> None:
        """
        Функция для сбора заполненных данных, подстановки их в реферат

        :return: None
        """

        Rich.debug_log("Пользователь нажал кнопку сборки реферата")

        self.get_input_data_for_report()


    def get_input_data_for_report(self) -> None:
        """
        Функция для получения данных, введённых пользователем в соответствующие поля.

        :return: None
        """

        authors = self.inputAuthors.text().strip()
        copyright_holders = self.inputCopyrightHolders.text().strip()
        app_name = self.inputAppName.text().strip()
        annotation = self.inputAnnotation.text().strip()
        IBM_type = self.inputTypeIBM.text().strip()
        program_language = self.inputProgramLanguage.text().strip()
        operation_system = self.inputOS.text().strip()
        scope_program = self.inputScopeProgram.text().strip()

        if (not authors or not copyright_holders or not app_name
                or not annotation or not IBM_type or not program_language
                or not operation_system or not scope_program):
            Rich.warning_log("Проверьте поля - есть незаполненные поля")
            return

        Rich.print_spacer()

        Rich.debug_log(f"Текст поля 'авторы': {authors}")
        Rich.debug_log(f"Текст поля 'правообладатели': {copyright_holders}")
        Rich.debug_log(f"Текст поля 'Название приложения': {app_name}")
        Rich.debug_log(f"Текст поля 'Аннотация': {annotation}")
        Rich.debug_log(f"Текст поля 'Тип ЭВМ': {IBM_type}")
        Rich.debug_log(f"Текст поля 'Язык программирования': {program_language}")
        Rich.debug_log(f"Текст поля 'Операционная система': {operation_system}")
        Rich.debug_log(f"Текст поля 'Объём программы в мегабайтах': {scope_program}")

        self.inputAuthors.setText("")
        self.inputCopyrightHolders.setText("")
        self.inputAppName.setText("")
        self.inputAnnotation.setText("")
        self.inputTypeIBM.setText("")
        self.inputProgramLanguage.setText("")
        self.inputOS.setText("")
        self.inputScopeProgram.setText("")

        Rich.print_spacer()
        Rich.debug_log("Поля очищены")

        self.save_data_to_csv(authors, copyright_holders, app_name,
                    annotation, IBM_type, program_language,
                    operation_system, scope_program)

        self.read_csv_data()

        self.fill_report_data(authors, copyright_holders, app_name,
                    annotation, IBM_type, program_language,
                    operation_system, scope_program)


    @staticmethod
    def fill_report_data(authors, copyright_holders, app_name,
                    annotation, IBM_type, program_language,
                    operation_system, scope_program):
        """
        Функция для заполнения документа Реферат.docx данными, которые ввёл пользователь

        :return: None
        """

        path_template_report = Path("resources/documents/report.docx").as_posix()
        doc = DocxTemplate(path_template_report)

        context = {
            'authors': authors,
            'copyright_holder': copyright_holders,
            'program_name': app_name,
            'annotation': annotation,
            'computer_type': IBM_type,
            'language': program_language,
            'os': operation_system,
            'program_size': scope_program
        }

        doc.render(context)
        path_save_doc = Path("output/output-report.docx").as_posix()
        doc.save(path_save_doc)

        Rich.success_log("Документ успешно создан!")


    @staticmethod
    def save_data_to_csv(authors, copyright_holders, app_name,
                    annotation, IBM_type, program_language,
                    operation_system, scope_program) -> None:
        """
        Функция для сохранения введённых данных в csv файл

        :return: None
        """

        csv_data = [authors, copyright_holders, app_name,
                    annotation, IBM_type, program_language,
                    operation_system, scope_program]

        with open('resources/csv/report-data.csv',
                  mode='w',
                  newline='',
                  encoding='utf-8'
                  ) as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(csv_data)

            Rich.success_log("Данные, введённые пользователем, сохранены в csv файл")


    @staticmethod
    def read_csv_data() -> None:
        """
        Функция для получения данных из csv

        :return: list - массив данных (ранее были введены пользователем
         для заполнения шаблона реферата)
        """

        with (open('resources/csv/report-data.csv',
                   mode='r',
                   newline='',
                   encoding='utf-8')
              as csv_file):
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                Rich.print_tabel(
                    "Данные из csv (реферат)",
                    ["Параметр", "Значение"],
                    [
                        ["Авторы", row[0]],
                        ["Правообладатель", row[1]],
                        ["Название программы", row[2]],
                        ["Аннотация", row[3]],
                        ["Тип ЭВМ", row[4]],
                        ["Язык программирования", row[5]],
                        ["Поддерживаемые операционные системы", row[6]],
                        ["Объём программы", row[7]],
                    ]
                )


    def mousePressEvent(self, event) -> None:
        """
        Обработчик события нажатия кнопки мыши.

        :param event: Принимает event - объект события, содержащий информацию о нажатии
        (какая кнопка, координаты и т.д.).

        :return: None
        """

        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            event.accept()


    def mouseMoveEvent(self, event) -> None:
        """
        Обработчик события движения мыши.

        :param event: Принимает event - объект события, содержащий информацию о нажатии
        (какая кнопка, координаты и т.д.).

        :return: None
        """

        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.drag_position
            self.move(self.pos() + delta)
            self.drag_position = event.globalPosition().toPoint()
            event.accept()