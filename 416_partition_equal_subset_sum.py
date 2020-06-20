from typing import List

# https://leetcode.com/problems/partition-equal-subset-sum/
class Solution:
    def print_possible_sums(self, possible_sums: List[int]):
        print("Printing possible sums...")
        for sum_, is_possible in enumerate(possible_sums):
            print("{0}:{1}".format(sum_, is_possible), end=' ')

    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        else:
            possible_sums = [False] * (total_sum + 1)
            
            # take the first element or not take it
            possible_sums[0] = True
            possible_sums[nums[0]] = True
            
            total_nums = len(nums)
            total_possible_sums = len(possible_sums)

            # print(total_nums)
            # print(total_possible_sums)
            # self.print_possible_sums(possible_sums)

            for itr in range(1, total_nums):
                new_possible_sums = set()

                # take the current element
                for sum_val, is_possible in enumerate(possible_sums):
                    if is_possible:
                        #print(sum_val)
                        #print(nums[itr])
                        new_possible_sums.add(sum_val + nums[itr])

                for new_possible_sum in new_possible_sums:
                    possible_sums[new_possible_sum] = True


                # self.print_possible_sums(possible_sums)
                        
            return possible_sums[total_sum // 2]

s = Solution()
print(s.canPartition( [1, 5, 11, 5]))
print(s.canPartition( [1, 2, 3, 5]))