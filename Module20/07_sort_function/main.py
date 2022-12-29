def tpl_sort(a, b, c, d, f, g, k):
    mylist = a, b, c, d, f, g, k
    if all(type(item) is int for item in mylist):
        return sorted(mylist)
    else:
        return mylist

print(tpl_sort(6, 3, -1, 8, 4, 10, -5))