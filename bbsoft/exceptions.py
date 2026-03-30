class BBSoftError(Exception):
    """Base exception for all BBSoft SDK errors."""

    def __init__(self, message: str, status_code: int | None = None):
        self.status_code = status_code
        super().__init__(message)


class AuthenticationError(BBSoftError):
    """Raised when the API key is missing or invalid."""


class NotFoundError(BBSoftError):
    """Raised when a requested resource is not found."""


class ServerError(BBSoftError):
    """Raised when the API returns a 5xx error."""
