
from src._shared.errors.bad_request import BadRequestError
from src.statistic.domain.entity.result_activity import ResultActivity
from src.statistic.repository.statistic_repository_interface import ResultActivityRepositoryInterface
from web.repository.db.config.connection import DBConnectionHandler

from web.repository.statistic.result_activity_model import ResultActivityModel

class ResultActivityRepository(ResultActivityRepositoryInterface):

    @classmethod
    def create(self, input: ResultActivity) -> any:
        with DBConnectionHandler() as db:

            try:
                result_model = ResultActivityModel(
                    id = input.get_id(),
                    activity_category= input.get_activity().get_category(),
                    student_id = input.get_student().get_id(),
                    classroom_id = input.get_classroom_id(),
                    activity_id = input.get_activity().get_id(),
                    student_name = input.get_student().get_name(),
                    student_enrollment= input.get_student().get_enrollment(),
                    student_email= input.get_student().get_email(),
                    time_mrplato = input.get_mrplato_metrics().get_time(),
                    num_attempts= input.get_mrplato_metrics().get_num_attempts(),
                    num_backs= input.get_mrplato_metrics().get_num_backs(),
                    num_errors= input.get_mrplato_metrics().get_errors(),
                    problem_id= input.get_activity().get_problem_id(),
                    problem= input.get_activity().get_problem(),
                    solution= input.get_activity().get_solution(),
                    time_activity_expires = input.get_activity().get_time(),
                )                
                
                db.session.add(result_model)
                db.session.commit()


            except Exception as error:
                db.session.rollback()
                raise error
                


    @classmethod
    def verify(self, user_id, activity_id, problem_id):
        with DBConnectionHandler() as db:
            verify = db.session.query(ResultActivityModel).filter_by(student_id=user_id, activity_id=activity_id, problem_id=problem_id).first() is None
            return verify
        

    
    @classmethod
    def get_solved_activity(self, activity_id, user_id):
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(ResultActivityModel).filter_by(student_id=user_id, activity_id=activity_id).all()
                if element.__len__() == 0:
                    raise BadRequestError("Could not find activity")
           
                return element

        except Exception as error:
            db.session.rollback()
            raise error

    @classmethod
    def get_by_classroom(self, classroom_id):
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(ResultActivityModel).filter_by(classroom_id=classroom_id).all()
                if element is None:
                    raise BadRequestError("Could not find activity")
           
                return element

        except Exception as error:
            db.session.rollback()
            raise error