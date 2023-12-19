"""sFQRA model."""

from typing import Tuple

import numpy as np

from .fqra import FQRA


class sFQRA(FQRA):
    """A class that represents the FQRA model.

    The sFQRA model is an FQRA model where the input variables are standardized by subtracting the mean and dividing by the standard deviation (calculated across rows).
    """

    def __init__(
        self, quantile: float = None, n_factors: int = None, fit_intercept: bool = False
    ) -> None:
        """Initialize the sFQRA model.

        :param quantile: quantile
        :type quantile: float
        :param n_factors: number of factors (principal components) to use; if None, number of factors is selected automatically using  Bayesian information criterion
        :type n_factors: int
        :param fit_intercept: True if fit intercept in model, defaults to False
        :type fit_intercept: bool, optional
        """
        super().__init__(quantile, n_factors, fit_intercept)

    def fit(self, X: np.array, y: np.array):
        """Fit the model to the data.

        :param X: input matrix
        :type X: np.array
        :param y: dependent variable
        :type y: np.array
        :return: fitted model
        :rtype: sFQRA
        """
        X, mean, std = self._zscore(X)
        y = (y - mean) / std
        return super().fit(X, y)

    def predict(self, X: np.array) -> np.array:
        """Predict the dependent variable.

        :param X: input matrix
        :type X: np.array
        :return: prediction
        :rtype: np.array
        """
        X, mean, std = self._zscore(X)
        y = super().predict(X)
        return y * std + mean

    def _zscore(self, X: np.array) -> Tuple[np.array, np.array, np.array]:
        mean = np.mean(X, axis=1)
        std = np.std(X, axis=1)
        return (X - mean[:, np.newaxis]) / std[:, np.newaxis], mean, std
