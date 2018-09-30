import pandas as pd

class Pipeline():

    def __init__(self):
        """
        Initialize the Node.
        """
        self.producers = {}
        self.consumers = {}
        self.data = pd.DataFrame()
        pass

    def process(self):
        """
        Override this method to process your data.
        """
        pass

    def attach_consumer(self, name, consumer):
        """
        Inform the Node of a node to update.
        :param name: Name the node the pipeline is connecting to
        :param consumer: The consuming Node.
        :return: None
        """
        self.consumers[name] = consumer

    def attach_producer(self, name, consumer):
        """
        Inform the Node
        :param name:
        :param consumer:
        :return:
        """
        self.producers[name] = consumer

    def unattach_consumer(self, name):
        self.consumers.pop(name)

    def unattach_producer(self, name):
        self.consumers.pop(name)

    def accept_data(self, data):
        self.data = data

    def publish_data(self):
        map(lambda x: x.accept_data(self.data), [consumer for consumer in self.consumers.values()])
