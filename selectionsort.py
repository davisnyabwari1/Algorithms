list = [5, 3, 2, 1, 100, 10, 15]


def sort(list):
    # unsorted list
    for i in range(len(list)-1):
        minpos = i
        # sorted list
        for j in range(i, len(list)):
            if list[j] < list[minpos]:
                minpos = j
        # swap the final minpos value and list[i]
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


sort(list)
print(list)
