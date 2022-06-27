# coding: utf-8

# 資料處理-字串


def main():
    sString = "人易科技:上 機 測 驗 - 演算法"
    sString = string_process1(sString)
    sString = string_process2(sString)
    string_process3(sString)


def string_process1(sString):
    """字元『:』改成全形
    """
    targetString = ":"
    iChr = ord(targetString)
    return sString.replace(":", chr(iChr+65248))


def string_process2(sString):
    """去掉中文字間的空白(保留-號兩側空白)
    """
    sString = sString.replace(" ",'').replace("-", " - ")
    return sString


def string_process3(sString):
    """印出符號:到-之間的字元
    """
    print(sString[sString.find("：")+1:sString.find("-"):])


if __name__ == "__main__":
    main()