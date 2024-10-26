"""
    Question: Employees Earning More Than Their Managers
    Desc:   
        Write a solution to find the employees who earn more than their managers.
        Return the result table in any order.
        
    URL: https://leetcode.com/problems/combine-two-tables/description/?lang=pythondatahttps://leetcode.com/problems/employees-earning-more-than-their-managers/description/?lang=pythondata
"""

import pandas as pd


class Solution:

    def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
        # Self-join on the employee table: join employee table with itself
        merged_df = pd.merge(
            employee,
            employee,
            left_on="managerId",
            right_on="id",
            suffixes=("", "_manager"),
        )

        # Filter for employees whose salary is greater than their manager's salary
        result = merged_df[merged_df["salary"] > merged_df["salary_manager"]]

        # Select only the employee name column as per the result format
        return result[["name"]].rename(columns={"name": "Employee"})
