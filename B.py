import math

def B(q):
    if q == 0 or q == 1:
        return 0
    val = -1 * q*math.log(q, 2) - (1-q)*math.log(1-q, 2)
    return val



val1 = B(5/8) - ((5/8)*B(4/5) + (3/8)*B(1/3))
val2 = B(5/8) - ((4/8)*B(1) + (3/8)*B(1/3) + (1/8)*B(0))
print(val1)
print(val2)