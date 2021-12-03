import pandas as pd

PATH_DATA = "data/raw/strength_league_39_2020.csv"
data = pd.read_csv(PATH_DATA)
OUTPUT_PATH = "data/processed/strength_and_goals_39_2020.csv"


def remove_columns(data):
    df = data.drop(columns=["home_id", "away_id", "home", "away", "won", "total_goals"])
    return df


def add_total_goals(data):
    df = data.assign(total_goals=data.home + data.away)
    return df


def change_to_bool(data):
    df = data.assign(
        are_more_goal=lambda dataframe: dataframe["total_goals"].map(
            lambda total_goals: True if total_goals >= 3 else False
        )
    )
    return df


def main():
    cleaned_data = add_total_goals(data)
    cleaned_data = change_to_bool(cleaned_data)
    cleaned_data = remove_columns(cleaned_data)
    cleaned_data.to_csv(OUTPUT_PATH)


if __name__ == "__main__":
    main()
