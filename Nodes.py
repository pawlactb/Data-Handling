import pandas as pd


class Node(object):

    def __init__(self, name="Unnamed Node", upstream=None):
        """
        Initialize the Node.
        :param str name: Node Name (should be unique).
        :param list upstream: Upstream nodes.
        """

        self.data = pd.DataFrame()
        self.name = name
        self.upstream = dict()
        self.downstream = dict()

        if upstream is not None:
            for up in upstream:
                self.attach_upstream([up])

    def __repr__(self):
        """
        Provide print representation of the Pipeline.
        :return: str representation of the Node.
        """

        upstream = self.upstream.keys()
        downstream = self.downstream.keys()
        return "Node: " + self.name + " with inputs: " + " ,".join(upstream) + ", and outputs: " + " ,".join(downstream)

    def attach_upstream(self, upstream):
        """
        Attach one or more upstream nodes.
        :param list upstream: list of upstream Nodes.
        :return: None
        """

        for up in upstream:
            self.upstream[up.name] = up
            up.attach_downstream([self])

    def attach_downstream(self, downstream):
        """
        Attach downstream node(s).
        :param list downstream: downstream nodes.
        :return: None
        """

        for down in downstream:
            self.downstream[down.name] = down

    def receive_data(self, data):
        """
        Receive data from upstream.
        :param Pandas.Dataframe data: The data to receive.
        :return: None
        """

        self.data = pd.DataFrame.copy(data)

    def process_data(self):
        """
        Process contained data.
        :return: None
        """

        pass
