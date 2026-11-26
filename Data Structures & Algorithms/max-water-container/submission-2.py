class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = 0
        n = len(heights)
        left = 0
        right = n - 1
        while left <= right:
            h = min(heights[left], heights[right])
            w = right - left
            v = h * w
            max_vol = max(max_vol, v)
            if heights[left] <= heights[right]:
                left = left + 1
            else:
                right = right - 1
        return max_vol