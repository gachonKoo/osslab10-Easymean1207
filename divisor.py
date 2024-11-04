import sys
import math


def findDivisor(number=int(sys.argv[1])):
    divisor = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            # append the divisor
            divisor.append(i)
            if i != number // i:
                divisor.append(number // i)

    # sort the divisor list
    divisor.sort()

    print(*divisor)
    print()


findDivisor()