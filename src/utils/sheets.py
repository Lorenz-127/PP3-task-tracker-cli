import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any, Optional
from contextlib import contextmanager

class GoogleSheets:
    """
    Class for managing Google Sheets operations.
    
    This class provides methods to interact with Google Sheets, including
    reading, writing, updating, and deleting data. It uses a context manager
    for efficient resource management.

        Example usage:
        with GoogleSheets() as gs:
            data = gs.get_all_records("Sheet1")
            gs.append_row("Sheet1", ["New", "Data", "Here"])
            gs.batch_update("Sheet1", [
                {"range": "A1:B1", "values": [["Updated", "Cell"]]}
            ])
    """

    SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive",
    ]

    def __init__(self, creds_file: str = "creds.json"):
        """
        Initialize the GoogleSheets class.

        :param creds_file: Path to the credentials JSON file (default: "creds.json")
        """
        self.creds = Credentials.from_service_account_file(creds_file)
        self.scoped_creds = self.creds.with_scopes(self.SCOPE)
        self.client = None
        self.sheet = None

    def __enter__(self):
        """Set up the Google Sheets connection when entering the context."""
        self.client = gspread.authorize(self.scoped_creds)
        self.sheet = self.client.open("task_tracker")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up the Google Sheets connection when exiting the context."""
        self.client = None
        self.sheet = None

    def get_worksheet(self, sheet_name: str) -> gspread.Worksheet:
        """
        Retrieve a specific worksheet from the Google Sheet.

        :param sheet_name: The name of the worksheet.
        :return: The requested worksheet.
        :raises ValueError: If the worksheet doesn't exist.
        """
        try:
            return self.sheet.worksheet(sheet_name)
        except gspread.exceptions.WorksheetNotFound:
            raise ValueError(f"Worksheet '{sheet_name}' not found.")

    def get_all_records(self, sheet_name: str) -> List[Dict[str, Any]]:
        """
        Retrieve all records from a specific worksheet.

        :param sheet_name: The name of the worksheet.
        :return: A list of dictionaries containing all records.
        """
        worksheet = self.get_worksheet(sheet_name)
        return worksheet.get_all_records()

    def append_row(self, sheet_name: str, row_data: List[Any]) -> None:
        """
        Append a row to a specific worksheet.

        :param sheet_name: The name of the worksheet.
        :param row_data: The data to be appended as a new row.
        """
        worksheet = self.get_worksheet(sheet_name)
        worksheet.append_row(row_data)

    def update_cell(self, sheet_name: str, row: int, col: int, value: Any) -> None:
        """
        Update a specific cell in a worksheet.

        :param sheet_name: The name of the worksheet.
        :param row: The row number of the cell to update.
        :param col: The column number of the cell to update.
        :param value: The new value for the cell.
        """
        worksheet = self.get_worksheet(sheet_name)
        worksheet.update_cell(row, col, value)

    def find_row(self, sheet_name: str, search_val: Any, col: int = 1) -> int:
        """
        Find a row in a worksheet based on a search value in a specific column.

        :param sheet_name: The name of the worksheet.
        :param search_val: The value to search for.
        :param col: The column to search in (default is 1, the first column).
        :return: The row number of the found cell.
        :raises ValueError: If the search value is not found.
        """
        worksheet = self.get_worksheet(sheet_name)
        try:
            cell = worksheet.find(str(search_val), in_column=col)
            return cell.row
        except gspread.exceptions.CellNotFound:
            raise ValueError(f"Value '{search_val}' not found in column {col}.")

    def delete_row(self, sheet_name: str, row: int) -> None:
        """
        Delete a specific row from a worksheet.

        :param sheet_name: The name of the worksheet.
        :param row: The row number to delete.
        """
        worksheet = self.get_worksheet(sheet_name)
        worksheet.delete_row(row)

    def batch_update(self, sheet_name: str, updates: List[Dict[str, Any]]) -> None:
        """
        Perform batch updates on a worksheet.

        :param sheet_name: The name of the worksheet.
        :param updates: A list of dictionaries containing update information.
                        Each dictionary should have 'range' and 'values' keys.
        Example:
            updates = [
                {"range": "A1:B1", "values": [["Updated", "Cell"]]},
                {"range": "C2", "values": [["Another Update"]]}
            ]
        """
        worksheet = self.get_worksheet(sheet_name)
        worksheet.batch_update(updates)

    def get_column(self, sheet_name: str, col: int) -> List[Any]:
        """
        Get all values in a specific column.

        :param sheet_name: The name of the worksheet.
        :param col: The column number to retrieve.
        :return: A list of values in the specified column.
        """
        worksheet = self.get_worksheet(sheet_name)
        return worksheet.col_values(col)

    def sync_task(self, task_id: int) -> None:
        """
        Synchronize a task between local storage and Google Sheets.

        :param task_id: The ID of the task to synchronize.
        """
        local_task = self.get_local_task(task_id)
        cloud_task = self.get_cloud_task(task_id)
        synced_task = self.resolve_sync_conflict(local_task, cloud_task)
        self.update_local_task(synced_task)
        self.update_cloud_task(synced_task)

