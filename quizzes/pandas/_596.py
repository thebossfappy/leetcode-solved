"""
URL: https://leetcode.com/problems/classes-with-at-least-5-students/description/
"""

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (
        courses.groupby("class", as_index=False).size().query("size >= 5")[["class"]]
    )
    return result
