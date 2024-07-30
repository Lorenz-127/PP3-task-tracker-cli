import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any

class GoogleSheets:
    """
    Class for managing Google Sheets operations.
    """

    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    # Global constants as class attributes
    CREDS = Credentials.from_service_account_file("creds.json")
    SCOPED_CREDS = CREDS.with_scopes(SCOPE)
    GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
    SHEET = GSPREAD_CLIENT.open("task_tracker")

    @classmethod
    def get_worksheet(cls, sheet_name: str) -> gspread.Worksheet:
        """
        Retrieve a specific worksheet from the Google Sheet.

        :param sheet_name: The name of the worksheet.
        :return: The requested worksheet.
        :raises ValueError: If the worksheet doesn't exist.
        """
        try:
            return cls.SHEET.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            raise ValueError(f"Worksheet '{sheet_name}' not found.")

    @classmethod
    def get_all_records(cls, sheet_name: str) -> List[Dict[str, Any]]:
        """
        Retrieve all records from a specific worksheet.

        :param sheet_name: The name of the worksheet.
        :return: A list of dictionaries containing all records.
        """
        worksheet = cls.get_worksheet(sheet_name)
        return worksheet.get_all_records()

    @classmethod
    def append_row(cls, sheet_name: str, row_data: List[Any]) -> None:
        """
        Append a row to a specific worksheet.

        :param sheet_name: The name of the worksheet.
        :param row_data: The data to be appended as a new row.
        """
        worksheet = cls.get_worksheet(sheet_name)
        worksheet.append_row(row_data)

    @classmethod
    def update_cell(cls, sheet_name: str, row: int, col: int, value: Any) -> None:
        """
        Update a specific cell in a worksheet.

        :param sheet_name: The name of the worksheet.
        :param row: The row number of the cell to update.
        :param col: The column number of the cell to update.
        :param value: The new value for the cell.
        """
        worksheet = cls.get_worksheet(sheet_name)
        worksheet.update_cell(row, col, value)

    @classmethod
    def find_row(cls, sheet_name: str, search_val: Any, col: int = 1) -> int:
        """
        Find a row in a worksheet based on a search value in a specific column.

        :param sheet_name: The name of the worksheet.
        :param search_val: The value to search for.
        :param col: The column to search in (default is 1, the first column).
        :return: The row number of the found cell.
        :raises ValueError: If the search value is not found.
        """
        worksheet = cls.get_worksheet(sheet_name)
        try:
            cell = worksheet.find(str(search_val), in_column=col)
            return cell.row
        except gspread.exceptions.CellNotFound:
            raise ValueError(f"Value '{search_val}' not found in column {col}.")

    @classmethod
    def delete_row(cls, sheet_name: str, row: int) -> None:
        """
        Delete a specific row from a worksheet.

        :param sheet_name: The name of the worksheet.
        :param row: The row number to delete.
        """
        worksheet = cls.get_worksheet(sheet_name)
        worksheet.delete_row(row)
        