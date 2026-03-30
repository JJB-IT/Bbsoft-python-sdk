from __future__ import annotations

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import to_dataframe


class VehicleResource:
    """Operations on /api/CellVehicles."""

    def __init__(self, http: HttpClient):
        self._http = http

    def list(self) -> pd.DataFrame:
        """Return all registered vehicles."""
        return to_dataframe(self._http.get("/api/CellVehicles"))

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get a vehicle by its record ID."""
        return to_dataframe(self._http.get(f"/api/CellVehicles/byid/{id}"))

    def get_by_registration(self, vehicle_registration: str) -> pd.DataFrame:
        """Get a vehicle by its registration number."""
        return to_dataframe(
            self._http.get(f"/api/CellVehicles/byreg/{vehicle_registration}")
        )

    def create(
        self,
        account_number: str,
        vehicle_registration: str,
        driver: str,
        custom_barcode: bool = False,
    ) -> dict:
        """Add a new vehicle."""
        return self._http.post(
            f"/api/CellVehicles/vehicles/{account_number}/{vehicle_registration}/{driver}",
            params={"custom_barcode": str(custom_barcode).lower()},
        )

    def update(
        self,
        account_number: str,
        vehicle_registration: str,
        driver: str,
        active: bool,
        custom_barcode: bool = False,
    ) -> dict:
        """Update an existing vehicle."""
        return self._http.put(
            f"/api/CellVehicles/vehicles/{account_number}/{vehicle_registration}/{driver}/{str(active).lower()}",
            params={"custom_barcode": str(custom_barcode).lower()},
        )
