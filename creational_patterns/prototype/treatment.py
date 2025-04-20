import copy

class TreatmentPlan:
    def __init__(self, procedures):
        self.procedures = procedures

    def __str__(self):
        return f"TreatmentPlan({self.procedures})"

    def clone(self):
        return copy.deepcopy(self)
