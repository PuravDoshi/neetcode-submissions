class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = float('-inf')
        n = len(heights)
        left = 0
        right = n - 1
        while left < right:
                difference = right - left
                height = min(heights[left], heights[right])
                max_volume = max(max_volume, (difference * height))
                if heights[left] < heights[right]:
                    left = left + 1
                else:
                    right = right - 1
        return max_volume 