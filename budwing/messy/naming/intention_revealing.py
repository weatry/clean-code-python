from typing import List


class IntentionRevealing:
    """
    Messy example showing non-intention-revealing names.

    The class demonstrates poor variable naming (e.g. `d`, `theList`, `getThem`)
    and explains why more descriptive names are preferable.
    """

    SLOGAN: str = "USE INTENTION-REVEALING NAMES"

    def __init__(self) -> None:
        # d is not descriptive name. what is it?
        self.d: int = 0  # elapsed time in days

    def get_them(self, the_list: List[List[int]]) -> List[List[int]]:
        """
        Return a list of cells whose first element equals 4.
        """
        list1: List[List[int]] = []
        for x in the_list:
            if x[0] == 4:
                list1.append(x)
        return list1

    def get_sum(self, the_list: List[List[int]]) -> int:
        """
        Compute a sum over a list of order line items.
        """
        d = 0  # what is d? (total price accumulator in this context)
        for x in the_list:
            d += x[0] * x[1]
            print(d)

        return d
    