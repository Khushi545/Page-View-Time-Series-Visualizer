from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
import unittest

draw_line_plot()
draw_bar_plot()
draw_box_plot()

# Run tests
loader = unittest.TestLoader()
suite = loader.loadTestsFromName('test_module')
unittest.TextTestRunner().run(suite)