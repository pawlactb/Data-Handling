from Nodes import Node


class Pipeline(Node):

    def __init__(self, name="Unnamed Pipeline", inputs=None, outputs=None):
        super().__init__(name, inputs)

        self.outputs = dict()
        if outputs is not None:
            for output in outputs:
                self.outputs.update([(output.name, output)])
                output.attach_upstream([self])

    def __repr__(self):
        upstream = self.upstream.keys()
        downstream = self.outputs.keys()
        return "Pipeline: " + self.name + " connecting: " + " ,".join(upstream) + " to: " + ", ".join(downstream)

    def process_data(self):
        print(self.data.head(5))
