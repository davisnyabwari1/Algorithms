list = [5, 3, 2, 1, 100, 10, 15]


def sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]  # Swap
                list[j] = list[j+1]
                list[j+1] = temp


sort(list)
print(list)  # sorted list
