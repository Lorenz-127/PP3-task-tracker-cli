import json
from database.json_manager import JSONManager
from utils.google_sheets import GoogleSheets
from typing import Dict, Any, List
from datetime import datetime
import os


class JSONManager:
    """
    Class for managing local JSON file operations.

    This class provides methods to read, write, and update JSON files
    used for local storage in the Todo List application.
    """

    def __init__(self, data_directory: str = "../data"):
        """
        Initialize the JSONManager.

        :param data_directory: Directory to store JSON files (default: "data")
        """
        self.data_directory = data_directory
        os.makedirs(self.data_directory, exist_ok=True)

    def _get_file_path(self, filename: str) -> str:
        """Get the full file path for a JSON file."""
        return os.path.join(self.data_directory, filename)

    def read_json(self, filename: str) -> Dict[str, Any]:
        """
        Read data from a JSON file.

        :param filename: Name of the JSON file to read
        :return: Dictionary containing the JSON data
        """
        file_path = self._get_file_path(filename)
        try:
            with open(file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def write_json(self, filename: str, data: Dict[str, Any]) -> None:
        """
        Write data to a JSON file.

        :param filename: Name of the JSON file to write
        :param data: Dictionary containing the data to write
        """
        file_path = self._get_file_path(filename)
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)

    def update_json(self, filename: str, key: str, value: Any) -> None:
        """
        Update a specific key in a JSON file.

        :param filename: Name of the JSON file to update
        :param key: Key to update or add
        :param value: New value for the key
        """
        data = self.read_json(filename)
        data[key] = value
        self.write_json(filename, data)

    def get_user(self, username: str) -> Dict[str, Any]:
        """
        Get user data from users.json.

        :param username: Username to look up
        :return: User data dictionary
        """
        users = self.read_json("users.json").get("users", [])
        for user in users:
            if user["username"] == username:
                return user
        return {}

    def add_user(self, user_data: Dict[str, Any]) -> None:
        """
        Add a new user to users.json.

        :param user_data: Dictionary containing user data
        """
        users = self.read_json("users.json")
        users.setdefault("users", []).append(user_data)
        self.write_json("users.json", users)

    def update_task_metadata(self, task_id: int, metadata: Dict[str, Any]) -> None:
        """
        Update metadata for a specific task in tasks_metadata.json.

        :param task_id: ID of the task to update
        :param metadata: New metadata for the task
        """
        tasks_metadata = self.read_json("tasks_metadata.json")
        tasks_metadata.setdefault("tasks", [])

        for task in tasks_metadata["tasks"]:
            if task["id"] == task_id:
                task.update(metadata)
                break
        else:
            tasks_metadata["tasks"].append({"id": task_id, **metadata})

        self.write_json("tasks_metadata.json", tasks_metadata)

    def get_task_metadata(self, task_id: int) -> Dict[str, Any]:
        """
        Get metadata for a specific task from tasks_metadata.json.

        :param task_id: ID of the task to retrieve
        :return: Task metadata dictionary
        """
        tasks_metadata = self.read_json("tasks_metadata.json").get("tasks", [])
        for task in tasks_metadata:
            if task["id"] == task_id:
                return task
        return {}

    def update_local_cache(self, cache_data: Dict[str, List[Dict[str, Any]]]) -> None:
        """
        Update the local_cache.json file with new data.

        :param cache_data: Dictionary containing cache data to update
        """
        self.write_json("local_cache.json", cache_data)

    def get_local_cache(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Get the entire contents of local_cache.json.

        :return: Dictionary containing all cached data
        """
        return self.read_json("local_cache.json")
