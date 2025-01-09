class NotFoundException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class IntegrityException(Exception):
    def __init__(self, detail: str):
        self.detail = detail


class UnknownException(Exception):
    def __init__(self, detail: str):
        self.detail = detail
