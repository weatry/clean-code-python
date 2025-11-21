from typing import List, Any


class MeaningfulDistinction:
    """
    By using names like source and destination, we make a meaningful distinction
    between the two arrays. The user of the method will never be confused about
    which array is the source and which is the destination.
    """

    SLOGAN: str = "MAKE MEANINGFUL DISTINCTION"

    def copy_chars(self, source: List[str], destination: List[str]) -> None:
        """
        Copy characters from source array to destination array.

        Args:
            source: list of characters to copy from.
            destination: list where characters will be copied to.
        """
        for i in range(len(source)):
            destination[i] = source[i]

    def example(self) -> None:
        """
        Either using same name if productData and productInfo represent the same concept,
        or using distinct names that reflect their specific roles.
        """
        d = self.get_product()
        self.set_product(d)

    def get_product(self) -> List[Any]:
        # ...
        return []

    def set_product(self, data: List[Any]) -> None:
        # ...
        return
