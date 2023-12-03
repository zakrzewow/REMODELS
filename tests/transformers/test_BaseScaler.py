import numpy as np
import pandas as pd
import pytest

from remodels.transformers.BaseScaler import BaseScaler


def test_base_scaler_fit():
    scaler = BaseScaler()
    assert scaler.fit(None) is scaler


def test_base_scaler_transform_not_implemented():
    scaler = BaseScaler()
    with pytest.raises(NotImplementedError):
        scaler.transform(None)


def test_base_scaler_fit_transform_not_implemented():
    scaler = BaseScaler()
    with pytest.raises(NotImplementedError):
        scaler.fit_transform(None)


def test_base_scaler_to_dataframe():
    scaler = BaseScaler()
    original = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    transformed = np.array([[10, 20], [40, 50], [40, 50]])

    # Test _to_dataframe method
    result = scaler._to_dataframe(original, transformed)
    assert isinstance(result, pd.DataFrame)
    assert result.equals(pd.DataFrame(transformed, columns=["a", "b"]))
