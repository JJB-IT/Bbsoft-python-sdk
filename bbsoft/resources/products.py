from __future__ import annotations

from datetime import date, datetime

import pandas as pd

from bbsoft._http import HttpClient
from bbsoft._utils import format_date, to_dataframe
from bbsoft.enums import MIF, ProductType


class ProductResource:
    """Operations on /api/Product."""

    def __init__(self, http: HttpClient):
        self._http = http

    def list(self) -> pd.DataFrame:
        """Return all products."""
        return to_dataframe(self._http.get("/api/Product"))

    def get_by_id(self, id: int) -> pd.DataFrame:
        """Get a product by its record ID."""
        return to_dataframe(self._http.get(f"/api/Product/byid/{id}"))

    def get_by_product_code(self, product_code: str) -> pd.DataFrame:
        """Get a product by its product code."""
        return to_dataframe(
            self._http.get(f"/api/Product/byproductcode/{product_code}")
        )

    def create(
        self,
        product_code: str,
        product_barcode: str,
        product_description: str,
        product_price: float,
        type: ProductType,
        mif: MIF,
    ) -> dict:
        """Add a new product."""
        return self._http.post(
            f"/api/Product/productinsert/{product_code}/{product_barcode}/"
            f"{product_description}/{product_price}",
            params={"type": type.value, "mif": mif.value},
        )

    def update(
        self,
        product_code: str,
        product_barcode: str,
        product_description: str,
        product_price: float,
        active: bool,
        type: ProductType,
        mif: MIF,
    ) -> dict:
        """Update an existing product."""
        return self._http.put(
            f"/api/Product/productupdate/{product_code}/{product_barcode}/"
            f"{product_description}/{product_price}/{str(active).lower()}",
            params={"type": type.value, "mif": mif.value},
        )

    def update_price(
        self,
        product_code: str,
        new_price: float,
        update_date: str | date | datetime,
    ) -> dict:
        """Update a product's price."""
        dt = format_date(update_date)
        return self._http.put(
            f"/api/Product/productpriceupdate/{product_code}/{new_price}/{dt}"
        )
