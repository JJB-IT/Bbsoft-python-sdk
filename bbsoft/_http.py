import requests

from bbsoft.exceptions import AuthenticationError, BBSoftError, NotFoundError, ServerError


class HttpClient:
    """Low-level HTTP client handling auth, requests, and error mapping."""

    def __init__(self, base_url: str, api_key: str):
        self._base_url = base_url.rstrip("/")
        self._session = requests.Session()
        self._session.headers.update({"X-API-KEY": api_key})

    def _url(self, path: str) -> str:
        return f"{self._base_url}{path}"

    def _handle_response(self, response: requests.Response):
        if response.ok:
            if not response.content:
                return None
            return response.json()

        status = response.status_code
        try:
            detail = response.text
        except Exception:
            detail = "Unknown error"

        if status == 401 or status == 403:
            raise AuthenticationError(f"Authentication failed: {detail}", status)
        if status == 404:
            raise NotFoundError(f"Resource not found: {detail}", status)
        if status >= 500:
            raise ServerError(f"Server error: {detail}", status)
        raise BBSoftError(f"Request failed ({status}): {detail}", status)

    def get(self, path: str, params: dict | None = None):
        resp = self._session.get(self._url(path), params=params)
        return self._handle_response(resp)

    def post(self, path: str, params: dict | None = None):
        resp = self._session.post(self._url(path), params=params)
        return self._handle_response(resp)

    def put(self, path: str, params: dict | None = None):
        resp = self._session.put(self._url(path), params=params)
        return self._handle_response(resp)
