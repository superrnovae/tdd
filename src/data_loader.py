import pandas as pd

# Create a DataLoader class that:
# - Loads CSV files into pandas DataFrames
# - Validates the data (checks for required columns, handles missing values)
# - Performs basic data cleaning (date parsing, type conversion)
class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Loads CSV file into a pandas DataFrame."""
        self.data = pd.read_csv(
            self.file_path,
            parse_dates=['date'],
            sep=','
            )

    def validate_data(self, required_columns):
        """Validates the data for required columns and handles missing values."""
        if not all(column in self.data.columns for column in required_columns):
            raise ValueError("Missing required columns in the data.")
        self.data.dropna(inplace=True)

    def clean_data(self):
        """Performs basic data cleaning like date parsing and type conversion."""
        for column in self.data.select_dtypes(include=['object']).columns:
            try:
                self.data[column] = pd.to_datetime(self.data[column])
            except ValueError:
                pass  # Skip columns that cannot be converted to datetime

    def filter_by_date_range(self, date_column, start_date, end_date):
        """Filters the data by a date range."""
        self.data[date_column] = pd.to_datetime(self.data[date_column])
        self.data = self.data[(self.data[date_column] >= start_date) & (self.data[date_column] <= end_date)]

    def filter_by_categories(self, column, categories):
        """Filters the data by specific categories."""
        self.data = self.data[self.data[column].isin(categories)]