# coding: utf-8

# 資料排序-正序


def main():
    aList = [77,5,5,22,13,55,97,4,796,1,0,9]
    print(sort(aList))


def sort(array):
    """正序排列
    """
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] <= array[j]:
                tmp = array[i]
                array[i] = array[j]
                array[j] = tmp
    return array


if __name__ == "__main__":
    main()