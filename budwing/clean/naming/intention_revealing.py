from typing import List


class IntentionRevealing:

    SLOGAN: str = "USE INTENTION-REVEALING NAMES"

    FLAGGED: int = 4
    STATUS_VALUE: int = 0

    def __init__(self) -> None:
        """
        By using intention-revealing names, we can rename the variable d to elapsedTimeInDays.
        It clearly indicates what is being measured and the unit of that measurement. We can remove
        the commented-out alternative names since they are no longer needed.
        """
        self.elapsedTimeInDays: int = 0

    def get_flagged_cells_v1(self, game_board: List[List[int]]) -> List[List[int]]:
        """
        By renaming the method to getFlaggedCells, the parameter to gameBoard, and the variable to flaggedCells,
        we make the code more intention-revealing. It becomes clear that the method retrieves flagged cells from a game board.
        
        But it's still obscure what "cell[0]" means. We can further improve the code by introducing a Cell class
        with a method isFlagged(). This way, we encapsulate the cell's status within the Cell class, making the code even more intention-revealing.
        """
        flagged_cells: List[List[int]] = []
        for cell in game_board:
            if cell[self.STATUS_VALUE] == self.FLAGGED:
                flagged_cells.append(cell)
        return flagged_cells

    class Cell:
        """
        Cell is the smallest unit of the mine sweeper game board.
        The status of a cell is encapsulated within the Cell class.
        By using the isFlagged() method, we make the code more intention-revealing.
        """
        status: int
        x: int
        y: int
        bomb: bool

        def __init__(self, status: int = 0) -> None:
            self.status = status

        def is_flagged(self) -> bool:
            return self.status == 4

    def get_flagged_cells(self, game_board: List['IntentionRevealing.Cell']) -> List['IntentionRevealing.Cell']:
        """
        Now, we can further improve the getFlaggedCells method by using the Cell class.
        The code is self-explanatory, and we don't need comments to understand its purpose.
        """
        flagged_cells: List[IntentionRevealing.Cell] = []
        for cell in game_board:
            if cell.is_flagged():
                flagged_cells.append(cell)
        return flagged_cells

    class OrderItem:
        """
        Exercise for intention-revealing names.
        
        By defining the OrderItem class, we make the code more intention-revealing.
        """

        def __init__(self, quantity: int, unit_price: int) -> None:
            self.quantity = quantity
            self.unit_price = unit_price

    def get_total_price(self, order_items: List['IntentionRevealing.OrderItem']) -> int:
        """
        The method name getTotalPrice clearly indicates its purpose.
        
        Can you improve it further?
        """
        total_price = 0
        for item in order_items:
            total_price += item.quantity * item.unit_price
            print(total_price)

        return total_price
