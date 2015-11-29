"""Inventory of coconut """
class coconut():
    pass

class SouthAsian(coconut):
    name = "SouthAsian"
    weight = 3.0

class American(coconut):
    name = "American"
    weight = 3.5
    
class MiddleEastern(coconut):
    name = "MiddleEastern"
    weight = 2.5

class Inventory():
    def __init__(self):
        self.inv = []
        self.weights = set()
    def add_coconut(self, mutt):
        if isinstance(mutt(), coconut):
            if mutt.weight in self.weights:
                if mutt not in self.inv:
                    raise ValueError("Already there is a coconut type with same Weight") 
                    exit()
                else:
                    self.inv.append(mutt)
            else:
                self.inv.append(mutt)
                self.weights.add(mutt.weight)
                        
        else:
            raise TypeError("Input is not a cocount class type")

    def total_weight(self):
        if self.inv :
            total_weight = 0
            for i in self.inv:
                total_weight = total_weight + i.weight
            return total_weight

if __name__ == "__main__":
    inv_sample = Inventory()
    inv_sample.add_coconut(SouthAsian)
    inv_sample.add_coconut(SouthAsian)
    inv_sample.add_coconut(American)
    inv_sample.add_coconut(MiddleEastern)
