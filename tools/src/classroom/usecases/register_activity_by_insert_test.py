

from datetime import  datetime
from unittest.mock import Mock
from src.classroom.usecases.register_activity_by_insert import RegisterActivityByInsertUsecase
from src.classroom.usecases.register_activity_by_insert_dto import InputRegisterActivityByInsertUsecaseDto

class ListProblem:
    def __init__(self, list_problem) -> None:
        self.list_problem = list_problem

def test_register_activity_by_insert_usecase():

    repository = Mock()
    problem_facade = Mock()
    usecase = RegisterActivityByInsertUsecase(problem_facade=problem_facade, repository=repository)
    
    repository.create.return_value = None
    
    lista= [b'0 - p  \xe2\x86\x92 q , p \xe2\x8a\xa2 (q v p)', b'1 - p \xe2\x86\x92 q , ~q \xe2\x8a\xa2 ~p', b'2 - p \xe2\x86\x92 q , q \xe2\x86\x92 s \xe2\x8a\xa2 p \xe2\x86\x92 s', b'3 - ~~p \xe2\x86\x92 q \xe2\x8a\xa2 p -> q', b'4 - p \xe2\x86\x92 ~~q \xe2\x8a\xa2 p -> q', b'5 - p \xe2\x86\x92 ~(p ^ r)  \xe2\x8a\xa2 p \xe2\x86\x92  (~p v ~r)', b'6 - ~~p \xe2\x8a\xa2 p', b'7 - ~p \xe2\x8a\xa2 ~~~p', b'8 - ~~p \xe2\x86\x92 q \xe2\x8a\xa2 p -> q', b'9 - p \xe2\x86\x92 ~~q \xe2\x8a\xa2 p -> q', b'10 - p \xe2\x86\x92 ~(p ^ r)  \xe2\x8a\xa2 p \xe2\x86\x92  (~p v ~r)', b'11 - ~~p \xe2\x8a\xa2 p', b'12 - ~p \xe2\x8a\xa2 ~~~p', b'13 - \xe2\x88\xbcp(a) \xe2\x8a\xa2 \xe2\x88\xbc\xe2\x88\x80xp(x)', b'14 - \xe2\x88\x83x\xe2\x88\x80y(p(x,y) v q(x,y)) \xe2\x8a\xa2 p(a,a) v q(a,a)', b'15 - \xe2\x88\x80x(p(x) \xe2\x86\x92 q(x)) , \xe2\x88\x80x(q(x) \xe2\x86\x92 r(x)) \xe2\x8a\xa2 \xe2\x88\x80x(p(x) \xe2\x86\x92 r(x))', b'16 -  \xe2\x88\x80x(p(x) \xe2\x88\xa7 q(x)) \xe2\x8a\xa2 \xe2\x88\x80xp(x) \xe2\x88\xa7 \xe2\x88\x80xq(x)', b'17 - ~\xe2\x88\x80xp(x)  \xe2\x8a\xa2  \xe2\x88\x83x~p(x)', b'18 - ~\xe2\x88\x83xp(x)  \xe2\x8a\xa2  \xe2\x88\x80x~p(x)', b'19 - \xe2\x88\x80xp(x)  \xe2\x8a\xa2 \xe2\x88\x80xp(x)', b'20 - ~~p \xe2\x8a\xa2 CNF', b'21 - p \xe2\x8a\xa2 DNF', b'22 - p \xe2\x8a\xa2 CNF', b'23 - ~p \xe2\x8a\xa2 CNF']
    list_problem = ListProblem(lista)
    problem_facade.register_problem.return_value = list_problem
    dto = InputRegisterActivityByInsertUsecaseDto(
        availability=True,
        category="category",
        classroom_id="classroom_id",
        created_at=datetime.now(),
        id="asdd",
        problem_comentary="adsaads",
        problem_created_at=datetime.now(),
        problem_id="dwsqw",
        updated_at=datetime.now(),
        problem_list_name="qdwqdw",
        problem_list_problem=[],
        problem_updated_at=datetime.now(),
        time=datetime.now()
    )
    result = usecase.execute(input=dto)

    assert result is None