"""
Option payoff and Monte Carlo pricing functions.
"""

from __future__ import annotations

import numpy as np

from src.statistics import confidence_interval, monte_carlo_standard_error


def european_call_payoff(S_T: np.ndarray, K: float) -> np.ndarray:
    """
    Compute the payoff of a European call option.

    Payoff = max(S_T - K, 0)
    """
    if K <= 0:
        raise ValueError("K must be positive.")

    return np.maximum(S_T - K, 0.0)


def european_put_payoff(S_T: np.ndarray, K: float) -> np.ndarray:
    """
    Compute the payoff of a European put option.

    Payoff = max(K - S_T, 0)
    """
    if K <= 0:
        raise ValueError("K must be positive.")

    return np.maximum(K - S_T, 0.0)


def price_european_option_mc(
    terminal_prices: np.ndarray,
    K: float,
    r: float,
    T: float,
    option_type: str = "call",
) -> dict[str, float | tuple[float, float]]:
    """
    Price a European option using Monte Carlo simulation.

    Parameters
    ----------
    terminal_prices : np.ndarray
        Simulated final stock prices at maturity.
    K : float
        Strike price.
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity, in years.
    option_type : str
        Either "call" or "put".

    Returns
    -------
    dict
        Dictionary containing price, standard error, confidence interval,
        and average undiscounted payoff.
    """
    if T <= 0:
        raise ValueError("T must be positive.")

    if option_type == "call":
        payoffs = european_call_payoff(terminal_prices, K)
    elif option_type == "put":
        payoffs = european_put_payoff(terminal_prices, K)
    else:
        raise ValueError("option_type must be either 'call' or 'put'.")

    discount_factor = np.exp(-r * T)

    average_payoff = float(np.mean(payoffs))
    discounted_payoffs = discount_factor * payoffs

    price = float(np.mean(discounted_payoffs))
    standard_error = monte_carlo_standard_error(discounted_payoffs)
    ci = confidence_interval(price, standard_error)

    return {
        "price": price,
        "standard_error": standard_error,
        "confidence_interval": ci,
        "average_payoff": average_payoff,
    }