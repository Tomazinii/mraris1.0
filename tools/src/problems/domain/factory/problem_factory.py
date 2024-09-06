

from src.problems.domain.entity.problem import Problem, PropsProblemType
from src.problems.domain.value_object.list import ListProblem
from src.problems.domain.value_object.slug import Slug


class ProblemFactory:
    @staticmethod
    def create(id, list_name, created_at, updated_at, comentary, slug: Slug, list_problem: ListProblem) -> Problem:
        props = PropsProblemType(comentary=comentary, id=id, list_name=list_name, created_at=created_at,updated_at=updated_at)
        problem = Problem(props=props)
        problem.set_slug(slug=slug)
        problem.set_list_problem(list_problem=list_problem)
        return problem
        

        