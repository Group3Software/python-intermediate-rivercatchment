"""Tests for statistics functions within the Model layer."""
# Import packages

import pandas as pd
import pandas.testing as pdt
import datetime
import pytest


def test_daily_std_integers():
    """Test that std function works for an array of positive integers."""
    from catchment.models import daily_std

    test_input = pd.DataFrame(
                     data=[[1, 2],
                           [3, 4],
                           [5, 6]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[2.0, 2.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_std(test_input), test_result)


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from catchment.models import daily_mean

    test_input = pd.DataFrame(
                     data=[[0.0, 0.0],
                           [0.0, 0.0],
                           [0.0, 0.0]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[0.0, 0.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from catchment.models import daily_mean

    test_input = pd.DataFrame(
                     data=[[1, 2],
                           [3, 4],
                           [5, 6]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[3.0, 4.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_mean(test_input), test_result)


def test_daily_max():
    """Test that mean function works for an array of zeros."""
    from catchment.models import daily_max

    test_input = pd.DataFrame(
                     data=[[0.0, 0.0],
                           [0.0, 0.0],
                           [0.0, 0.0]],
                     index=[pd.to_datetime('2000-01-01 01:00'),
                            pd.to_datetime('2000-01-01 02:00'),
                            pd.to_datetime('2000-01-01 03:00')],
                     columns=['A', 'B']
    )
    test_result = pd.DataFrame(
                     data=[[0.0, 0.0]],
                     index=[datetime.date(2000, 1, 1)],
                     columns=['A', 'B']
    )

    # Need to use Pandas testing functions to compare arrays
    pdt.assert_frame_equal(daily_max(test_input), test_result)


@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data, expected_index, expected_columns",
    [
        (
            [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0]],
            [pd.to_datetime('2000-01-01 01:00'),
             pd.to_datetime('2000-01-01 02:00'),
             pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B'],
            [[0.0, 0.0]],
            [datetime.date(2000, 1, 1)],
            ['A', 'B']),
        ([[1, 2], [3, 4], [5, 6]],
            [pd.to_datetime('2000-01-01 01:00'),
             pd.to_datetime('2000-01-01 02:00'),
             pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B'],
            [[3.0, 4.0]],
            [datetime.date(2000, 1, 1)],
            ['A', 'B']
         )
    ]
)
def test_daily_mean(test_data, test_index, test_columns,
                    expected_data, expected_index, expected_columns):
    """Test mean function works"""
    from catchment.models import daily_mean
    pdt.assert_frame_equal(
        daily_mean(pd.DataFrame(data=test_data, index=test_index, columns=test_columns)),
        pd.DataFrame(data=expected_data, index=expected_index, columns=expected_columns))


@pytest.mark.parametrize(
    "test_data, test_index, test_columns, expected_data, expected_index, expected_columns",
    [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B', 'C'],
            [[0.14, 0.25, 0.33], [0.57, 0.63, 0.66], [1.0, 1.0, 1.0]],
            [pd.to_datetime('2000-01-01 01:00'),
                pd.to_datetime('2000-01-01 02:00'),
                pd.to_datetime('2000-01-01 03:00')],
            ['A', 'B', 'C']
        ),
    ])
def test_normalise(test_data, test_index, test_columns, expected_data, expected_index, expected_columns):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from catchment.models import data_normalise
    pdt.assert_frame_equal(data_normalise(pd.DataFrame(data=test_data, index=test_index, columns=test_columns)),
                           pd.DataFrame(data=expected_data, index=expected_index, columns=expected_columns),
                           atol=1e-2)
