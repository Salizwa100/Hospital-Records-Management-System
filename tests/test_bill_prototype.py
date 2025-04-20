import unittest
from prototype.bill_prototype import BillPrototype

class MockBill:
    def __init__(self, bill_id, amount):
        self.bill_id = bill_id
        self.amount = amount

class TestBillPrototype(unittest.TestCase):
    def test_clone_bill(self):
        original = MockBill("B001", 100.0)
        prototype = BillPrototype(original)
        clone = prototype.clone()
        self.assertEqual(clone.bill_id, "B001")
        self.assertEqual(clone.amount, 100.0)
        self.assertIsNot(clone, original)

if __name__ == "__main__":
    unittest.main()
