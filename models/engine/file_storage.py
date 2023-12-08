#!/usr/bin/python3
""" The FileStorage class manages storage and data retrieval
from a file, as evident from the save, reload and new methods
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """FileStorage class that serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns all the objects stored in
        the __objects dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """This method adds a new object to the __objects
        dictionary.
        """
        key = f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """This methos writes the current data in the
        __objects dictionary to the JSON file.
        """
        data = {}
        for key, obj in FileStorage.__objects.items():
            data[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(data, f, indent=4)

    def reload(self):
        """Deserializes the JSON fileto __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
            for key, value in data.items():
                if "BaseModel" in key:
                    reloaded = BaseModel(**value)
                    self.new(reloaded)
        except Exception:
            pass
