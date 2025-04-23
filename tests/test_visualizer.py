import pytest
import pandas as pd
from src.visualizer import DataVisualizer

import matplotlib.pyplot as plt

@pytest.fixture
def sample_data():
    data = {
        "Category": ["Food", "Transport", "Entertainment", "Food", "Transport"],
        "Amount": [100, 50, 70, 200, 80],
        "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"]
    }
    return pd.DataFrame(data)

@pytest.fixture
def visualizer(sample_data):
    return DataVisualizer(sample_data)

def test_bar_chart(visualizer):
    fig = visualizer.bar_chart(category_column="Category", amount_column="Amount", title="Test Bar Chart")
    assert isinstance(fig, plt.Figure)

def test_line_chart(visualizer):
    fig = visualizer.line_chart(time_column="Date", value_column="Amount", title="Test Line Chart")
    assert isinstance(fig, plt.Figure)

def test_pie_chart(visualizer):
    fig = visualizer.pie_chart(category_column="Category", value_column="Amount", title="Test Pie Chart")
    assert isinstance(fig, plt.Figure)

def test_heatmap(visualizer):
    fig = visualizer.heatmap(correlation_columns=["Amount"], title="Test Heatmap")
    assert isinstance(fig, plt.Figure)

def test_bar_chart_save(visualizer, tmp_path):
    save_path = tmp_path / "bar_chart.png"
    visualizer.bar_chart(category_column="Category", amount_column="Amount", save_path=str(save_path))
    assert save_path.exists()

def test_line_chart_save(visualizer, tmp_path):
    save_path = tmp_path / "line_chart.png"
    visualizer.line_chart(time_column="Date", value_column="Amount", save_path=str(save_path))
    assert save_path.exists()

def test_pie_chart_save(visualizer, tmp_path):
    save_path = tmp_path / "pie_chart.png"
    visualizer.pie_chart(category_column="Category", value_column="Amount", save_path=str(save_path))
    assert save_path.exists()

def test_heatmap_save(visualizer, tmp_path):
    save_path = tmp_path / "heatmap.png"
    visualizer.heatmap(correlation_columns=["Amount"], save_path=str(save_path))
    assert save_path.exists()