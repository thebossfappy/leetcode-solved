"""
URL: https://leetcode.com/problems/employee-bonus/description/
"""

import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(bonus, on="empId", how="left")
    result = merged[(merged["bonus"].isna()) | (merged["bonus"] < 1000)]
    return result[["name", "bonus"]]
