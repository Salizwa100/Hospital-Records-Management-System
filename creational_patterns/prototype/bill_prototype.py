import copy

class BillPrototype:
    def __init__(self, bill):
        self.bill = bill

    def clone(self):
        return copy.deepcopy(self.bill)
