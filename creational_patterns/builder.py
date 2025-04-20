
class Bill:
    def __init__(self):
        self.patient_id = ""
        self.bill_items = []
        self.total = 0.0

    def show_bill(self):
        print(f"Patient: {self.patient_id}")
        print(f"Items: {self.bill_items}")
        print(f"Total: ${self.total}")

class BillBuilder:
    def __init__(self):
        self.bill = Bill()

    def set_patient(self, patient_id):
        self.bill.patient_id = patient_id
        return self

    def add_item(self, item, cost):
        self.bill.bill_items.append(item)
        self.bill.total += cost
        return self

    def build(self):
        return self.bill
