# coding: utf-8

# 兩數總和


def twoSum(nums, target):
    tmp_res = []
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if target == (nums[i]+nums[j]):
                tmp_res.append(i)
                tmp_res.append(j)
                return tmp_res


if __name__ == "__main__":
    print(twoSum([2,7,11,15], 1))