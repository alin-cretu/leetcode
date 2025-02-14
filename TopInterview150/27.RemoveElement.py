

class Solution:
    @staticmethod
    def remove_element( nums, val) :
        k = 0
        for x in range(len(nums)):
            if val != nums[x]:
                nums[k] = nums[x]
                k += 1
        return nums[:k]



test_arr = [3,3, 2, 2, 3,3]

new_length = Solution.remove_element(test_arr, 3)

print(new_length)