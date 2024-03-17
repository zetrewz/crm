from rest_framework import status
from rest_framework.exceptions import APIException


class UnableToCreateSprint(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Нельзя начать новый спринт до завершения текущего'
