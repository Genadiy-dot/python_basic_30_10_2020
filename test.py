import math


def f():
    summ = 0
    z = input().split()
    for i in range(len(z)):
        if z[i] == 'SOS':

            return summ, True

        z[i] = int(z[i])
        summ += z[i]

    return summ, False


print(f())

