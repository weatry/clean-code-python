from budwing.clean.naming.intention_revealing import IntentionRevealing


def test_get_flagged_cells_v1_and_cell():
    ir = IntentionRevealing()

    # v1 uses raw int lists where index 0 is status
    game_board = [[4, 0], [0, 1], [4, 2]]
    flagged = ir.get_flagged_cells_v1(game_board)
    assert flagged == [[4, 0], [4, 2]]

    # using Cell class
    cells = [IntentionRevealing.Cell(4), IntentionRevealing.Cell(0)]
    flagged2 = ir.get_flagged_cells(cells)
    assert len(flagged2) == 1
    assert flagged2[0].is_flagged()


def test_get_total_price():
    ir = IntentionRevealing()
    items = [IntentionRevealing.OrderItem(2, 10), IntentionRevealing.OrderItem(3, 5)]
    total = ir.get_total_price(items)
    assert total == 2 * 10 + 3 * 5
