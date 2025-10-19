"""
URL: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/
"""

import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # Count orders per customer, take the top 1, and format as required
    top_customer = (
        orders.groupby("customer_number", as_index=False)
        .size()
        .sort_values("size", ascending=False)
        .head(1)[["customer_number"]]
    )
    return top_customer
