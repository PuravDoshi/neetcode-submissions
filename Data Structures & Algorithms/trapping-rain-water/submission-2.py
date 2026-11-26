class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_height = [0] * n
        max_left_height = 0
        for i in range(n):
            left_height[i] = max_left_height
            if height[i] > max_left_height:
                max_left_height = height[i]

        right_height = [0] * n
        max_right_height = 0
        for i in range(n-1, -1, -1):
            right_height[i] = max_right_height
            if height[i] > max_right_height:
                max_right_height = height[i]
        
        final = [0] * n
        for i in range(n):
            final[i] = min(left_height[i], right_height[i]) - height[i]
        rain = 0
        for i in final:
            if i > 0:
                rain = rain + i
        return rain