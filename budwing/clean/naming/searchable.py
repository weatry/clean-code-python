"""
Clean examples recommending searchable, descriptive names and constants.
"""


class Searchable:
    SLOGAN: str = "USE SEARCHABLE NAMES"

    def __init__(self) -> None:
        """It's easier to search code with descriptive names."""
        self.age: int = 30
        self.birth_date: str = "1990-01-01"
        self.customer_id: str = "C123456"

    def week(self, s: str) -> None:
        print(f"Age: {self.age}, Birth Date: {self.birth_date}, Customer ID: {self.customer_id}")
        # DAYS_IN_WEEK is easier to search than 7
        DAYS_IN_WEEK = 7
        for i in range(DAYS_IN_WEEK):
            print(f"day in a week: {i}")
