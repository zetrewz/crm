from rest_framework import status
from rest_framework.exceptions import APIException


class UnableToCreateSprint(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Нельзя создать новый спринт до завершения текущего'


class SprintNotProvided(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Вы должны предоставить информацию и спринте'


class UnableToAddTask(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Нельзя добавить задачу в завершенный спринт'


class TaskIsFinished(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Нельзя добавить завершенную задачу'


class TaskAlreadyInProgress(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Задача уже в выполняется в другом спринте'


class InvitationAlreadyExists(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'Вы уже приглашали в команду данного юзера'


class InvitationPermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'В команду может приглашать только тимлид'
