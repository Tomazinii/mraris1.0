

class Problem:
    __id: str
    __name: str
    __list_problem: any
    __slug: str

    def __init__(self, id, name, list_problem, slug):
        self.__id = id
        self.__name = name
        self.__list_problem = list_problem
        self.__slug = slug

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_list_problem(self):
        return self.__list_problem
    
    def get_slug(self):
        return self.__slug
        