from core.user_data_entry import EntryData
from utils.output_rich import Rich


if __name__ == "__main__":
    Rich.simple_log("Запуск программы")
    EntryData.entry_report_data()
