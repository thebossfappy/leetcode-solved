"""
    Question: Duplicate Emails
    Desc:   
        Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

        Return the result table in any order.
    URL: https://leetcode.com/problems/duplicate-emails/description/?lang=pythondata
    Resource: NA
"""

import pandas as pd


class Solution:

    def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
        # Group by email and count the occurrences
        email_counts = person.groupby("email").size().reset_index(name="count")

        # Filter emails that appear more than once
        duplicates = email_counts[email_counts["count"] > 1]

        # Select only the email column for the result
        return duplicates[["email"]]
