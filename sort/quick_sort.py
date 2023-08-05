nums = [5, 6, 4, 8, 3, 7, 10, 2, 9, 1]


def quick_sort(left, right):
    if left >= right:
        return
    pivot = nums[left]
    i, j = left, right
    while i != j:
        while nums[i] <= pivot and i < j:
            i += 1
        while nums[j] >= pivot and i < j:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[i], nums[left] = nums[left], nums[i]
    quick_sort(left, j - 1)
    quick_sort(j + 1, right)


def sort():
    pass


quick_sort(0, len(nums) - 1)
print(nums)
