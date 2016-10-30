import math

def find_next_square(sq):
    tmp = math.modf(sq ** 0.5)
    if tmp[0] == 0:
        return int((tmp[1] + 1) ** 2)
    return -1
