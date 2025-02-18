# O(1) - Константное время
# Алгоритм работает в за фиксированное время, независимо от размера входных


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def get_element_by_index(lst, index):
    return lst[index]


print(get_element_by_index(lst, 4))

# O (log n) логарифмическое время
# Часто встречается в алгоритмах, использующих
# деление входных данных на части (например, бинарный поиск).


def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right - mid - 1

    return -1
# print(binary_search(lst, 9)

# O (n) - Линейное время
# Алгоритм проходит по всем входным данным один разю


def find_element(lst, target):

    for i in lst:
        print(i)
        if i  == target:
            return True

    return False
print(find_element(lst, 10))

# O (n^2) - квадратичное время
# Обычно встречается в алгоритмах с двумя вложениями
# циклами, например, в пузырьковой сортировке.
lst3 = [9, 2, 5, 1, 5, 2, 8, 7, 45]

print(lst3.sort())
print(lst3)



def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j +1]:
                lst[j], lst[j +1] = lst[j + 1], lst[j]


bubble_sort(lst=lst3)
print(lst3)


def two_sum(nums, target):
    num_map, i = {}, {}

    for i, num in enumerate(nums):
        complemenet = target - num
        if complemenet in num_map:
            return [num_map{}]

