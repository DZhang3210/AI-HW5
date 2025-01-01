import math

def sigmoid(x):
    return 1/(1+math.exp(-x))


# val1 = sigmoid(0.14)*(1-sigmoid(0.14))
# print(val1)

val1=sigmoid(0.099836)
val2 = sigmoid(0.155)
print(val1)
print(val2)