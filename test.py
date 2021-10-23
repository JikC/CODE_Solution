print(int(False))

def solution(N):
    # write your code in Python 3.6
    if N<10: return N
    res = 0
    for i in range(N//9):
        res = res*10 + 9

    return res + (N%9)*(10**(N//9))


def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    l = len(A)
    res = 0
    summa = sum(A)
    minNum = summa//l if summa%l==0 else summa//l+1

    for i in A:
        if i<minNum:
            res += (minNum-i)
    return res


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from extratypes import Point2D  # library with types used in the task


def Collinear(point1, point2, point3):
    return ((point2.y - point1.y) * (point3.x - point2.x)) == ((point3.y - point2.y) * (point2.x - point1.x))


def solution(A):
    # write your code in Python 3.6
    N = len(A)
    res = 0
    if N < 3: return 0
    n = 1
    for i in range(3, N + 1):
        n *= i
    if (n / 6) > 100000000: return -1
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                res += int(Collinear(A[i], A[j], A[k]))

    return res