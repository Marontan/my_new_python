import time
from matplotlib import pyplot
import math
import random
from Sort import bubble_sort

def measure_time(fn, *args):
    start = time.time()
    fn(*args)
    end = time.time()
    return end - start

string_multiply = lambda n, *args:"s" * n * 2500000
string_const = lambda n, *args: "a" * 2500000

def linears_search(search_list, *args):
    searched_item = search_list[-1]
    for item in search_list:
        if item == searched_item:
            return item
    return None

def binary_search(search_list, *args):
    searched_item = search_list[-1]
    n = len(search_list)
    left = 0
    right = n-1
    while left <= right:
        middle = (left + right)//2
        if searched_item < search_list[middle]:
            right = middle - 1
        elif searched_item > search_list[middle]:
            left = middle+1
        else:
            return middle
    return None

# вычисление н-го числа Фибоначи
def fibbo(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)


if __name__ == '__main__':
    n_s = range(1,11)
    # outputs = [measure_time(string_multiply, n) for n in n_s]
    # outputs_const = [measure_time(string_const, n) for n in n_s]
    # output_log = [math.log(n,20) for n in n_s]
    # linear_search = [measure_time(linears_search, list(range(n*25000))) for n in n_s]
    # output_search = [measure_time(binary_search, list(range(n*25000))) for n in n_s]

    output_bubble = [measure_time(bubble_sort, list(range(n*1, 1, -1)))for n in n_s]

    # pyplot.plot(n_s, outputs)
    # pyplot.plot(n_s, outputs_const)
    # pyplot.plot(n_s, linear_search)
    # pyplot.plot(n_s, output_search)
    pyplot.plot(n_s, output_bubble)
    pyplot.legend(["outputs", "outputs_const", "linear_search", "bin_search"])
    pyplot.show()