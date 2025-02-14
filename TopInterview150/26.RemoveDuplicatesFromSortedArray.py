
def remove_elements(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k, nums[:k]


test_arr = [1, 1, 2, 3, 4, 4, 5]

print(remove_elements(test_arr))