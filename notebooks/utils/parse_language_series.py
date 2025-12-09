"""Utilities to parse delimiter-separated lists stored as strings in pandas Series.

This module provides helpers to transform a pandas Series of strings into
lists of string tokens split by a given separator (default ';'), trimming
whitespace and discarding empty entries.

Example:
    >>> s = pd.Series(["Java; Shell; JavaScript;", pd.NA, "Python;  Go;"])
    >>> split_delimited_series(s)
    0         [Java, Shell, JavaScript]
    1                            []
    2                         [Python, Go]
    dtype: object
"""

from __future__ import annotations

from typing import Any, List

import pandas as pd

__all__ = ["split_delimited_series", "split_semicolon_series"]


def _parse_cell(value: Any, sep: str = ";") -> List[str]:
    """Parse a single cell into a list of trimmed, non-empty tokens.

    - Treats NaN/None as an empty list.
    - Converts non-string types to str before splitting.
    - Strips whitespace from each token.
    - Filters out empty tokens (e.g., from trailing or double separators).
    - Preserves token order.
    """
    if pd.isna(value):
        return []

    try:
        text = str(value)
    except Exception:
        return []

    return [tok.strip() for tok in text.split(sep) if tok.strip()]


def split_delimited_series(series: pd.Series, sep: str = ";") -> pd.Series:
    """Split each entry in a pandas Series by `sep`, returning lists of tokens.

    Each cell is converted to a list[str] by:
      - splitting on `sep`,
      - stripping whitespace from each part,
      - discarding empty parts,
      - preserving order.
    NaN/None values become empty lists.

    Parameters
    ----------
    series : pd.Series
        Input series (typically dtype 'string[python]' or 'object').
    sep : str, default ';'
        Delimiter used to split strings.

    Returns
    -------
    pd.Series
        Same index as input, dtype object, each value is List[str].

    Example
    -------
    >>> df = pd.DataFrame({
    ...     "project_languages": ["Java; CSS; JavaScript;", pd.NA, "Python;  Go;"]
    ... })
    >>> df["project_languages"] = split_delimited_series(df["project_languages"])
    >>> df["project_languages"]
    0         [Java, CSS, JavaScript]
    1                            []
    2                         [Python, Go]
    dtype: object
    """
    if not isinstance(series, pd.Series):
        raise TypeError("`series` must be a pandas Series")

    return series.apply(lambda v: _parse_cell(v, sep=sep))


# Convenience alias for legacy/semantic use
def split_semicolon_series(series: pd.Series) -> pd.Series:
    """Alias for `split_delimited_series(series, sep=';')`."""
    return split_delimited_series(series, sep=";")