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

