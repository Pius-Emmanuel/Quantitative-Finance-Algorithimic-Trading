# Markowitz model (Modern Portfolio theory)
* The Markowitz model is a mathematical framework for constructing portfolios of assets that balances risk and return. It is based on the idea that investors are risk-averse, and that they can measure the risk of a portfolio by its variance (or standard deviation) and the expected return.

* The Markowitz model can be implemented in a few steps:

1. Estimate the expected return and covariance matrix of the assets in the portfolio. This can be done using historical data or other methods such as a Capital Asset Pricing Model (CAPM).

2. Choose a target return for the portfolio.

Use a optimization algorithm to find the weights of the assets in the portfolio that minimize the variance for the target return. This step is known as Mean-Variance Optimization.

The result of this optimization is a set of weights for each asset that when combined will give the optimal portfolio for the given risk-return trade-off.

It's important to note that the assumption of normally distributed returns is not always met in practice. Furthermore the historical expected return and covariance matrix are not always a good estimates of the future returns and volatilities.