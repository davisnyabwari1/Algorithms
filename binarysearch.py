list = [4, 7, 8, 12, 45, 99, 100]
search_value = 100


def search(list, search_value):
    lowerbound = 0
    upperbound = len(list)-1

    for items in list:
        mid_index = (lowerbound+upperbound)//2
        if list[mid_index] == search_value:
            return True
        else:
            if list[mid_index] < search_value:
                lowerbound = mid_index+1
            else:
                upperbound = mid_index-1
    return False


if search(list, search_value):
    print('Found value')
else:
    print('Not Found')


# list = [4, 7, 8, 12, 45, 99]
# search_value = 99


# def search(list, search_value):
#     lowerbound = 0
#     upperbound = len(list)-1

#     while lowerbound <= upperbound:
#         mid_index = (lowerbound+upperbound)//2
#         if list[mid_index] == search_value:
#             return True
#         else:
#             if list[mid_index] < search_value:
#                 lowerbound = mid_index+1
#             else:
#                 upperbound = mid_index-1
#     return False


# if search(list, search_value):
#     print('Found value')
# else:
#     print('Not Found')
