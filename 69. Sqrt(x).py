# 牛顿迭代法

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    # if x <= 1: return x
    # r = x
    # while r > (x / r):
    #     r = (r + x / r) // 2
    # return int(r)
    if x <= 1: return x
    left, right = 0, x
    while right >= left:
        mid = (right + left) // 2
        if x / mid < mid:
            right = mid - 1
        elif mid < x / mid:
            left = mid + 1
        else:
            return mid
    return right


if __name__ == '__main__':
    print(mySqrt(8))

