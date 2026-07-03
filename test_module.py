import unittest
import pandas as pd
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        from time_series_visualizer import df
        self.assertEqual(df.shape[0], 1238)

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        self.assertEqual(self.ax.get_title(), 
            "Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    def test_line_plot_xlabel(self):
        self.assertEqual(self.ax.get_xlabel(), "Date")

    def test_line_plot_ylabel(self):
        self.assertEqual(self.ax.get_ylabel(), "Page Views")

class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_xlabel(self):
        self.assertEqual(self.ax.get_xlabel(), "Years")

    def test_bar_plot_ylabel(self):
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views")

class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = draw_box_plot()
        self.ax1, self.ax2 = self.fig.axes

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)")

if __name__ == "__main__":
    unittest.main()