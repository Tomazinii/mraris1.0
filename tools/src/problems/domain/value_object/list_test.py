

from typing import List
from tools.src.problems.domain.value_object.file import File
from tools.src.problems.domain.value_object.list import ListProblem
from io import StringIO


def test_valid_file():
        # Criar um arquivo de teste com extensão .txt
        file_content = "problem1\nproblem2\nproblem3"
        file = StringIO(file_content)
        file.name = "test.txt"

        file = File(file=file, name=file.name)
        
        # Testar se a instância é criada corretamente
        list_problem = ListProblem(file)
        assert list_problem.get_list() == ["problem1", "problem2", "problem3"]

def test_invalid_extension():
    file_content = "\n".join([f"problem{i}" for i in range(50)])
    file = StringIO(file_content)
    file.name = "test.pdf"
    file = File(file=file, name=file.name)
    try:
        list_problem = ListProblem(list=file)
    except Exception as error:
         assert str(error) == "Requires .txt or .arg file; other type not is supported."

