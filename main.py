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

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
