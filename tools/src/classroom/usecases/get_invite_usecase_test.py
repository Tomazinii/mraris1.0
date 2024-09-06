

import datetime
from unittest.mock import Mock
from src._shared.value_object.email import Email
from src.account.domain.entity.invite import InviteStudent
from src.classroom.usecases.get_invite_usecase import GetInviteUsecase


def test_get_invite_usecase():

    repository = Mock()
    invite1 = InviteStudent(
        classroom_id="classroom_id",
        id="id",
        time_expires=datetime.datetime.now(),
    )
    email = Email("a@a.com")
    invite1.set_to(email=email)
    
    invite2 = InviteStudent(
        classroom_id="classroom_id",
        id="id",
        time_expires=datetime.datetime.now(),
    )
    invite2.set_to(email=email)
    
    invites = [invite1,invite2]

    repository.get_by_classroom.return_value = invites

    usecase = GetInviteUsecase(repository=repository)

    result = usecase.execute(classroom_id="id")

    assert result[0].to == invites[0].get_to()
    assert result[0].active == invites[0].get_active()

