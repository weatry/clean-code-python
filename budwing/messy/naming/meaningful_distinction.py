from typing import List, Any


class MeaningfulDistinction:
    

    SLOGAN: str = "MAKE MEANINGFUL DISTINCTION"

    def copy_chars(self, a1: List[str], a2: List[str]) -> None:
        """
        Copy characters from `a1` to `a2`.

        Copies characters from one array to another.

        But the names a1 and a2 do not convey any meaningful distinction between the two arrays.
        You never know which is the source and which is the destination.
        We should choose names that reflect their specific roles.

        Args:
            a1: source list of characters.
            a2: destination list of characters.
        """
        for i in range(len(a1)):
            a2[i] = a1[i]

    def example(self) -> None:
        """
        data and info are the noise words that do not convey any meaningful distinction.
        We should choose names that reflect their specific roles.
        """
        d = self.get_product_data()
        self.set_product_info(d)

    def get_product_data(self) -> List[Any]:
        # ...
        return []

    def set_product_info(self, data: List[Any]) -> None:
        # ...
        return
