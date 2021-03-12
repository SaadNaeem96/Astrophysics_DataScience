import numpy as np

def sidereal_converter(fileName):
    data = np.genfromtxt(fileName,
                     names=None,
                     dtype=None,
                     delimiter=',')
    for i in range(len(data)):
        data[i][0] = (data[i][0]-1973)*366.242
    return data

def square(arr):
    return arr**2

def get_pi():
    return np.pi

def picky(num):
    if not isinstance(num, (np.float, float, np.int, int)):
        raise TypeError("Must input a number")
