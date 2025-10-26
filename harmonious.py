from collections import Counter
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cnt = Counter(nums)
        best = 0
        for x in cnt:
            if x + 1 in cnt:
                best = max(best, cnt[x] + cnt[x + 1])
        return best
