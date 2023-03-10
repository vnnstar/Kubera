from enum import IntEnum


class InternalCode(IntEnum):
    SUCCESS = 0
    INVALID_PARAMS = 10
    INVALID_AUTHENTICATION = 30
    INTERNAL_SERVER_ERROR = 40
    UNAUTHORIZED = 50
    DATA_VALIDATION_ERROR = 60
    DATA_NOT_FOUND = 61
    DATA_ALREADY_EXISTS = 62
