import scipy
from numpy import array

n = 16
a = 0.95


def f(x):
    return scipy.stats.chi2.cdf(x, n) - 1 + a


cv = scipy.optimize.fsolve(f, array(18))

print("Critical Value: " + str(cv))
