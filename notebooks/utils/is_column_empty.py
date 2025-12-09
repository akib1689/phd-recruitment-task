"""Utility functions for data validation used by notebooks.

This module contains small helpers that can be shared across notebooks.
"""

import pandas as pd

__all__ = ["is_effectively_empty"]


def is_effectively_empty(series: pd.Series) -> bool:
    """Return True if a pandas Series is effectively empty.

    - For object dtype: treat strings that are empty or only whitespace as empty as well as NaNs.
    - For other dtypes: return True only if all values are NaN.
    """
    if series.dtype == 'object':
        # preserve None/NaN handling but also treat whitespace-only strings as empty
        stripped = series.astype(str).str.strip()
        # If original all nulls (NaN/None), then `.astype(str)` makes them 'nan' which is not desired.
        # Use the original isnull check combined with string emptiness.
        is_null = series.isnull()
        # For non-null values, check if trimmed string is empty
        trimmed_empty = (~is_null) & (stripped == '')
        return (is_null | trimmed_empty).all()
    else:
        return series.isnull().all()
