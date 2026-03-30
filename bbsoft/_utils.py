from datetime import date, datetime

import pandas as pd


def format_date(value: str | date | datetime) -> str:
    """Convert a date value to the API's expected format: yyyy-MM-dd HH:mm:ss."""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d 00:00:00")
    return value


def to_dataframe(data: list | dict) -> pd.DataFrame:
    """Convert an API response to a pandas DataFrame."""
    if isinstance(data, dict):
        data = [data]
    if not data:
        return pd.DataFrame()
    return pd.DataFrame(data)
