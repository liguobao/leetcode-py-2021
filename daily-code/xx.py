from typing import List

i = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]

def func(l: List[int], left: int, right: int) -> int:
    if len(l[left:right + 1]) == 3:
        return l[right] if l[left] == l[left + 1] else l[left]
    mid = int((left + right) / 2)
    n = l[mid]
    if n == l[mid + 1] :
        if mid % 2 == 0:
            return func(l, mid, right)
        else: func(l, left, mid - 1)
    elif n == l[mid - 1]:
        if mid % 2 == 0:
            return func(l, left, mid)
        else:
            return func(l, mid + 1, right)
    else:
        return n

print(func(i, 0, len(i) - 1))