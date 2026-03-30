from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import format_date, to_dataframe


class ShiftResource:
    """Operations on /api/Shift."""

    def __init__(self, http: HttpClient):
        self._http = http

    def list(self) -> pd.DataFrame:
        """Return all shifts."""
        return to_dataframe(self._http.get("/api/Shift"))

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get a shift by its record ID."""
        return to_dataframe(self._http.get(f"/api/Shift/byid/{id}"))

    def get_by_date(
        self,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get shifts within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(self._http.get(f"/api/Shift/date/{start}/{end}"))

    def change(self, start_date: str | date | datetime) -> dict:
        """Create or change a shift."""
        dt = format_date(start_date)
        return self._http.post(f"/api/Shift/shiftchange/{dt}")
