from functools import lru_cache
import math
class Solution:
    def jump(self, nums):
        n = len(nums)

        @lru_cache(maxsize=None)
        def jump_at_idx(idx):
            if idx >= n - 1:
                return 0
            min_jumps = math.inf
            for i in range(nums[idx]):
                count = jump_at_idx(idx + i + 1)
                if min_jumps > count:
                    min_jumps = count
            
            return min_jumps + 1

        return jump_at_idx(0)


if __name__ == "__main__":
    test_nums = [2,1]
    print(Solution().jump(test_nums))
