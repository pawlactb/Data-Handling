from Nodes import Node


class Pipeline(Node):

    def __init__(self, name="Unnamed Pipeline", upstream=None, downstream=None):
        """
        Initialize the Pipeline.
        :param name: Pipeline Name (should be unique).
        :param upstream: Upstream node(s).
        :param downstream: Downstream node(s).
        """
        super().__init__(name, upstream)

        self.outputs = dict()
        if downstream is not None:
            for output in downstream:
                self.outputs.update([(output.name, output)])
                output.attach_upstream([self])

    def __repr__(self):
        """
        Provide print representation of the Pipeline.
        :return: String representation of the Pipeline.
        """
        upstream = self.upstream.keys()
        downstream = self.outputs.keys()
        return "Pipeline: " + self.name + " connecting: " + " ,".join(upstream) + " to: " + ", ".join(downstream)
