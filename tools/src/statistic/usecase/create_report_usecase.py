

import datetime
from src._shared.usecase.usecase_interface import UsecaseInterface
from src.statistic.repository.statistic_repository_interface import ResultActivityRepositoryInterface

import csv
import os
from uuid import uuid4

class CreateReportUsecase(UsecaseInterface):

    def __init__(self, repository: ResultActivityRepositoryInterface):
        self.repository = repository

    def execute(self, classroom_id: str):
        results = self.repository.get_by_classroom(classroom_id=classroom_id)

        # Caminho do arquivo CSV
        file_path = f"../reports/reports-{datetime.datetime.now()}-{uuid4()}.csv"

        # Escrevendo os dados no arquivo CSV
        with open(file_path, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            campos = ["id", "classroom_id", "activity_id", "student_id", "student_name", "student_enrollment", "student_email", "time_mrplato", "num_attempts", "num_backs", "num_errors", "problem_id", "problem", "solution", "time_activity_expires", "activity_category"]
            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)

            # Escrevendo o cabeçalho
            escritor_csv.writeheader()

            students = [ 
            {"id": data.id, "classroom_id":data.classroom_id, "activity_id": data.activity_id, "student_id": data.student_id, "student_name":  data.student_name, "student_enrollment": data.student_enrollment, "student_email": data.student_email, "time_mrplato": data.time_mrplato, "num_attempts": data.num_attempts,"activity_category": data.activity_category , "num_backs": data.num_backs, "num_errors": data.num_errors, "problem_id": data.problem_id, "problem": data.problem, "solution": data.solution, "time_activity_expires": data.time_activity_expires}
            for data in results
            ]

            # Escrevendo os dados dos estudantes
            for student in students:
                escritor_csv.writerow(student)


            return file_path

