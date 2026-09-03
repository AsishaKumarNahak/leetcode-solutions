class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        parities = {x & 1 for x in nums1}
        if len(parities) == 1:
            return True
        return min(nums1) % 2 == 1