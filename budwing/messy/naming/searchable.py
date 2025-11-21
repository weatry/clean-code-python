"""
Messy examples that use non-searchable names (single letters) and magic numbers.
"""


class Searchable:
    SLOGAN: str = "USE SEARCHABLE NAMES"

    def __init__(self) -> None:
        # a: age
        # b: birth date
        # c: customer id
        self.a: int = 30
        self.b: str = "1990-01-01"
        self.c: str = "C123456"

    def week(self, s: str) -> None:
        print(f"Age: {self.a}, Birth Date: {self.b}, Customer ID: {self.c}")
        for i in range(7):  # 7 is hard to search
            print(f"day in a week: {i}")
