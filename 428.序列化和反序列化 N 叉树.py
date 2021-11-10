class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        from collections import deque
        if not root: return ""
        queue = deque([root])
        res = []
        while queue:
            node = queue.pop()
            res.append(str(node.val))
            res.append(str(len(node.children)))
            for ch in node.children:
                queue.appendleft(ch)
        return ",".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """