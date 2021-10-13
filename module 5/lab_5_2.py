first = list(range(1, 10))
second = list(range(1, 10, 2))
third = []


def find_intersections(fst_lst, scd_lst):
    for el in fst_lst:
        for it in scd_lst:
            if it == el:
                third.append(it)
    return third


print(find_intersections(first, second))
