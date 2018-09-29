from datetime import datetime

import bcolz
from pandas_datareader.iex.tops import LastReader


def main():
    start = datetime(2018, 1, 1)
    end = datetime(2018, 9, 22)

    reader = LastReader(symbols="FB, TWTR, GOOGL, MU", start=start)

    df = reader.read()
    print(df.values)
    ct = bcolz.ctable(df, rootdir=r"C:\Users\pawla\PycharmProjects\DataCollecting\bcolz", auto_flush=True)
    print(ct.head())


if __name__ == "__main__":
    main()
