

from src._shared.errors.bad_request import BadRequestError


class Category:
    __categories_type = ("exercises","tournament","challenges","games")
    __category: str

    def __init__(self, category: str):
        self.validate_category(category=category)
        self.__category = category


    def validate_category(self, category):
        if category not in self.__categories_type:
            raise BadRequestError("Invalid category")
        
    def get_category(self):
        return self.__category
