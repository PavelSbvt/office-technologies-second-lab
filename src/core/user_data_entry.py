import csv

from utils.output_rich import Rich


class UserEntryReportData:
    """
    Класс для сохранения и работы с данными, которые вводит пользователь
    """

    def __init__(self):
        # Авторы
        self.authors: str = ""
        # Правообладатель
        self.copyright_holders: str = ""
        # Название программы
        self.program_name: str = ""
        # Аннотация
        self.annotations: str = ""
        # Тип ЭВМ
        self.IBM_type:str = ""
        # Язык программирования
        self.program_language: str = ""
        # Операционная система
        self.operation_system: str = ""
        # Объём программы в мегабайтах
        self.scope_program: float = 0


    def get_authors(self) -> None:
        """
        Функция для получения фио авторов для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.authors

        :return: None
        """

        self.authors = Rich.input_data("Авторы").strip()

        if self.authors:
            Rich.debug_log(f"Авторы: {self.authors}")
        else:
            Rich.warning_log("Список авторов пуст.")


    def get_copyright_holders(self) -> None:
        """
        Функция для получения фио правообладателя для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.copyright_holders

        :return: None
        """

        self.copyright_holders = Rich.input_data("Правообладатель").strip()

        if self.copyright_holders:
            Rich.debug_log(f"Правообладатель: {self.copyright_holders}")
        else:
            Rich.warning_log("Не введена информация о правообладателе.")


    def get_program_name(self) -> None:
        """
        Функция для получения название программы для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.program_name

        :return: None
        """

        self.program_name = Rich.input_data("Название программы").strip()

        if self.program_name:
            Rich.debug_log(f"Название программы: {self.program_name}")
        else:
            Rich.warning_log("Не введено название программы.")


    def get_annotation(self) -> None:
        """
        Функция для получения аннотации для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.annotation

        :return: None
        """

        self.annotations = Rich.input_data("Аннотация").strip()

        if self.annotations:
            Rich.debug_log(f"Аннотация: {self.annotations}")
        else:
            Rich.warning_log("Не введена аннотация.")


    def get_IBM_type(self) -> None:
        """
        Функция для получения типа ЭВМ для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.IBM_type

        :return: None
        """

        self.IBM_type = Rich.input_data("Тип ЭВМ").strip()

        if self.IBM_type:
            Rich.debug_log(f"Тип ЭВМ: {self.IBM_type}")
        else:
            Rich.warning_log("Не введён тип ЭВМ.")


    def get_program_language(self) -> None:
        """
        Функция для получения языка программирования для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.program_language

        :return: None
        """

        self.program_language = Rich.input_data("Язык программирования").strip()

        if self.program_language:
            Rich.debug_log(f"Язык программирования: {self.program_language}")
        else:
            Rich.warning_log("Не введён язык программирования.")


    def get_operation_system(self) -> None:
        """
        Функция для получения имён поддерживаемых операционных системы для реферата.
        Получение данных из ввода консоли и присвоение полученных значений
        атрибуту класса - self.operation_system

        :return: None
        """

        self.operation_system = Rich.input_data("Поддерживаемые операционные системы").strip()

        if self.operation_system:
            Rich.debug_log(f"Поддерживаемые операционные системы: {self.operation_system}")
        else:
            Rich.warning_log("Не введены поддерживаемые операционные системы.")


    def get_scope_program(self) -> None:
        """
        Функция для получения объёма программы для реферата.
        Получение данных из ввода консоли и присвоение полученного значения
        атрибуту класса - self.scope_program

        :return: None
        """

        self.scope_program = Rich.input_data("Объём программы").strip()

        if self.scope_program:
            Rich.debug_log(f"Объём программы: {self.scope_program}")
        else:
            Rich.warning_log("Не введён объём программы.")


    def entry_report_data(self) -> None:
        """
        Ввод пользователем данных для заполнения полей в реферате

        Ввод данных через консоль и сохранение их в атрибуты класса

        :return: None
        """

        Rich.simple_log("Ввод данных реферата")

        self.get_authors()

        self.get_copyright_holders()

        self.get_program_name()

        self.get_annotation()

        self.get_IBM_type()

        self.get_program_language()

        self.get_operation_system()

        self.get_scope_program()


    def save_data_to_csv(self) -> None:
        """
        Функция для сохранения введённых данных в csv файл

        :return: None
        """

        csv_data = [self.authors, self.copyright_holders, self.program_name,
                    self.annotations, self.IBM_type, self.program_language,
                    self.operation_system, self.scope_program]

        with open('resources/csv/report-data.csv',
                  mode='w',
                  newline='',
                  encoding='utf-8'
                  ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(csv_data)

            Rich.success_log("Данные, введённые пользователем, сохранены в csv файл")

    def get_csv_data(self) -> None:
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

            Rich.debug_log("Данные из csv:")
            Rich.print_spacer_points()
            for row in csv_reader:
                Rich.debug_log(f"Авторы: {row[0]}")
                Rich.debug_log(f"Правообладатель: {row[1]}")
                Rich.debug_log(f"Название программы: {row[2]}")
                Rich.debug_log(f"Аннотация: {row[3]}")
                Rich.debug_log(f"Тип ЭВМ: {row[4]}")
                Rich.debug_log(f"Язык программирования: {row[5]}")
                Rich.debug_log(f"Поддерживаемые операционные системы: {row[6]}")
                Rich.debug_log(f"Объём программы: {row[7]}")
                Rich.print_spacer_points()

