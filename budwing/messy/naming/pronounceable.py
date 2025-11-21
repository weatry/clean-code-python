"""
Messy examples showing non-pronounceable/abbreviated identifiers that make discussion difficult.

This example uses abbreviated, non-pronounceable names for demo purposes.
"""

from datetime import datetime


class Pronounceable:
    SLOGAN: str = "USE PRONOUNCEABLE NAMES"

    class DtaRcrd102:
        """
        Abbreviated, non-pronounceable names make it difficult to discuss the code.
        genymdhms: generation year month day hour minute second
        modymdhms: modification year month day hour minute second
        pszqint: persistent storage zillionth quintillionth integer
        """

        def __init__(self) -> None:
            self.genymdhms: datetime = datetime.now()
            self.modymdhms: datetime = datetime.now()
            self.pszqint: str = "102"
