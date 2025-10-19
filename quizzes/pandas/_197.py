"""
URL: https://leetcode.com/problems/rising-temperature/
"""

import pandas as pd


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Ensure chronological order
    weather = weather.sort_values("recordDate")

    prev_temp = weather["temperature"].shift(1)
    prev_date = weather["recordDate"].shift(1)

    is_yesterday = weather["recordDate"] - prev_date == pd.Timedelta(days=1)
    hotter = weather["temperature"] > prev_temp

    return weather.loc[is_yesterday & hotter, ["id"]]
