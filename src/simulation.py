"""
Simulation utilities for stock price paths.

This module contains functions to simulate stock prices using
Geometric Brownian Motion under the risk-neutral measure.
"""

from __future__ import annotations

import numpy as np


def simulate_gbm_paths(
    S0: float,
    r: float,
    sigma: float,
    T: float,
    n_steps: int,
    n_paths: int,
    seed: int | None = None,
) -> np.ndarray:
    """
    Simulate stock price paths using Geometric Brownian Motion.

    Parameters
    ----------
    S0 : float
        Initial stock price.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility of the stock.
    T : float
        Time to maturity, in years.
    n_steps : int
        Number of time steps in each path.
    n_paths : int
        Number of simulated paths.
    seed : int | None
        Random seed for reproducibility.

    Returns
    -------
    np.ndarray
        Simulated stock paths with shape (n_paths, n_steps + 1).
        The first column contains the initial price S0.
    """
    if S0 <= 0:
        raise ValueError("S0 must be positive.")
    if sigma < 0:
        raise ValueError("sigma must be non-negative.")
    if T <= 0:
        raise ValueError("T must be positive.")
    if n_steps <= 0:
        raise ValueError("n_steps must be positive.")
    if n_paths <= 0:
        raise ValueError("n_paths must be positive.")

    rng = np.random.default_rng(seed)

    dt = T / n_steps

    random_shocks = rng.standard_normal(size=(n_paths, n_steps))

    log_returns = (
        (r - 0.5 * sigma**2) * dt
        + sigma * np.sqrt(dt) * random_shocks
    )

    cumulative_log_returns = np.cumsum(log_returns, axis=1)

    paths = np.empty((n_paths, n_steps + 1))
    paths[:, 0] = S0
    paths[:, 1:] = S0 * np.exp(cumulative_log_returns)

    return paths