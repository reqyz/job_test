from dataclasses import dataclass


@dataclass
class BaseApiException(BaseException):
    message: str = 'server error'
    status = 500


@dataclass
class NotFoundException(BaseApiException):
    message: str = 'object not found'
    status: int = 404


@dataclass
class AlreadyExists(BaseApiException):
    message: str = 'already exists'
    status: int = 400


@dataclass
class CantCreateException(BaseApiException):
    message: str = 'object cannot be created'
    status: int = 400


@dataclass
class NotEnoughData(BaseApiException):
    message: str = 'not enough data'
    status: int = 400


@dataclass
class TokenError(BaseApiException):
    message: str = 'corrupted token'
    status: int = 403
