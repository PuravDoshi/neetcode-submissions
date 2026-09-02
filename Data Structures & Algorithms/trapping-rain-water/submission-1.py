class Solution:
    def trap(self, height: List[int]) -> int:
        # n = len(height)
        # max_left = 0
        # max_right = 0
        # ml = []
        # mr = [0]*n
        # temp = []
        # result = []
        # total = 0
        # for i in range(n):
        #     ml.append(max_left)
        #     if height[i] > max_left:
        #         max_left = height[i]
        # for i in range(n-1, -1, -1):
        #     mr[i] = max_right
        #     if height[i] > max_right:
        #         max_right = height[i]
        # for i in range(n):
        #     temp.append(min(ml[i], mr[i]))
        # for i in range(n):
        #     diff = temp[i] - height[i]
        #     if diff < 0:
        #         diff = 0
        #     result.append(diff)
        # for i in range(n):
        #     total = total + result[i]
        # return total

        if height is None:
            return 0
        res = 0
        n = len(height)
        l = 0
        r = n-1
        leftmax = height[l]
        rightmax = height[r]
        while l < r:
            if  leftmax <= rightmax:
                l = l + 1
                leftmax = max(leftmax, height[l])
                res = res + (leftmax - height[l])
            else:
                r = r - 1
                rightmax = max(rightmax, height[r])
                res = res + (rightmax - height[r])
        return res