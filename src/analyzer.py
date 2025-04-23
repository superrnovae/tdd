import pandas as pd

class DataAnalyzer:
    def __init__(self, dataframe):
        """
        Initialize the DataAnalyzer with a pandas DataFrame.
        """
        self.dataframe = dataframe

    def summary_statistics(self, category_column, value_column) -> pd.DataFrame:
        """
        Calculate summary statistics (mean, median, std dev) by category.
        :param category_column: Column name for categories.
        :return: DataFrame with summary statistics.
        """
        return self.dataframe.groupby(category_column).agg(
            mean=(value_column, 'mean'),
            median=(value_column, 'median'),
            std_dev=(value_column, 'std')
        ).reset_index()

    def time_series_analysis(self, date_column, value_column):
        """
        Analyze spending trends over time.
        :param date_column: Column name for dates.
        :param value_column: Column name for spending values.
        :return: DataFrame with spending trends over time.
        """
        self.dataframe[date_column] = pd.to_datetime(self.dataframe[date_column])
        return self.dataframe.groupby(self.dataframe[date_column].dt.to_period('M'))[value_column].sum().reset_index()

    def spending_distribution(self, value_column, bins=10):
        """
        Analyze spending distribution.
        :param value_column: Column name for spending values.
        :param bins: Number of bins for distribution.
        :return: Series with spending distribution counts.
        """
        return pd.cut(self.dataframe[value_column], bins=bins).value_counts()

    def top_spending_categories(self, category_column, value_column, top_n=5):
        """
        Identify the top spending categories.
        :param category_column: Column name for categories.
        :param value_column: Column name for spending values.
        :param top_n: Number of top categories to return.
        :return: DataFrame with top spending categories.
        """
        return self.dataframe.groupby(category_column)[value_column].sum().nlargest(top_n).reset_index()

    def customer_segmentation(self, customer_column, value_column, bins=4):
        """
        Segment customers by spending patterns.
        :param customer_column: Column name for customers.
        :param value_column: Column name for spending values.
        :param bins: Number of segments to create.
        :return: DataFrame with customer segments.
        """
        customer_spending = self.dataframe.groupby(customer_column)[value_column].sum()
        customer_spending['segment'] = pd.qcut(customer_spending, q=bins, labels=[f'Segment {i+1}' for i in range(bins)])
        return customer_spending.reset_index()