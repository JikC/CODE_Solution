def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    # ss = s.split(' ')
    # res = []
    # i = len(ss) - 1
    # while i >= 0:
    #     if ss[i] != '':
    #         res.append(ss[i])
    #     i -= 1
    # return ' '.join(res)
    ss = s.split()
    a = reversed(s.split())
    return " ".join(a)


if __name__ == '__main__':
    strs = "    the sky  is    blue"
    print(reverseWords(strs))
