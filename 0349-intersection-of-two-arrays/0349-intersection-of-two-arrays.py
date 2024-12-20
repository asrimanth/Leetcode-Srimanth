class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        # return list(nums1.intersection(nums2))
        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
        return intersection
