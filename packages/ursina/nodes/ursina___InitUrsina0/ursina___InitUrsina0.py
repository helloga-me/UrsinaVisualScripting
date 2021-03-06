from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------

from ursina import *

class InitUrsina_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(InitUrsina_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if input_called == 0:
            scene.clear()
            scene.reflection_map = "reflection_map_3"
            app = Ursina()
            print("Working !!!")
            var_handler = self.get_vars_handler()
            var_handler.create_new_var("app")
            var_handler.set_var("app",app)
            self.exec_output(0)
        pass  # ...

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
