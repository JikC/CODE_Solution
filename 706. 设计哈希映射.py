class MyHashMap(object):

    # def __init__(self):
    #     self.s = {}
    #
    # def put(self, key, value):
    #     """
    #     :type key: int
    #     :type value: int
    #     :rtype: None
    #     """
    #     self.s[key] = value
    #
    #
    # def get(self, key):
    #     """
    #     :type key: int
    #     :rtype: int
    #     """
    #     for k in self.s.keys():
    #         if k == key: return self.s[key]
    #     return -1
    #
    #
    # def remove(self, key):
    #     """
    #     :type key: int
    #     :rtype: None
    #     """
    #     for k in self.s.keys():
    #         if k == key: del self.s[key]
    #     return -1
    def __init__(self):
        self.k = []
        self.v = []

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        for i in range(len(self.k)):
            if self.k[i] == key:
                self.v[i] = value
                return
        self.k.append(key)
        self.v.append(value)
        return

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        for i in range(len(self.k)):
            if self.k[i] == key: return self.v[i]
        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        for i in range(len(self.k)):
            if self.k[i] == key:
                if len(self.k) == 1:
                    self.k, self.v = [], []
                else:
                    self.k[i] = []
                    self.v[i] = []
                    return
        return


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
keys = ["put", "put", "get", "get", "put", "get", "remove", "get"]
values = [[1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

print(obj.put(769, 729))
print(obj.remove(769))
print(obj.put(379, 724))
print(obj.remove(415))
print(obj.put(421, 11))
print(obj.remove(507))
print(obj.get(421))
print('d')
