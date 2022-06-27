# coding: utf-8

# 邏輯處理-交集、差集、聯集


def main():
    aListA = [77,5,5,22,13,55,97,4,796,1,0,9]
    aListB = [0,1,2,3,4,5,6,7,8,9]

    aListC = intersection(aListA, aListB)
    aListD = difference_set(aListA, aListB)
    aListE = union_set(aListA, aListB)

    print(aListC, aListD, aListE)


def intersection(array1, array2):
    """交集
    """
    result = []
    for i in array1:
        if i in array2 and i not in result:
            result.append(i)
    return result


def difference_set(array1, array2):
    """差集
    """
    result = []
    for i in array1:
        if i not in array2 and i not in result:
            result.append(i)    
    return result


def union_set(array1, array2):
    """聯集
    """
    result = []
    for i in array1:
        if i not in result:
            result.append(i)
    for j in array2:
        if j not in result:
            result.append(j)
    return result


if __name__ == "__main__":
    main()