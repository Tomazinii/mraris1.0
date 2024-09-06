
from typing import Any


class File:
    __file: Any
    __name: str

    def __init__(self, file, name):
        self.__file = file
        self.__name = name

    def get_name(self):
        return self.__name
    
    def get_file(self):
        return self.__file
        