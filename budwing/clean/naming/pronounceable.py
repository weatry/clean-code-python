"""
Clean version showing pronounceable and descriptive names.
"""

from datetime import datetime


class Pronounceable:
    SLOGAN: str = "USE PRONOUNCEABLE NAMES"

    class Customer:
        """Descriptive inner class with pronounceable field names."""

        def __init__(self) -> None:
            self.generation_timestamp: datetime = datetime.now()
            self.modification_timestamp: datetime = datetime.now()
            self.record_id: str = "102"
