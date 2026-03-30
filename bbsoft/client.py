from __future__ import annotations

import os

from bbsoft._http import HttpClient
from bbsoft.exceptions import AuthenticationError
from bbsoft.resources import (
    AccountDiscountResource,
    AccountResource,
    FuelOrderResource,
    ProductResource,
    ShiftResource,
    TransactionResource,
    VehicleResource,
)

_DEFAULT_BASE_URL = "https://api.bbsoft.co.za"


class BBSoftClient:
    """Main client for the BBSoft FMS API.

    Usage::

        from bbsoft import BBSoftClient

        client = BBSoftClient()                          # reads BBS-API-KEY from env
        client = BBSoftClient(api_key="your-key-here")   # or pass explicitly

        df = client.accounts.list()
        df = client.transactions.get_by_date("2026-01-01", "2026-01-31")
    """

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str = _DEFAULT_BASE_URL,
    ):
        resolved_key = api_key or os.environ.get("BBS-API-KEY")
        if not resolved_key:
            raise AuthenticationError(
                "No API key provided. Pass api_key= or set the BBS-API-KEY environment variable."
            )

        self._http = HttpClient(base_url, resolved_key)

        self.accounts = AccountResource(self._http)
        self.discounts = AccountDiscountResource(self._http)
        self.vehicles = VehicleResource(self._http)
        self.fuel_orders = FuelOrderResource(self._http)
        self.products = ProductResource(self._http)
        self.shifts = ShiftResource(self._http)
        self.transactions = TransactionResource(self._http)
