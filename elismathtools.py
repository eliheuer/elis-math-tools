from math import *

def test(x,y):
    print("x = ", x)
    print("y = ", y)
    return x**y

def factors(n):
    results = set()
    for i in range(1, n + 1):
        if n % i == 0:
            results.add(i)
            results.add(int(n/i))
            results_list = list(sorted(results))
    return results_list

def checkIfSqIsEqualToItself(*args):
    print("number set = ", args)
    for arg in args:
        argSq = arg**2
        if argSq == arg:
            print(arg,"squared is equal to itself")
        else:
            print(arg,"squared is equal to", argSq)

if __name__ == "__main__":
    checkIfSqIsEqualToItself(1,2,3,4,5,6,7,8,9)

    
