# Create a DataVisualizer class that takes analysis results and generates:
# - Bar charts for spending by category
# - Line charts for spending over time
# - Pie charts for spending distribution
# - Heatmaps for correlation between variables
# - Each method should support customization options (colors, titles, etc.)
# - Methods should return the figure and also have an option to save to file

import seaborn as sns
import pandas as pd
from typing import Optional, Dict

import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, analysis_results: pd.DataFrame):
        """
        Initialize the DataVisualizer with analysis results.

        :param analysis_results: A pandas DataFrame containing the analysis results.
        """
        self.analysis_results = analysis_results

    def bar_chart(self, category_column: str, amount_column: str, title: str = "Bar Chart", save_path: Optional[str] = None):
        """
        Generate a bar chart for spending by category.

        :param category_column: Column name for categories.
        :param value_column: Column name for values.
        :param title: Title of the chart.
        :param color: Bar color.
        :param save_path: File path to save the chart (optional).
        :return: The matplotlib figure.
        """
        fig, ax = plt.subplots()
        print(self.analysis_results.head())
        print(self.analysis_results.dtypes)
        self.analysis_results.groupby(category_column, as_index=False).sum().plot(
            kind='bar', color=['steelblue', 'orange', 'green'], ax=ax, x=category_column
        )
        ax.set_title(title)
        ax.set_ylabel(amount_column)
        ax.set_xlabel(category_column)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
        return fig

    def line_chart(self, time_column: str, value_column: str, title: str = "Line Chart", 
                   color: str = "green", save_path: Optional[str] = None):
        """
        Generate a line chart for spending over time.

        :param time_column: Column name for time.
        :param value_column: Column name for values.
        :param title: Title of the chart.
        :param color: Line color.
        :param save_path: File path to save the chart (optional).
        :return: The matplotlib figure.
        """
        fig, ax = plt.subplots()
        self.analysis_results.groupby(time_column)[value_column].sum().plot(
            kind='line', color=color, ax=ax
        )
        ax.set_title(title)
        ax.set_xlabel(time_column)
        ax.set_ylabel(value_column)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
        return fig

    def pie_chart(self, category_column: str, value_column: str, title: str = "Pie Chart", 
                  save_path: Optional[str] = None):
        """
        Generate a pie chart for spending distribution.

        :param category_column: Column name for categories.
        :param value_column: Column name for values.
        :param title: Title of the chart.
        :param save_path: File path to save the chart (optional).
        :return: The matplotlib figure.
        """
        fig, ax = plt.subplots()
        self.analysis_results.groupby(category_column)[value_column].sum().plot(
            kind='pie', autopct='%1.1f%%', ax=ax
        )
        ax.set_title(title)
        ax.set_ylabel("")  # Hide the y-label for better aesthetics
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
        return fig

    def heatmap(self, correlation_columns: Optional[list] = None, title: str = "Heatmap", 
                cmap: str = "coolwarm", save_path: Optional[str] = None):
        """
        Generate a heatmap for correlation between variables.

        :param correlation_columns: List of columns to include in the correlation matrix (optional).
        :param title: Title of the heatmap.
        :param cmap: Colormap for the heatmap.
        :param save_path: File path to save the heatmap (optional).
        :return: The matplotlib figure.
        """
        if correlation_columns:
            data = self.analysis_results[correlation_columns]
        else:
            data = self.analysis_results

        correlation_matrix = data.corr()

        fig, ax = plt.subplots()
        sns.heatmap(correlation_matrix, annot=True, cmap=cmap, ax=ax)
        ax.set_title(title)
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)
        return fig