"""
Clean examples that provide meaningful context for variable and method names.

By choosing a name like `address_state` we make the context explicit.
Also demonstrates using a helper class to encapsulate message creation.
"""

from typing import List


class MeaningfulContext:
    SLOGAN: str = "MAKE MEANINGFUL CONTEXT"

    def __init__(self) -> None:
        # make context explicit: state of an address
        self.address_state: str = ""

    class GuessStatisticsMessage:
        """
        By defining a separate class to handle the message creation,
        we provide meaningful context to the process of generating the guess statistics message.
        """

        def __init__(self) -> None:
            self.number: str = ""
            self.verb: str = ""
            self.plural_modifier: str = ""

        def make(self, candidate: str, count: int) -> str:
            self.create_plural_dependent_message_parts(count)
            return f"There {self.verb} {self.number} {candidate}{self.plural_modifier}"

        def create_plural_dependent_message_parts(self, count: int) -> None:
            if count == 0:
                self.there_are_no_letters()
            elif count == 1:
                self.there_is_one_letter()
            else:
                self.there_are_many_letters(count)

        def there_are_many_letters(self, count: int) -> None:
            self.number = str(count)
            self.verb = "are"
            self.plural_modifier = "s"

        def there_is_one_letter(self) -> None:
            self.number = "1"
            self.verb = "is"
            self.plural_modifier = ""

        def there_are_no_letters(self) -> None:
            self.number = "no"
            self.verb = "are"
            self.plural_modifier = "s"
