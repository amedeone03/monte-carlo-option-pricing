"""
Tests for Black-Scholes pricing functions.
"""

from src.black_scholes import black_scholes_call, black_scholes_put


def test_black_scholes_call_known_value():
    """
    Test Black-Scholes call price against a known benchmark.
    """
    price = black_scholes_call(
        S0=100,
        K=100,
        r=0.05,
        sigma=0.20,
        T=1.0,
    )

    assert round(price, 4) == 10.4506


def test_black_scholes_put_known_value():
    """
    Test Black-Scholes put price against a known benchmark.
    """
    price = black_scholes_put(
        S0=100,
        K=100,
        r=0.05,
        sigma=0.20,
        T=1.0,
    )

    assert round(price, 4) == 5.5735