import pandas as pd


class Pipeline():

    def __init__(self):
        self.producers = {}
        self.consumers = {}
        self.data = pd.DataFrame()
        pass

    def process(self):
        pass

    def attach_consumer(self, name, consumer):
        self.consumers[name] = consumer

    def attach_producer(self, name, consumer):
        self.producers[name] = consumer

    def unattach_consumer(self, name):
        self.consumers.pop(name)

    def unattach_producer(self, name):
        self.consumers.pop(name)

    def accept_data(self, data):
        self.data = data

    def publish_data(self):
        map(lambda x: x.accept_data(self.data), [consumer for consumer in self.consumers.values()])
