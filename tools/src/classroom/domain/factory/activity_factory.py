

from src.classroom.domain.entity.activity import Activity
from src.classroom.domain.entity.classroom import Classroom
from src.classroom.domain.entity.problem import Problem

class ActivityFactory:

    @staticmethod
    def create(created_at, id, updated_at, category, classroom_id, time, problem_id, list_problem, problem_name, problem_slug, availability) -> Activity:
        

        activity = Activity(
            created_at=created_at,
            id=id,
            updated_at=updated_at
        )

        problem = Problem(id=problem_id,list_problem=list_problem, name=problem_name, slug=problem_slug)

        activity.set_problem(problem=problem)
        activity.set_category(category=category)
        activity.set_classroom(classroom_id)
        activity.set_problem(problem=problem)
        activity.set_time(time)
        activity.set_availability(availability=availability)

        return activity