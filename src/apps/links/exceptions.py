from dataclasses import dataclass

from utils.exeptions import BaseApiException


@dataclass
class StringIsNotAnUrl(BaseApiException):
    message = 'string is not an url'
    status = 422
