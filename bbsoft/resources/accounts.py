from __future__ import annotations

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import to_dataframe


class AccountResource:
    """Operations on /api/Account."""

    def __init__(self, http: HttpClient):
        self._http = http

    def list(self) -> pd.DataFrame:
        """Return all accounts."""
        return to_dataframe(self._http.get("/api/Account"))

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get an account by its record ID."""
        return to_dataframe(self._http.get(f"/api/Account/ById/{id}"))

    def get_by_account_number(self, account_number: str) -> pd.DataFrame:
        """Get an account by account number."""
        return to_dataframe(
            self._http.get(f"/api/Account/Byaccountnumber/{account_number}")
        )

    def get_by_status(self, active: bool) -> pd.DataFrame:
        """Get accounts filtered by active/inactive status."""
        return to_dataframe(
            self._http.get(f"/api/Account/bystatus/{str(active).lower()}")
        )

    def create(
        self,
        account_number: str,
        account_name: str,
        account_balance: float,
    ) -> dict:
        """Add a new account."""
        return self._http.post(
            f"/api/Account/account/{account_number}/{account_name}/{account_balance}"
        )

    def update(
        self,
        account_number: str,
        account_name: str,
        account_balance: float,
        active: bool,
    ) -> dict:
        """Update an existing account."""
        return self._http.put(
            f"/api/Account/account/{account_number}/{account_name}/{account_balance}/{str(active).lower()}"
        )
