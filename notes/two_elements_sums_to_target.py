# coding: utf-8
''' 在列表 nums 中找到两个数字相加等于 target '''


def two_sum(nums, target):
    # 5383 ms
    found = False
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                found = True
                break
        if found:
            break
    if found:
        return [i, j]


def two_sum_2(nums, target):
    # 1245 ms
    for i in range(len(nums)):
        val = nums[i]
        res = target - val
        try:
            i_re = nums[i+1:].index(res) + i + 1
            return [i, i_re]
        except ValueError:
            pass


def two_sum_3(nums, target):
    # 36 ms
    indices = {v: i for i, v in enumerate(nums)}
    for i, v in enumerate(nums):
        res = target - v
        if res in indices:
            if indices[res] != i:
                return [i, indices[res]]


def two_sum_5(nums, target):
    # 性能提升已经可以忽略
    indices = {}
    for i, v in enumerate(nums):
        if target - v in indices:
            return i, indices[target - v]
        indices[v] = i
