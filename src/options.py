"""
Option payoff and Monte Carlo pricing functions.
"""

from __future__ import annotations

import numpy as np


def european_call_payoff(S_T: np.ndarray, K: float) -> np.ndarray:
    """
    Compute the payoff of a European call option.

    Payoff = max(S_T - K, 0)

    Parameters
    ----------
    S_T : np.ndarray
        Final stock prices at maturity.
    K : float
        Strike price.

    Returns
    -------
    np.ndarray
        Payoff for each simulated final stock price.
    """
    if K <= 0:
        raise ValueError("K must be positive.")

    return np.maximum(S_T - K, 0.0)


def european_put_payoff(S_T: np.ndarray, K: float) -> np.ndarray:
    """
    Compute the payoff of a European put option.

    Payoff = max(K - S_T, 0)

    Parameters
    ----------
    S_T : np.ndarray
        Final stock prices at maturity.
    K : float
        Strike price.

    Returns
    -------
    np.ndarray
        Payoff for each simulated final stock price.
    """
    if K <= 0:
        raise ValueError("K must be positive.")

    return np.maximum(K - S_T, 0.0)