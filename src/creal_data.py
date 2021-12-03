import pandas as pd

PATH_DATA = "data/raw/strength_league_39_2020.csv"
data = pd.read_csv(PATH_DATA)


def main():
    print(data)


if __name__ == "__main__":
    main()
