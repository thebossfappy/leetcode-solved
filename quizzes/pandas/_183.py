"""
    Question: Customers Who Never Order
    Desc:   
        Write a solution to find all customers who never order anything.

        Return the result table in any order.
    URL: https://leetcode.com/problems/customers-who-never-order/description/?lang=pythondata
    Resource: NA
"""

import pandas as pd


class Solution:

    def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
        # Filter for customers whose id is not in Orders' customerId
        no_order_customers = customers[~customers["id"].isin(orders["customerId"])]

        # Select and rename the column to 'Customers' as required by the output format
        return no_order_customers[["name"]].rename(columns={"name": "Customers"})
