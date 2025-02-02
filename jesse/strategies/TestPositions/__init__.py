from jesse.strategies import Strategy


class TestPositions(Strategy):
    def before(self):
        if self.index == 0:
            assert self.positions[self.symbol] == self.position

    def should_long(self) -> bool:
        return False

    def should_short(self) -> bool:
        return False

    def go_long(self):
        pass

    def go_short(self):
        pass

    def should_cancel(self):
        return False
