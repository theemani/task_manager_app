"""
file_manager.py
Handles file operations for saving and loading tasks.
"""

import json


class FileManager:
    def __init__(self, filename):
        """
        Initializes the FileManager with the given filename.

        :param filename: str, the name of the file to manage
        """
        self.filename = filename

    def save_data(self, data):
        """
        Saves the given data to a file.

        :param data: list, the data to save
        """
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def load_data(self):
        """
        Loads data from a file.

        :return: list, the loaded data
        """
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
