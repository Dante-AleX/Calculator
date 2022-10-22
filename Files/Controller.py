import Model_Sum
import View


def button_click():
    value_a = View.get_value()
    value_b = View.get_value()
    Model_Sum.init(value_a, value_b)
    result = Model_Sum.sum()
    View.view_data(result)