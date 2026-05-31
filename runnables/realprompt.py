from runnableabstract import Runnable
class RealPrompt(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables


    def invoke(self, input_dict):
       return self.template.format(**input_dict)