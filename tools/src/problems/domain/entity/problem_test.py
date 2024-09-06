import datetime
from io import StringIO
import uuid
from tools.src.problems.domain.value_object.file import File

from tools.src.problems.domain.value_object.slug import Slug

from ..value_object import ListProblem
from unittest.mock import Mock
from .problem import Problem
from .problem import PropsProblemType

def test_create_problem_entity():
    props = PropsProblemType(id= str(uuid.uuid4()), comentary="training list",created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(),list_name="list 01")

    file_content = "problem1\nproblem2\nproblem3"
    file = StringIO(file_content)
    file.name = "test.txt"
    file = File(file=file, name=file.name)

    list_problem_input = ListProblem(list=file)
    slug = Slug(props.list_name)
    entity = Problem(props)
    
    entity.set_slug(slug)
    entity.set_list_problem(list_problem_input)

    assert entity.get_list_name() == props.list_name
    assert entity.get_slug() == slug
    assert entity.get_list_problem().get_list() == ["problem1","problem2","problem3"]
    assert entity.get_id() == props.id
    assert entity.get_comentary() == props.comentary
    assert entity.get_created_at() == props.created_at
    assert entity.get_updated_at() == props.updated_at
