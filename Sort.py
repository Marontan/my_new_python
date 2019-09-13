from random import shuffle

def bubble_sort(unsorted_list):
    is_swapp = True
    while is_swapp:
        is_swapp = False
        for i in range(len(unsorted_list)-1):
            if unsorted_list[i] > unsorted_list[i+1]:
                unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                is_swapp = True
    return unsorted_list

if __name__ == '__main__':
    list1 = list(range(100))
    shuffle(list1)
    print(list1)
    # print(measure_time(bubble_sort, list1))
    # bubble_sort(list1)
    print(list1)