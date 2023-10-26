from .baseCustomException import baseException


class missingFieldException(baseException):
    message = "missing one or more required field"
    errorCode = 400
class invalidJsonFormatException(baseException):
    message = "invalid json format"
    errorCode = 400