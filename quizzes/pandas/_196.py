"""
URL: https://leetcode.com/problems/delete-duplicate-emails/
"""

import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Make the smallest id for each email come first, then drop dups
    person.sort_values(["email", "id"], inplace=True)
    person.drop_duplicates(subset=["email"], keep="first", inplace=True)
