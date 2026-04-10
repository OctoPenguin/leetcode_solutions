from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr_len = len(nums)
        i = 0
        while i < arr_len - 1:
            cur_addend = nums[i]
            req_addend = target - cur_addend
            j = arr_len - 1
            while j > i:
                if nums[j] == req_addend:
                    return [i, j]
                j -= 1
            i += 1
        return [-1, -1]
