from datetime import datetime
import uuid
class Base:
    __id: str
    __created_at: datetime
    __updated_at: datetime

    def __init__(self, id, created_at, updated_at):
        self.__id = id if id is not None else str(uuid.uuid4())
        self.__created_at = created_at if created_at is not None else datetime.now()
        self.__updated_at = updated_at if updated_at is not None else datetime.now()


    def get_id(self):
        return self.__id
    
    def get_created_at(self):
        return self.__created_at
    
    def get_updated_at(self):
        return self.__updated_at

        
    