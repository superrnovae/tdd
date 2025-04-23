import pytest
import pandas as pd
from src.analyzer import DataAnalyzer

@pytest.fixture
def sample_data():
    # Sample data for testing
    data = {
        'Category': ['A', 'B', 'A', 'B', 'C'],
        'Value': [10, 20, 30, 40, 50],
        'Date': ['2023-01-01', '2023-01-02', '2023-02-01', '2023-02-02', '2023-03-01'],
        'Customer': ['X', 'Y', 'X', 'Z', 'Y']
    }
    df = pd.DataFrame(data)
    analyzer = DataAnalyzer(df)
    return analyzer

def test_summary_statistics(sample_data):
    result = sample_data.summary_statistics('Category', 'Value')
    expected = pd.DataFrame({
        'Category': ['A', 'B', 'C'],
        'mean': [20.0, 30.0, 50.0],
        'median': [20.0, 30.0, 50.0],
        'std_dev': [14.142135623730951, 14.142135623730951, None]
    })
    pd.testing.assert_frame_equal(result, expected)

def test_time_series_analysis(sample_data):
    result = sample_data.time_series_analysis('Date', 'Value')
    expected = pd.DataFrame({
        'Date': ['2023-01', '2023-02', '2023-03'],
        'Value': [30, 70, 50]
    })
    pd.testing.assert_frame_equal(result, expected)

def test_spending_distribution(sample_data):
    result = sample_data.spending_distribution('Value', bins=3)
    expected = pd.Series([2, 2, 1], index=pd.IntervalIndex.from_tuples([(10.0, 23.333), (23.333, 36.667), (36.667, 50.0)]))
    pd.testing.assert_series_equal(result, expected)

def test_top_spending_categories(sample_data):
    result = sample_data.top_spending_categories('Category', 'Value', top_n=2)
    expected = pd.DataFrame({
        'Category': ['C', 'B'],
        'Value': [50, 60]
    })
    pd.testing.assert_frame_equal(result, expected)

def test_customer_segmentation(sample_data):
    result = sample_data.customer_segmentation('Customer', 'Value', bins=2)
    expected = pd.DataFrame({
        'Customer': ['X', 'Y', 'Z'],
        'Value': [40, 70, 40],
        'segment': ['Segment 1', 'Segment 2', 'Segment 1']
    })
    pd.testing.assert_frame_equal(result, expected)
