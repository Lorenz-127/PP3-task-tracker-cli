import gspread
from google.oauth2.service_account import Credentials


class GoogleSheets:
    """
    Class For the Worksheet functions
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
    def get_sheet(cls, sheet_name):
        """
        Method to get the sheet needed

        :param sheet_name: the name of the sheet from the worksheet
        :return: the sheet to work with as worksheet
        """
        worksheet = cls.SHEET.worksheet(sheet_name)
        return worksheet

        # todo api error handling

        # todo exception handling
        
        # with restart of the program