from Nodes import Node
from Pipelines import Pipeline


def main():

    n1 = Node("n1")
    n2 = Node("n2")
    p1 = Pipeline("p1", [n1], [n2])

    print(n1)
    print(n2)
    print(p1)


if __name__ == "__main__":
    main()
