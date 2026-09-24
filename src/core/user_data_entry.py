from utils.output_rich import Rich


class UserEntryData:
    """
    Класс для сохранения и работы с данными, которые вводит пользователь
    """

    def __init__(self):
        self.authors: list = []


    Rich.simple_log("Ввод данных пользователем")


    def entry_report_data(self) -> None:
        """
        Ввод пользователем данных для заполнения полей в реферате

        Ввод данных через консоль и сохранение их в атрибуты класса

        :return: None
        """

        raw = Rich.input_data("Авторы (через запятую)").strip()
        self.authors = [a.strip() for a in raw.split(",") if a.strip()]

        if not self.authors:
            print("Список авторов пуст.")


EntryData = UserEntryData()
