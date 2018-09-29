from abc import ABC, abstractmethod

import pandas as pd


class Pipeline(ABC):

    def __init__(self, input=None, output=None):
        self.input = input
        self.output = output
        self.data = pd.DataFrame()
        pass

    def process(self):
        pass

    @abstractmethod
    def accept_data(self, data):
        pass

    @abstractmethod
    def publish_data(self):
        pass


class PassThroughPipeline(Pipeline):

    def accept_data(self, data):
        self.data = data;

    def publish_data(self):
        self.output.accept_data(self.data)
