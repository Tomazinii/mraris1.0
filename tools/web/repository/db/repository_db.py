from web.repository.db.config.connection import DBConnectionHandler
from web.repository.db.database import Article


class ArticleRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Article).all()
            return data
        
    def insert(self, id, title):
        with DBConnectionHandler() as db:
            try:
                data_isert = Article(id=id, name=title)
                db.session.add(data_isert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception