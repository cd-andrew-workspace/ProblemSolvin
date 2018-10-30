def problem1(lst, index):
    if index < len(lst) + 1:
        return lst[index - 1]
    else:
        fixedIndex = index % len(lst)
        return lst[fixedIndex - 1]
