class Utils:

    def __int__(self, another_class):
        self.another_class = another_class

    def calculate_balance(self):
        return float(self.another_class.balance) * self.rate
