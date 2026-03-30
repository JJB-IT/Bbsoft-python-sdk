from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import format_date, to_dataframe
from bbsoft.enums import PaymentType, TransactionStatus


class TransactionResource:
    """Operations on /api/Transaction."""

    def __init__(self, http: HttpClient):
        self._http = http

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get a transaction by its record ID."""
        return to_dataframe(self._http.get(f"/api/Transaction/byid/{id}"))

    def get_by_greater_id(self, id: int) -> pd.DataFrame:
        """Get all transactions with an ID greater than the given value."""
        return to_dataframe(
            self._http.get(f"/api/Transaction/bygreaterid/{id}")
        )

    def get_by_invoice_id(self, invoice_id: int) -> pd.DataFrame:
        """Get a transaction by its invoice ID."""
        return to_dataframe(
            self._http.get(f"/api/Transaction/byinvoiceid/{invoice_id}")
        )

    def get_by_shift(self, shift_processed: int) -> pd.DataFrame:
        """Get transactions for a specific shift."""
        return to_dataframe(
            self._http.get(f"/api/Transaction/byshift/{shift_processed}")
        )

    def get_by_order_number(self, order_number: str) -> pd.DataFrame:
        """Get transactions by order number."""
        return to_dataframe(
            self._http.get(f"/api/Transaction/byOrderNumber/{order_number}")
        )

    def get_by_status(self, status: TransactionStatus) -> pd.DataFrame:
        """Get transactions filtered by status."""
        return to_dataframe(
            self._http.get("/api/Transaction/bystatus", params={"status": status.value})
        )

    def update_invoice(self, id: int, invoice_number: str) -> dict:
        """Update a transaction's invoice number."""
        return self._http.put(
            f"/api/Transaction/transactions/{id}/{invoice_number}"
        )

    def get_by_date(
        self,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get transactions within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(f"/api/Transaction/date/{start}/{end}")
        )

    def get_completed_by_date(
        self,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get completed transactions within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(f"/api/Transaction/completedbydate/{start}/{end}")
        )

    def get_by_payment_type(
        self,
        payment: PaymentType,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get transactions filtered by payment type within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(
                f"/api/Transaction/bypaymenttype/{start}/{end}",
                params={"payment": payment.value},
            )
        )

    def get_by_pump_pos(
        self,
        pump_pos: int,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get transactions by pump position within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(
                f"/api/Transaction/bypumppos/{pump_pos}/{start}/{end}"
            )
        )

    def get_by_attendant(
        self,
        attendant_name: str,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get transactions by attendant name within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(
                f"/api/Transaction/byattendantname/{attendant_name}/{start}/{end}"
            )
        )

    def get_infinity_by_id(self, id: int) -> pd.DataFrame:
        """Get an infinity transaction by its record ID."""
        return to_dataframe(
            self._http.get(f"/api/Transaction/infinitytransactionbyid/{id}")
        )

    def get_infinity_by_date(
        self,
        start_date: str | date | datetime,
        end_date: str | date | datetime,
    ) -> pd.DataFrame:
        """Get infinity transactions within a date range."""
        start = format_date(start_date)
        end = format_date(end_date)
        return to_dataframe(
            self._http.get(
                f"/api/Transaction/infinitytransactiondate/{start}/{end}"
            )
        )
