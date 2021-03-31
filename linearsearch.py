# mylist = [5, 8, 4, 6, 9, 2]
# elementOfsearch = 9
# pos = 0


# def search(mylist, elementOfsearch):
#     i = 0
#     while i < len(mylist):
#         if mylist[i] == elementOfsearch:
#             globals()['pos'] = i
#             return True
#         i = i+1

#     return False


# if search(mylist, elementOfsearch):
#     print('Found at position', pos+1)
# else:
#     print('Not found')


# LINEAR SEARCH USING FOR LOOP
mylist = [5, 8, 4, 6, 9, 2]
elementOfsearch = 2
pos = 0


def search(mylist, elementOfsearch):
    for i in mylist:
        if i == elementOfsearch:
            globals()['pos'] = mylist.index(i)
            return True

    return False


if search(mylist, elementOfsearch):
    print('Found at position', pos+1)
else:
    print('Not found')
