from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import format_date, to_dataframe


class FuelOrderResource:
    """Operations on /api/FuelOrder."""

    def __init__(self, http: HttpClient):
        self._http = http

    def list(self) -> pd.DataFrame:
        """Return all fuel orders."""
        return to_dataframe(self._http.get("/api/FuelOrder"))

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get a fuel order by its record ID."""
        return to_dataframe(self._http.get(f"/api/FuelOrder/byid/{id}"))

    def get_by_account_number(self, account_number: str) -> pd.DataFrame:
        """Get fuel orders for a specific account."""
        return to_dataframe(
            self._http.get(f"/api/FuelOrder/byaccountnumber/{account_number}")
        )

    def get_by_order_number(self, order_number: str) -> pd.DataFrame:
        """Get a fuel order by its order number."""
        return to_dataframe(
            self._http.get(f"/api/FuelOrder/byOrdernumber/{order_number}")
        )

    def get_by_date(
        self,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get fuel orders within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(f"/api/FuelOrder/date/{start}/{end}")
        )

    def create(
        self,
        product_code: str,
        account_number: str,
        vehicle_registration: str,
        driver: str,
        order_number: str,
        order_reference: str,
        order_litres: float,
        order_expiry: str | date | datetime,
    ) -> dict:
        """Create a new fuel order."""
        expiry = format_date(order_expiry)
        return self._http.post(
            f"/api/FuelOrder/createorder/{product_code}/{account_number}/"
            f"{vehicle_registration}/{driver}/{order_number}/{order_reference}/"
            f"{order_litres}/{expiry}"
        )

    def update(
        self,
        product_code: str,
        account_number: str,
        vehicle_registration: str,
        driver: str,
        order_number: str,
        order_reference: str,
        order_litres: float,
        order_expiry: str | date | datetime,
    ) -> dict:
        """Update an existing fuel order."""
        expiry = format_date(order_expiry)
        return self._http.put(
            f"/api/FuelOrder/updateorder/{product_code}/{account_number}/"
            f"{vehicle_registration}/{driver}/{order_number}/{order_reference}/"
            f"{order_litres}/{expiry}"
        )

    def cancel(self, id: int, order_expiry: str | date | datetime) -> dict:
        """Cancel a fuel order."""
        expiry = format_date(order_expiry)
        return self._http.put(f"/api/FuelOrder/cancelorder/{id}/{expiry}")
