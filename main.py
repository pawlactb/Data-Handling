from Nodes import Node


def main():
    # start = datetime(2018, 1, 1)
    # end = datetime(2018, 9, 22)
    #
    # reader = LastReader(symbols="FB, TWTR, GOOGL, MU", start=start)
    #
    # df = reader.read()
    # print(df.values)
    # ct = bcolz.ctable(df, rootdir=r"C:\Users\pawla\PycharmProjects\DataCollecting\bcolz", auto_flush=True)
    # print(ct.head())
    n1 = Node("n1")
    n2 = Node("n2", [n1])

    print(n1)
    print(n2)

if __name__ == "__main__":
    main()
