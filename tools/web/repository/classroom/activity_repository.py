from datetime import datetime
from typing import List
from src._shared.errors.not_found import NotFoundError
from src.classroom.domain.entity.activity import Activity
from src.classroom.domain.factory.activity_factory import ActivityFactory
from src.classroom.domain.repository.activity_repository_interface import ActivityRepositoryInterface
from web.repository.classroom.activity_models import ActivityModel
from web.repository.db.config.connection import DBConnectionHandler


class ActivityRepository(ActivityRepositoryInterface):

    @classmethod
    def create(self, input: Activity):
        with DBConnectionHandler() as db:
            try:
                activity = ActivityModel(
                    id=input.get_id(),
                    category=input.get_category(),
                    time=input.get_time(),
                    availability=input.get_availability(),
                    created_at=input.get_created_at(),
                    updated_at=input.get_updated_at(),
                    list_problem=input.get_problem().get_list_problem(),
                    problem_id=input.get_problem().get_id(),
                    problem_name=input.get_problem().get_name(),
                    problem_slug=input.get_problem().get_slug(),
                    classroom_id=input.get_classroom(),
                )

                db.session.add(activity)
                db.session.commit()

            except Exception as error:
                db.session.rollback()
                raise error

    @classmethod
    def delete(self, id):
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(ActivityModel).filter_by(id=id).delete()
                
                if element == 0:
                    raise NotFoundError("Element not found")
                
                db.session.commit()
                

        except Exception as error:
            db.session.rollback()
            raise error
    
    @classmethod
    def get_by_classroom(self, classroom_id):
        try:
            with DBConnectionHandler() as db:
                element = db.session.query(ActivityModel).filter_by(classroom_id=classroom_id).order_by(ActivityModel.created_at.desc()).all()
                return element

        except Exception as error:
            db.session.rollback()
            raise error
        

    @classmethod
    def update_availabity(self, list_activity_id: List):
        with DBConnectionHandler() as db:
            try:
                for id in list_activity_id:
                    data = db.session.query(ActivityModel).filter_by(id=id).first()
                    data.availability = False
                    db.session.commit()
            
            except Exception as error:
                raise error

    @classmethod
    def update(self, input):
          with DBConnectionHandler() as db:
            try:
                data = db.session.query(ActivityModel).filter_by(id=input.activity_id).first()
                data.availability = input.availability
                data.time = input.time
                data.category = input.category
                db.session.commit()
            except Exception as error:
                raise error

    @classmethod
    def get(self, teacher_id):
        try:
            with DBConnectionHandler() as db:
              pass

                
        except Exception as error:
            db.session.rollback()
            raise error
        
    
    def get_by_id(self, id):
        try:
            with DBConnectionHandler() as db:
                data = db.session.query(ActivityModel).filter_by(id=id).first()

                if data is None:
                    raise NotFoundError("Activity not found")
                

                activity = ActivityFactory.create(
                    availability=data.availability,
                    category=data.category,
                    classroom_id=data.classroom_id,
                    created_at=data.created_at,
                    id=data.id,
                    list_problem=data.list_problem,
                    problem_id=data.problem_id,
                    problem_name=data.problem_name,
                    problem_slug=data.problem_slug,
                    time=data.time,
                    updated_at=data.updated_at,
                )

                return activity

                
        except Exception as error:
            db.session.rollback()
            raise error