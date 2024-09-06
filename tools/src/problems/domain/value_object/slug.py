import re

from src._shared.errors.bad_request import BadRequestError

class Slug:
    __slug: str

    def __init__(self, list_name):
        self.validate(list_name=list_name)
        self.slugfy(text=list_name)

        
    def validate(self, list_name):
        if not isinstance(list_name, str):
            raise BadRequestError("list_name must be a string")
        
    def slugfy(self, text):
        text = re.sub(r'[^\w\s-]', '', text).strip().lower()
        text = re.sub(r'[-\s]+', '-', text)
        self.__slug = text
        
    def get_slug(self):
        return self.__slug