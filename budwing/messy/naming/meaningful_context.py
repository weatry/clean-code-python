"""
Messy examples showing poor contextual naming.

The name `state` is misleading because it does not convey any meaningful context about what state it represents.
It may refer to a state of a process, an order, a user, etc. We should choose a name that reflects its specific context.
"""

class MeaningfulContext:
    SLOGAN: str = "MAKE MEANINGFUL CONTEXT"

    def __init__(self) -> None:
        # state of an address (messy name)
        self.state: str = ""

    def print_guess_statistics(self, candidate: str, count: int) -> None:
        """
        The method is not easy to understand because it lacks meaningful context.

        Args:
            candidate: a character candidate.
            count: number of occurrences.
        """
        number: str
        verb: str
        plural_modifier: str
        if count == 0:
            number = "no"
            verb = "are"
            plural_modifier = "s"
        elif count == 1:
            number = "1"
            verb = "is"
            plural_modifier = ""
        else:
            number = str(count)
            verb = "are"
            plural_modifier = "s"
        guess_message = f"There {verb} {number} {candidate}{plural_modifier}"
        print(guess_message)
