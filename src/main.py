import sys

from PyQt6.QtWidgets import QApplication

from gui.main_window import MainWindow
from utils.output_rich import Rich


if __name__ == "__main__":
    Rich.print_spacer()
    Rich.simple_log("Запуск программы")
    Rich.print_spacer()

    App = QApplication(sys.argv)

    MyMainWindow = MainWindow()
    Rich.enter_log("Показ главного окна")
    Rich.print_spacer()
    MyMainWindow.show()

    sys.exit(App.exec())
