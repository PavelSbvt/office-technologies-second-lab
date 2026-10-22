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

        self.report_data = []
        self.consent_processing_personal_data = []
        self.consent_info_about_author = []

        ui_path = Path('src/gui/ui/main_window.ui').as_posix()
        loadUi(ui_path, self)

        self.buttonBuildReport.clicked.connect(self.build_report)
        self.buttonBuildConsent.clicked.connect(self.build_connect)
        self.buttonBuildConsentInfoAboutAuthor.clicked.connect(
            self.build_consent_info_about_author)


    def build_consent_info_about_author(self) -> None:
        """
        Функция для заполнения шаблона согласия на указание сведений об авторе.

        :return: None
        """

        Rich.debug_log("Пользователь нажал кнопку сборки согласия на указание "
                       "сведений об авторе")

        self.get_input_data_for_consent_info_about_author()


    def build_connect(self) -> None:
        """
        Функция для заполнения шаблона согласия данными, которые ввёл пользователь.

        :return: None
        """

        Rich.debug_log("Пользователь нажал кнопку сборки согласия на обработку "
                       "персональных данных")

        self.get_input_data_for_consent_processing_personal_data()


    def build_report(self) -> None:
        """
        Функция для сбора заполненных данных, подстановки их в реферат

        :return: None
        """

        Rich.debug_log("Пользователь нажал кнопку сборки реферата")

        self.get_input_data_for_report()

        # self.fill_report_data(authors, copyright_holders, app_name,
        #                       annotation, IBM_type, program_language,
        #                       operation_system, scope_program)


    def get_input_data_for_consent_info_about_author(self) -> None:
        """
        Функция для получения данных, введённых пользователем в соответствующие поля
        вкладки заполнения шаблона согласия на указание сведений об авторе.

        :return: None
        """

        IBM_name = self.inputNameIBMProgram.text().strip()
        physical_person_data = self.inputPhysicalPersonData.text().strip()
        juridical_person_data = self.inputJuridicalPersonData.text().strip()
        authors_name = self.inputAuthorsName.text().strip()
        born_data = self.inputBornData.text().strip()
        citizenship = self.inputCitizenship.text().strip()
        place_of_life = self.inputPlaceOfLife.text().strip()
        src_percent = self.inputSrcPercent.text().strip()
        copyright_holder_name = self.inputCopyrightHolderName.text().strip()
        role = self.inputRole.text().strip()

        if (not IBM_name or not physical_person_data or not juridical_person_data
                or not authors_name or not born_data or not citizenship
                or not place_of_life or not src_percent
                or not copyright_holder_name or not role):
            Rich.warning_log("Проверьте поля - есть незаполненные поля")
            return

        Rich.print_spacer()

        Rich.debug_log(f"Текст поля 'Название программы ЭВМ': {IBM_name}")
        Rich.debug_log(f"Текст поля 'Физ. лицо': {physical_person_data}")
        Rich.debug_log(f"Текст поля 'Юр. лицо': {juridical_person_data}")
        Rich.debug_log(f"Текст поля 'ФИО автора': {authors_name}")
        Rich.debug_log(f"Текст поля 'Дата рождения': {born_data}")
        Rich.debug_log(f"Текст поля 'Гражданство': {citizenship}")
        Rich.debug_log(f"Текст поля 'Место жительства': {place_of_life}")
        Rich.debug_log(f"Текст поля 'Процент исходного кода': {src_percent}")
        Rich.debug_log(f"Текст поля 'ФИО правообладателя': {copyright_holder_name}")
        Rich.debug_log(f"Текст поля 'Должность': {role}")

        self.inputNameIBMProgram.setText("")
        self.inputPhysicalPersonData.setText("")
        self.inputJuridicalPersonData.setText("")
        self.inputAuthorsName.setText("")
        self.inputBornData.setText("")
        self.inputCitizenship.setText("")
        self.inputPlaceOfLife.setText("")
        self.inputSrcPercent.setText("")
        self.inputCopyrightHolderName.setText("")
        self.inputRole.setText("")

        Rich.print_spacer()
        Rich.debug_log("Поля очищены")

        self.save_consent_info_about_author_to_csv(
            IBM_name, physical_person_data, juridical_person_data,
            authors_name, born_data, citizenship, place_of_life,
            src_percent, copyright_holder_name, role)

        self.consent_info_about_author = (
            self.read_csv_data_for_consent_info_about_author())


    def get_input_data_for_consent_processing_personal_data(self) -> None:
        """
        Функция для получения данных, введённых пользователем в соответствующие поля
        вкладки заполнения шаблона соглашения на обработку персональных данных

        :return: None.
        """

        IBM_name = self.inputNameIBM.text().strip()
        full_name = self.inputFullName.text().strip()
        address = self.inputAddress.text().strip()
        serial_and_number_passport = self.inputPasportInfo.text().strip()
        data_issue = self.inputDataIssue.text().strip()
        issue_by = self.inputIssuedByWhom.text().strip()
        surname_and_initials = self.inputSurnameInitials.text().strip()

        if (not IBM_name or not full_name or not address or
                not serial_and_number_passport or not data_issue
                or not issue_by or not surname_and_initials):
            Rich.warning_log("Проверьте поля - есть незаполненные поля")
            return

        Rich.print_spacer()

        Rich.debug_log(f"Текст поля 'название программы ЭВМ': {IBM_name}")
        Rich.debug_log(f"Текст поля 'Фамилия Имя Отчество': {full_name}")
        Rich.debug_log(f"Текст поля 'Адрес прописки': {address}")
        Rich.debug_log(f"Текст поля 'Серия номер паспорта': {serial_and_number_passport}")
        Rich.debug_log(f"Текст поля 'Дата выдачи паспорта': {data_issue}")
        Rich.debug_log(f"Текст поля 'Кем выдан': {issue_by}")
        Rich.debug_log(f"Текст поля 'Фамилия И. О.': {surname_and_initials}")

        self.inputNameIBM.setText("")
        self.inputFullName.setText("")
        self.inputAddress.setText("")
        self.inputPasportInfo.setText("")
        self.inputDataIssue.setText("")
        self.inputIssuedByWhom.setText("")
        self.inputSurnameInitials.setText("")

        Rich.print_spacer()
        Rich.debug_log("Поля очищены")

        self.save_consent_to_processing_personal_data_to_csv( IBM_name, full_name,
            address, serial_and_number_passport, data_issue, issue_by, surname_and_initials)

        self.consent_processing_personal_data = (
            self.read_csv_data_for_consent_processing_personal_data())


    def get_input_data_for_report(self) -> None:
        """
        Функция для получения данных, введённых пользователем в соответствующие поля
        вкладки заполнения шаблона реферата

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

        self.save_report_data_to_csv(authors, copyright_holders, app_name,
                    annotation, IBM_type, program_language,
                    operation_system, scope_program)

        self.report_data = self.read_csv_data_report()


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


    def closeEvent(self, event) -> None:
        """
        Функция, вызывающаяся при закрытии окна.

        :param event: событие закрытия окна

        :return: None
        """

        Rich.exit_log("Выход из приложения - закрытие главного окна")
        Rich.print_spacer_points()
        event.accept()


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
    def save_report_data_to_csv(authors, copyright_holders, app_name,
                         annotation, IBM_type, program_language,
                         operation_system, scope_program) -> None:
        """
        Функция для сохранения введённых данных реферата в csv файл

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
    def save_consent_to_processing_personal_data_to_csv(
            IBM_name, full_name, address, serial_and_number_passport, data_issue,
            issue_by, surname_and_initials) -> None:
        """
        Функция для сохранения данных, введённых пользователем для заполнения шаблона
        о согласии на обработку персональных данных, в csv

        :return: None
        """

        csv_data = [IBM_name, full_name, address, serial_and_number_passport,
                    data_issue, issue_by, surname_and_initials]

        with open('resources/csv/consent-to-processing-personal-data.csv',
                  mode='w',
                  newline='',
                  encoding='utf-8'
                  ) as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(csv_data)

            Rich.success_log("Данные, введённые пользователем, сохранены в csv файл")


    @staticmethod
    def save_consent_info_about_author_to_csv(
            IBM_name, physical_person_data, juridical_person_data,
            authors_name, born_data, citizenship, place_of_life,
            src_percent, copyright_holder_name, role) -> None:
        """
        Функция для сохранения данных, введённых пользователем для заполнения шаблона
        согласия на указание сведений об авторе, в csv.

        :return: None
        """

        csv_data = [IBM_name, physical_person_data, juridical_person_data,
                    authors_name, born_data, citizenship, place_of_life,
                    src_percent, copyright_holder_name, role]

        with open('resources/csv/consent-info-about-author.csv',
                  mode='w',
                  newline='',
                  encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_data)

            Rich.success_log("Данные, введённые пользователем, сохранены в csv файл")


    @staticmethod
    def read_csv_data_report() -> list:
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

            data_massive = []

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

                data_massive.append(row)

        return data_massive


    @staticmethod
    def read_csv_data_for_consent_processing_personal_data() -> list:
        """
        Функция для чтения csv и возвращения прочитанных данных, введённых
        пользователем для заполнения шаблона согласия на обработку персональных данных

        :return: list - возвращает массив с прочитанными данными
        """

        with (open('resources/csv/consent-to-processing-personal-data.csv',
                   mode='r',
                   newline='',
                   encoding='utf-8')
              as csv_file):
            csv_reader = csv.reader(csv_file)

            data_massive = []

            for row in csv_reader:
                Rich.print_tabel(
                    "Данные из csv (согласие на обработку персональных данных)",
                    ["Параметр", "Значение"],
                    [
                        ["Название программы ЭВМ", row[0]],
                        ["ФИО", row[1]],
                        ["Адрес прописки", row[2]],
                        ["Серия номер паспорта", row[3]],
                        ["Дата выдачи паспорта", row[4]],
                        ["Кем выдан паспорт", row[5]],
                        ["Фамилия И. О.", row[6]],
                    ]
                )

                data_massive.append(row)

        return data_massive


    @staticmethod
    def read_csv_data_for_consent_info_about_author() -> list:
        """
        Функция для чтения csv и возвращения прочитанных данных, введённых
        пользователем для заполнения шаблона согласия на указание сведений об авторе.

        :return: list - возвращает массив с прочитанными данными
        """

        with (open('resources/csv/consent-info-about-author.csv',
                   mode='r',
                   newline='',
                   encoding='utf-8') as csv_file):
            csv_reader = csv.reader(csv_file)

            data_massive = []

            for row in csv_reader:
                Rich.print_tabel(
                    "Данные из csv (согласие на указание сведений об авторе)",
                    ["Параметр", "Значение"],
                    [
                        ["Название программы ЭВМ", row[0]],
                        ["Физ. лицо", row[1]],
                        ["Юр. лицо", row[2]],
                        ["ФИО автора", row[3]],
                        ["Дата рождения", row[4]],
                        ["Гражданство", row[5]],
                        ["Место жительства", row[6]],
                        ["Процент исходного кода", row[7]],
                        ["ФИО правообладателя", row[8]],
                        ["Должность", row[9]],
                    ]
                )

                data_massive.append(row)

        return data_massive
