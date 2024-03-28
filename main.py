# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Date import Date
import numpy as np


def func(s):
    if s > 100:
        return
    else:
        return 120


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    date = Date(2023, 2, 25)
    # day1 = {1, 2, 6, 5, 7, 8}
    # day2 = {8, 5, 2, 1, 4}
    # day3 = day1 | day2
    # day3 = np.array(list(day3))
    # print(day3)
    # np.where(day3 == 5)
    # result = func(150)
    # print(result)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(matrix.shape[0])
    b1 = np.array([0, 1, 0, 0, 0, 1, 0, 0])
    b2 = np.array([1, 1, 0, 1, 1, 1, 1, 1])
    b3 = b1 | b2
    print(b3)
    # a = input()
    # b = input()
    # x = np.linspace(0, int(b) + 50, 51 + int(b))
    # strike_low = 75
    # strike_mid = 80
    # strike_high = 100
    # cap = 200
    #
    #
    # def func(s):
    #     return -max(0, strike_low - s) + max(0, strike_mid - s) - \
    #         max(0, strike_high - s) + max(0, s - strike_high) - max(0, s - cap)
    #
    #
    # result = map(func, x)
    # print(list(result))

    b4 = 5.7 * np.exp(-6) * b1
    print(b4.mean())
    # 筛选出含有特定值的列
    array = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9],
                      [1, 4, 7],
                      [2, 3, 5]])

    # 筛选条件：列的最小值大于1
    threshold = 4
    array = array.T
    # 找到满足条件的列的索引
    # condition = np.where(array[0] > threshold, True, False)
    #
    # # 使用condition作为布尔索引来筛选列
    # m_array = array * condition
    # print("m_array=", m_array)
    # filtered_array = array[:, condition]
    #
    # print(filtered_array)


    def test(x):
        for i in range(x.shape[0]):
            condition_ = np.where(x[i] > 4, True, False)
            x = x[:, condition_]
        return

    test(array)
    print(array)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
