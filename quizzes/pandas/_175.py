"""
    Question: Combine Two Tables
    Desc:   
        Write a solution to report the first name, last name, city, and state of each person in the Person table. 
        If the address of a personId is not present in the Address table, report null instead. 
        
        Return the result table in any order.
    URL: https://leetcode.com/problems/combine-two-tables/description/?lang=pythondata
    Resource: NA
"""

import pandas as pd


class Solution:

    def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

        # Perform a left join on the personId column
        result = pd.merge(person, address, on="personId", how="left")

        # Select the desired columns and return the result
        return result[["firstName", "lastName", "city", "state"]]
