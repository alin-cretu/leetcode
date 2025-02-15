def remove_duplicates(nums):
    k = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1
    return k


test_nums = [1, 1, 1, 2, 2, 3]
k = remove_duplicates(test_nums)
print(k, test_nums[:k])