class Solution:
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites: return True
        inDegree = [0] * numCourses  # 入度数组(列表，保存所有课程的依赖课程总数)
        ls = {}  # 关系表(字典，保存所有课程与依赖课程的关系)
        for pq in prerequisites:
            inDegree[pq[0]] += 1  # 保存课程初始入度值
            if not ls.__contains__(pq[1]):  # 当前课不存在于邻接表
                ls[pq[1]] = []
                ls[pq[1]] += [pq[0]]  # 添加依赖它的后续课程
            else:  # 当前课已经存在于邻接表
                ls[pq[1]] += [pq[0]]
        q = []
        for i in range(numCourses):
            if inDegree[i] == 0:  # 入度为0的课程入列
                q.append(i)
        while q:  # 队列只存储入度为0的课程，也就是可以直接选修的课程
            cur = q.pop(0)
            numCourses -= 1
            relation_list = ls[cur] if ls.__contains__(cur) else []
            if relation_list:  # 如果有依赖此课程的后续课程则更新入度
                for i in relation_list:
                    inDegree[i] -= 1  # 依赖它的后续课的入度-1
                    if inDegree[i] == 0:  # 后续课程除去当前课程无其他依赖课程则丢入队列
                        q.append(i)
        return numCourses == 0


obj = Solution()
print(obj.canFinish(2, [[0, 1]]))
