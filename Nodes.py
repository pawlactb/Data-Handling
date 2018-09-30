import pandas as pd


class Node(object):

    def __init__(self, name="Unnamed Node", upstream=None):
        self.data = pd.DataFrame()
        self.name = name
        self.upstream = dict()
        self.downstream = dict()

        if upstream is not None:
            for up in upstream:
                self.attach_upstream([up])

    def __repr__(self):
        upstream = self.upstream.keys()
        downstream = self.downstream.keys()
        return "Node: " + self.name + " with inputs: " + " ,".join(upstream) + ", and outputs: " + " ,".join(downstream)

    def attach_upstream(self, upstream):
        for up in upstream:
            self.upstream[up.name] = up
            up.attach_downstream([self])

    def attach_downstream(self, downstream):
        for down in downstream:
            self.downstream[down.name] = down

    def receive_data(self, data):
        self.data = pd.DataFrame.copy(data)

    def process_data(self):
        pass
