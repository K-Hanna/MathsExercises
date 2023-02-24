import random
from maths import Datas


def reDrawNumber(oldNumber, minValue, maxValue):
    if oldNumber == 0:
        newNumber = random.randint(minValue, maxValue)
        return reDrawNumber(newNumber, minValue, maxValue)
    else:
        return oldNumber


def countingOptions(n):
    return n * countingOptions(n - 1) if n > 1 else 1


def count(a, b, d):
    c = 0
    if d == '+':
        c = a + b
    if d == '-':
        c = abs(a - b)
    if d == '*':
        c = a * b
    if d == '/':
        c = int(a / b)
    return c


def drawNumbers(data):
    if data.maxValue < data.minValue:
        temp = data.maxValue
        data.maxValue = data.minValue
        data.minValue = temp
    examples = []
    while len(examples) < data.amount:
        a = random.randint(data.minValue, data.maxValue)
        b = random.randint(data.minValue, data.maxValue)
        d = random.choice(data.operations)
        if d == '-' and b > a:
            temp = b
            b = a
            a = temp
        if d == '/':
            if b == 0:
                b = reDrawNumber(b, data.minValue, data.maxValue)
            a = a * b
        c = count(a, b, d)
        if data.amount < countingOptions(data.maxValue - data.minValue) * len(data.operations):
            if not tuple((str(a) + ' ' + d + ' ' + str(b) + ' = ', c)) in examples:
                examples.append(tuple((str(a) + ' ' + d + ' ' + str(b) + ' = ', c)))
        else:
            examples.append(tuple((str(a) + ' ' + d + ' ' + str(b) + ' = ', c)))
    return examples


def check(expected, results):
    j = -1
    for i in range(len(expected)):
        if not expected[i].check:
            j += 1
            if results[j] == '':
                results[j] = -1
            expected[i].answer = int(results[j])
            if expected[i].result == int(results[j]):
                expected[i].check = True


def fillOutput(examples, outputData):
    for i in range(len(examples)):
        outputData.append(Datas.OutputData(examples[i][0], 0, examples[i][1], False))
