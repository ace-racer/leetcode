from typing import List
import copy

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        if k > 0:
            rotate_times = k
            if rotate_times > nums_len:
                rotate_times = rotate_times % nums_len

            elements_index_to_move_front = nums_len - rotate_times

            nums_copy = copy.deepcopy(nums[:elements_index_to_move_front])  
            del nums[:elements_index_to_move_front]
            
            nums.extend(nums_copy)
            # print(nums)

s = Solution()
s.rotate([1,2,3,4,5,6,7], 3)
# 5,6,7,1,2,3,4

s.rotate([-1, -100, 3, 99], 2)

s.rotate([-1, -100, 3, 99], 10)

s.rotate([-1, -100, 3, 99], 0)
