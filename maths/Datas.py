class InputData:
    def __init__(self, amount, minValue, maxValue, operations):
        self.amount = amount
        self.minValue = minValue
        self.maxValue = maxValue
        self.operations = operations


class OutputData:
    def __init__(self, equation, answer, result, check):
        self.equation = equation
        self.answer = answer
        self.result = result
        self.check = check
