import pandas as pd


class Node(object):

    def __init__(self, name="Unnamed Node", inputs=None):
        self.data = pd.DataFrame()
        self.name = name
        self.inputs = dict()

        if inputs is not None:
            for input in inputs:
                self.inputs.update([(input.name, input)])

    def __repr__(self):
        connected_to = self.inputs.keys()
        return "Node: " + self.name + " with inputs: " + " ,".join(connected_to) + "."

    def attach_input(self, name, input):
        self.inputs[name] = input

    def attach_inputs(self, inputs):
        for name, input in inputs:
            self.inputs[name] = input

    def receive_data(self, data):
        self.data = pd.DataFrame.copy(data)

    def process_data(self):
        pass
