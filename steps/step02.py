import numpy as np


class Variable:
    def __init__(self, data):
        self.data = data


class Function:
    def __call__(self, input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output


x = Variable(np.array(10))
f = Function()
y = f(x)
print(x)
print(type(y))
print(y.data)
