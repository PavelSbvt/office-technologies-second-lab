from core.user_data_entry import UserEntryReportData
from utils.output_rich import Rich


if __name__ == "__main__":
    Rich.print_spacer()
    Rich.simple_log("Запуск программы")
    Rich.print_spacer()

    EntryReportData = UserEntryReportData()

    EntryReportData.entry_report_data()
    EntryReportData.save_data_to_csv()
    EntryReportData.get_csv_data()