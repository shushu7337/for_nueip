# coding: utf-8

# 資料處理-陣列


def main():
    aList = [0,1,2,3,4,5,6,7,8,9]
    
    count_array(aList)
    print(split_array(aList))


def count_array(array):
    """計算『奇數值總和』-『偶數值總和』
    """
    iOdd_sum = sum(array[::2])
    iEven_sum = sum(array[1::2])

    return iOdd_sum - iEven_sum


def split_array(array):
    """分割為兩陣列，分別存放『偶數值』及『奇數值』
    """
    iOdd_sum = array[::2]    # 奇數值
    iEven_sum = array[1::2]  # 偶數值

    return iOdd_sum, iEven_sum

if __name__ == "__main__":
    main()