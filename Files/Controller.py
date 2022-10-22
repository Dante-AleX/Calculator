import Model_Sum as model
import View


def button_click():
    value_a = View.get_value()
    value_b = View.get_value()
    model.init(value_a, value_b)
    result = model.do_it()
    View.view_data(result)