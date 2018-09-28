class ActaError(Exception):
    pass


class InvalidACTARequestError(ActaError):
    pass


class InvalidACTAHandlerError(ActaError):
    pass


class InvalidACTASpecParameterError(ActaError):
    pass
