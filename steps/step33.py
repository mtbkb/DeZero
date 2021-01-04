if '__file__' in globals():
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
from dezero import Function
from dezero import Variable
import math
from dezero.utils import plot_dot_graph


def f(x):
    y = x ** 4 - 2 * x ** 2
    return y


x = Variable(np.array(2.0))
y = f(x)
y.backward(create_graph=True)
print(x.grad)
gx = x.grad
x.cleargrad()
gx.backward()
print(x.grad)