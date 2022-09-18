# exceptions.py
class AddressException(Exception):
    ...


class AddressNotFoundError(AddressException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Address Info Not Found"

