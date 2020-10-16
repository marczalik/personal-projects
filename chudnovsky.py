# Author: Marc Zalik
# Date: 2020-10-15
# Description: Uses the Chudnovsky algorithm to compute an estimation of pi using of arbitrary precision. Credit to
#              Nick Craig-Wood for the algorithm: https://www.craig-wood.com/nick/articles/pi-chudnovsky/

import math
from decimal import Decimal, getcontext
import sys

def handle_exit(pi):
    """
    At program exit, write current value of pi to a file in the local directory.
    :param pi: The estimated value of pi at time of program ending.
    """
    print("Writing pi to file...")
    filename = "pi.txt"
    file = open(filename, 'w')
    file.write(str(pi))
    file.close()
    sys.exit()

def chudnvosky(iterations):
    """
    Uses the Chudnovsky algorithm to quickly calculate an estimation of pi to arbitrary precision.
    :param iterations: The number of times to loop through the summation of the Chudnovsky algorithm. Also used to
                        determine the precision of the resulting estimation.
    """
    getcontext().prec = iterations + 1
    k = 0
    a_sum = Decimal(0)
    b_sum = Decimal(0)
    numerator = Decimal(0)
    denominator = Decimal(0)

    for iter in range(iterations):
        try:
            numerator = Decimal(math.factorial(6 * k) * ((-1) ** k))
            denominator = Decimal(math.factorial(3 * k) * (math.factorial(k) ** 3) * ((640320) ** (3 * k)))
            a_k = Decimal(numerator / denominator)
            b_k = a_k * k
            a_sum += a_k
            b_sum += b_k
            k += 1
        except KeyboardInterrupt:
            pi = combine(a_sum, b_sum)
            handle_exit(pi)

    pi = combine(a_sum, b_sum)
    handle_exit(pi)

def combine(a, b):
    """
    Takes the A term and B term and combines them with the constant term to return the final estimated value of pi.
    :param a: The A term according to Craig-Wood version of Chudnovsky.
    :param b: The B term according to Craig-Wood version of Chudnovsky.
    :return: The final estimation of pi.
    """
    sum = Decimal(0)
    constant = Decimal(426880 * Decimal(10005).sqrt())
    sum = (13591409 * a) + (545140134 * b)
    pi = constant / sum
    return pi

if __name__ == "__main__":
    chudnvosky(20000)
