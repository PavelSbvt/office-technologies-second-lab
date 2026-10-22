import sys

from PyQt6.QtWidgets import QApplication

from core.user_data_entry import UserEntryReportData
from gui.main_window import MainWindow
from utils.output_rich import Rich


# 2.1: Лабораторная 2.1 (4 балла): Разработать программу, которая формирует несколько типов (согласия, рефераты, отчеты)
# документа (docx и подобие) и заполняет его введенными значениями. Если значение введено неверно, то либо просить
# исправить данную ошибку, либо формировать документ выделяя неправильно заполненные поля. Сохранять введенные
# пользователем данные в отдельный файл формата .csv

if __name__ == "__main__":
    Rich.print_spacer()
    Rich.simple_log("Запуск программы")
    Rich.print_spacer()

    App = QApplication(sys.argv)

    MyMainWindow = MainWindow()
    MyMainWindow.show()

    sys.exit(App.exec())
