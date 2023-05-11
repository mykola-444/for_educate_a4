def min_elem(nums):
    min_element = float("inf")
    for num in nums:
        if num < min_element:
            min_element = num
    return min_element


def min_elem1(nums):
    min_element = 100
    if nums is None:
        print("Введіть не менше одного числа")
        print(min_element)
        min_element = 0
    else:
        min_element = 100
        for num in nums:
            if num < min_element:
                min_element = num
    return min_element


assert min_elem([1, 2, 3, 0]) == 0

assert min_elem([1, 2, 3, 0, -10]) == -10
assert min_elem([1, 2, 3]) == 1

print(min_elem1([]))
