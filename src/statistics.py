"""
Statistical utilities for Monte Carlo estimates.
"""

from __future__ import annotations

import numpy as np


def monte_carlo_standard_error(values: np.ndarray) -> float:
    """
    Compute the standard error of a Monte Carlo estimate.

    Parameters
    ----------
    values : np.ndarray
        Simulated values.

    Returns
    -------
    float
        Standard error of the sample mean.
    """
    if len(values) <= 1:
        raise ValueError("At least two values are required.")

    return float(np.std(values, ddof=1) / np.sqrt(len(values)))


def confidence_interval(
    estimate: float,
    standard_error: float,
    confidence_level: float = 0.95,
) -> tuple[float, float]:
    """
    Compute an approximate confidence interval for a Monte Carlo estimate.

    Currently supports the standard 95% normal approximation.

    Parameters
    ----------
    estimate : float
        Monte Carlo estimate.
    standard_error : float
        Standard error of the estimate.
    confidence_level : float
        Confidence level. Currently only 0.95 is supported.

    Returns
    -------
    tuple[float, float]
        Lower and upper bounds of the confidence interval.
    """
    if confidence_level != 0.95:
        raise NotImplementedError("Only 95% confidence intervals are currently supported.")

    z_score = 1.96
    lower = estimate - z_score * standard_error
    upper = estimate + z_score * standard_error

    return lower, upper