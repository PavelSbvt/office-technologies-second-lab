import re


class Validation:
    """
    Класс для работы с данными, которые вводит пользователь - проверки
    """

    @staticmethod
    def is_not_empty(value: str) -> bool:
        """
        Поле не пустое (после strip).
        """

        return bool(value and value.strip())


    @staticmethod
    def is_valid_date(value: str) -> bool:
        """
        Дата в формате ДД.ММ.ГГГГ.
        """

        return bool(re.fullmatch(r'\d{2}\.\d{2}\.\d{4}', value))


    @staticmethod
    def is_valid_passport(value: str) -> bool:
        """
        Серия и номер паспорта: 4 цифры, пробел, 6 цифр. Пример: '1234 567890'.
        """

        return bool(re.fullmatch(r'\d{4}\s\d{6}', value))


    @staticmethod
    def is_valid_percent(value: str) -> bool:
        """
        Целое число от 0 до 100.
        """

        return value.isdigit() and 0 <= int(value) <= 100


    @staticmethod
    def is_valid_birth_date(value: str) -> bool:
        """
        Дата рождения в формате ДД.ММ.ГГГГ с разумным годом.
        """

        if not Validation.is_valid_date(value):
            return False
        year = int(value.split('.')[2])
        return 1900 <= year <= 2026


    @staticmethod
    def is_valid_full_name(value: str) -> bool:
        """
        ФИО: каждое слово с заглавной буквы, только буквы, пробелы, дефис.
        Минимум два слова. Пример: 'Иванов Иван Иванович'.
        """

        # каждое слово: заглавная + строчные/заглавные (для дефиса внутри)
        pattern = r'[А-ЯЁA-Z][А-Яа-яЁёA-Za-z\-]*'
        words = value.split()

        if len(words) < 2:
            return False

        return all(re.fullmatch(pattern, word) for word in words)


    @staticmethod
    def is_valid_initials(value: str) -> bool:
        """
        Фамилия и инициалы: 'Иванов И. О.' или 'Иванов И.О.'.
        Фамилия и инициалы — с заглавной буквы.
        """

        return bool(re.fullmatch(
            r'[А-ЯЁA-Z][А-Яа-яЁёA-Za-z\-]*\s+[А-ЯЁA-Z]\.\s*[А-ЯЁA-Z]\.',
            value
        ))


    @staticmethod
    def is_valid_citizenship(value: str) -> bool:
        """
        Гражданство: буквы, пробелы, дефис, скобки.
        Пример: 'Российская Федерация', 'Россия (РФ)'.
        """

        return bool(re.fullmatch(r'[А-Яа-яЁёA-Za-z\s\-\(\)]+', value))


    @staticmethod
    def is_valid_positive_number(value: str) -> bool:
        """
        Положительное число (целое или дробное). Пример: '964' или '12.5'.
        """

        try:
            return float(value.replace(',', '.')) > 0
        except ValueError:
            return False


    @staticmethod
    def is_valid_program_language(value: str) -> bool:
        """
        Язык программирования: буквы, цифры, '+', '#', пробел, дефис.
        """

        return bool(re.fullmatch(r'[A-Za-zА-Яа-яЁё0-9\+\#\s\-]+', value))


    @staticmethod
    def is_valid_os(value: str) -> bool:
        """
        Название ОС / типа ЭВМ: буквы, цифры, пробелы, запятые, дефис, точка.
        """

        return bool(re.fullmatch(r'[A-Za-zА-Яа-яЁё0-9\s,\.\-]+', value))


    @staticmethod
    def is_valid_full_name_list(value: str) -> bool:
        """
        Список ФИО через запятую. Каждое — валидное ФИО.
        Пример: 'Иванов Иван Иванович, Петров Пётр Петрович'.
        """

        parts = [p.strip() for p in value.split(',')]
        parts = [p for p in parts if p]  # убираем пустые (двойные запятые)

        if not parts:
            return False

        return all(Validation.is_valid_full_name(p) for p in parts)


    @staticmethod
    def is_valid_initials_list(value: str) -> bool:
        """
        Список «Фамилия И. О.» через запятую.
        Каждый элемент — валидные инициалы (фамилия и инициалы с заглавной).
        Пример: 'Иванов И. О., Петров П. П.'.
        """

        parts = [p.strip() for p in value.split(',')]
        parts = [p for p in parts if p]

        if not parts:
            return False

        return all(Validation.is_valid_initials(p) for p in parts)

    @staticmethod
    def is_valid_copyright_holder(value: str) -> bool:
        """
        Правообладатель: либо ФИО, либо название организации.
        Пример: 'Иванов Иван Иванович' или 'ООО "Ромашка"'.
        """

        value = value.strip()

        if not value:
            return False

        if not re.search(r'[А-Яа-яЁёA-Za-z]', value):
            return False

        if Validation.is_valid_full_name(value):
            return True

        org_pattern = r'[А-Яа-яЁёA-Za-z0-9\s"«»\'\-\.\,\(\)]+'
        return bool(re.fullmatch(org_pattern, value))


    @staticmethod
    def is_valid_copyright_holder_list(value: str) -> bool:
        """
        Список правообладателей через запятую. Каждый — ФИО или организация.
        """

        parts = [p.strip() for p in value.split(',')]
        parts = [p for p in parts if p]

        if not parts:
            return False

        return all(Validation.is_valid_copyright_holder(p) for p in parts)
