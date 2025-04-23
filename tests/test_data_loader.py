import pytest
import pandas as pd

from data_loader import DataLoader  # Adjust the import path as needed

@pytest.fixture
def sample_data():
    """Fixture to provide sample data for testing."""
    data = {
        "date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "category": ["A", "B", "A"],
        "value": [10, 20, 30],
    }
    return pd.DataFrame(data)

@pytest.fixture
def data_loader(sample_data):
    """Fixture to provide a DataLoader instance."""
    return DataLoader(sample_data)

def test_data_loading(data_loader, sample_data):
    """Test that data is loaded correctly."""
    assert data_loader.data.equals(sample_data)

def test_required_columns_validation():
    """Test validation of required columns."""
    invalid_data = pd.DataFrame({"date": ["2023-01-01"], "value": [10]})
    with pytest.raises(ValueError, match="Missing required columns"):
        DataLoader(invalid_data)

def test_date_filtering(data_loader):
    """Test date filtering functionality."""
    filtered_data = data_loader.filter_by_date(start_date="2023-01-02", end_date="2023-01-03")
    expected_data = pd.DataFrame({
        "date": ["2023-01-02", "2023-01-03"],
        "category": ["B", "A"],
        "value": [20, 30],
    })
    assert filtered_data.reset_index(drop=True).equals(expected_data)

def test_category_filtering(data_loader):
    """Test category filtering functionality."""
    filtered_data = data_loader.filter_by_category(categories=["A"])
    expected_data = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-03"],
        "category": ["A", "A"],
        "value": [10, 30],
    })
    assert filtered_data.reset_index(drop=True).equals(expected_data)