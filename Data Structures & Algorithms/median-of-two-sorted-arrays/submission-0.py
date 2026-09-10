class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0
        final = []
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                final.append(nums1[i])
                i = i + 1
            else:
                final.append(nums2[j])
                j = j + 1
        if i < n1:
            while i < n1:
                final.append(nums1[i])
                i = i + 1
        if j < n2:
            while j < n2:
                final.append(nums2[j])
                j = j + 1
        n = len(final)
        left = 0
        right = n - 1
        mid = (left + right)//2
        if n % 2 == 0:
            mid = (left + right)//2
            return (final[mid] + final[mid+1])/2
        else:
            return final[mid]