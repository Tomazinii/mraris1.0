
from src._shared.errors.not_found import NotFoundError
from src._shared.repository.problem_repository_interface import ProblemRepositoryInterface
from src.problems.domain.entity.problem import Problem, PropsProblemType
from src.problems.domain.factory.problem_factory import ProblemFactory
from src.problems.domain.value_object.slug import Slug
from src.problems.usecase.register_list_problem_dto import InputRegisterListProblemDto
from web.repository.db.config.connection import DBConnectionHandler
from web.repository.problems.problem_model import ProblemModel
from sqlalchemy.orm.exc import NoResultFound
import json

class ProblemRepository(ProblemRepositoryInterface):

    @classmethod
    def create(self, input: Problem) -> any:
        with DBConnectionHandler() as db:
            try:
                list_problem = input.get_list_problem().get_list()
                
                problem = ProblemModel(id=input.get_id(),list_name=input.get_list_name(), comentary=input.get_comentary(), list_problem=list_problem, created_at=input.get_created_at(), updated_at=input.get_updated_at(),slug=input.get_slug().get_slug() )
                db.session.add(problem)
                db.session.commit()


            except Exception as error:
                db.session.rollback()
                raise error
                
    
    @classmethod
    def get_by_id(self, id) -> Problem:
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(ProblemModel).filter_by(id=id).first()
                props = PropsProblemType(
                    id=element.id,
                    comentary=element.comentary,
                    created_at=element.created_at,
                    list_name=element.list_name,
                    updated_at=element.updated_at,
                )
                decoded_data = element.list_problem
                # decoded_data = [bytes.fromhex(item[2:]).decode('utf-8') for item in element.list_problem if isinstance(item, bytes)]
                problem = Problem(props=props)
                problem.set_slug(Slug(element.list_name))
                problem.set_list_problem(decoded_data)
                return problem

        except Exception as error:
            db.session.rollback()
            raise error
    
    @classmethod
    def delete(self, id):
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(ProblemModel).filter_by(id=id).delete()
                db.session.commit()
                
                if element == 0:
                    raise NotFoundError("Element not found")

        except Exception as error:
            db.session.rollback()
            raise error
    
    @classmethod
    def update(self, input) -> Problem:
        pass

    @classmethod
    def get_all(self):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(ProblemModel).all()
                if data is None:
                    raise NotFoundError("Problems not exist")
                list_problem = [] 
                for element in data:
                    list_problem.append({"list_name": element.list_name, "comentary": element.comentary, "id": element.id, "created_at": element.created_at, "updated_at": element.updated_at})
                    
                return list_problem

        except Exception as error:
            db.session.rollback()
            raise error