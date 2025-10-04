x = [8, 3, 2, 20, 53, 3, 2, 5, 1, 4]


def sorting(list_x, low, high):
    if low < high:
        pivot_x = get_pivot(list_x, low, high)
        sorting(list_x, low, pivot_x - 1)
        sorting(list_x, pivot_x + 1, high)
    return list_x


def get_pivot(list_y, low, high):
    i = low + 1
    j = high
    p = low
    # loop throught list
    # get p in the middle
    # i have to be less than p
    # j have to be greater than p
    count = 0
    while j > i:
        while list_y[i] <= list_y[p] and i <= high:
            i += 1
        while list_y[j] > list_y[p]:
            j -= 1
        if j > i:
            list_y[i], list_y[j] = list_y[j], list_y[i]
    if list_y[j] < list_y[p]:
        list_y[j], list_y[p] = list_y[p], list_y[j]
    return j


print(sorting(x, 0, len(x) - 1))
