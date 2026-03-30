from __future__ import annotations

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import to_dataframe


class AccountDiscountResource:
    """Operations on /api/AccountDiscount."""

    def __init__(self, http: HttpClient):
        self._http = http

    def list(self) -> pd.DataFrame:
        """Return all account discounts."""
        return to_dataframe(self._http.get("/api/AccountDiscount"))

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get a discount by its record ID."""
        return to_dataframe(self._http.get(f"/api/AccountDiscount/byid/{id}"))

    def get_by_account_number(self, account_number: str) -> pd.DataFrame:
        """Get discounts for a specific account."""
        return to_dataframe(
            self._http.get(f"/api/AccountDiscount/byaccountnumber/{account_number}")
        )

    def create(
        self,
        account_number: str,
        product_code: str,
        discount: float,
    ) -> dict:
        """Add a new account discount."""
        return self._http.post(
            f"/api/AccountDiscount/discount/{account_number}/{product_code}/{discount}"
        )

    def update(
        self,
        account_number: str,
        product_code: str,
        discount: float,
        active: bool,
    ) -> dict:
        """Update an existing account discount."""
        return self._http.put(
            f"/api/AccountDiscount/discount/{account_number}/{product_code}/{discount}/{str(active).lower()}"
        )
