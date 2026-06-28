# Monte Carlo Option Pricing

This project uses Monte Carlo simulation to price financial options under a Geometric Brownian Motion model.

The first version focuses on European call and put options, comparing Monte Carlo estimates with the Black-Scholes analytical formula.

## Goals

- Simulate stock price paths using Geometric Brownian Motion
- Price European call and put options with Monte Carlo simulation
- Compute confidence intervals for the estimated prices
- Compare Monte Carlo results with Black-Scholes prices
- Study convergence as the number of simulations increases

## Project structure

```text
monte-carlo-option-pricing/
├── notebooks/
├── src/
├── outputs/
└── tests/