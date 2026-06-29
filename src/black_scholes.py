"""
Black-Scholes analytical pricing formulas for European options.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm


def _validate_black_scholes_inputs(
    S0: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
) -> None:
    """
    Validate inputs for Black-Scholes formulas.
    """
    if S0 <= 0:
        raise ValueError("S0 must be positive.")
    if K <= 0:
        raise ValueError("K must be positive.")
    if sigma <= 0:
        raise ValueError("sigma must be positive.")
    if T <= 0:
        raise ValueError("T must be positive.")


def _d1(S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Compute the d1 term in the Black-Scholes formula.
    """
    return (
        np.log(S0 / K) + (r + 0.5 * sigma**2) * T
    ) / (sigma * np.sqrt(T))


def _d2(S0: float, K: float, r: float, sigma: float, T: float) -> float:
    """
    Compute the d2 term in the Black-Scholes formula.
    """
    return _d1(S0, K, r, sigma, T) - sigma * np.sqrt(T)


def black_scholes_call(
    S0: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
) -> float:
    """
    Compute the Black-Scholes price of a European call option.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    K : float
        Strike price.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.
    T : float
        Time to maturity, in years.

    Returns
    -------
    float
        Black-Scholes call option price.
    """
    _validate_black_scholes_inputs(S0, K, r, sigma, T)

    d1 = _d1(S0, K, r, sigma, T)
    d2 = _d2(S0, K, r, sigma, T)

    call_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

    return float(call_price)


def black_scholes_put(
    S0: float,
    K: float,
    r: float,
    sigma: float,
    T: float,
) -> float:
    """
    Compute the Black-Scholes price of a European put option.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    K : float
        Strike price.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.
    T : float
        Time to maturity, in years.

    Returns
    -------
    float
        Black-Scholes put option price.
    """
    _validate_black_scholes_inputs(S0, K, r, sigma, T)

    d1 = _d1(S0, K, r, sigma, T)
    d2 = _d2(S0, K, r, sigma, T)

    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)

    return float(put_price)