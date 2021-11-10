def quickSort(arr, left=None, right=None):
    if left is None: left = 0
    if right is None: right = len(arr) - 1
    if left < right:
        partitionIdx = partition(arr, left, right)
        quickSort(arr, left, partitionIdx - 1)
        quickSort(arr, partitionIdx + 1, right)
    return arr


def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        i += 1
    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
    return index - 1


def quickSort1(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        great = [i for i in nums[1:] if i > pivot]
        return quickSort1(less) + [pivot] + quickSort1(great)


print(quickSort1([3, 1, 6, 5, 7, 2, 2, 4]))
