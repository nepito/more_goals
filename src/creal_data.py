import pandas as pd

PATH_DATA = "data/raw/strength_league_39_2020.csv"
data = pd.read_csv(PATH_DATA)
OUTPUT_PATH = "data/processed/strength_and_goals_39_2020.csv"


def remove_columns(data):
    df = data.drop(columns=["home_id", "away_id", "home", "away", "won"])
    return df


def add_total_goals(data):
    df = data.assign(total_goal=data.home + data.away)
    return df


def main():
    cleaned_data = add_total_goals(data)
    cleaned_data = remove_columns(cleaned_data)
    cleaned_data.to_csv(OUTPUT_PATH)


if __name__ == "__main__":
    main()
