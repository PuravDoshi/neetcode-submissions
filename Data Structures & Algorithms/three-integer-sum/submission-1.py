class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        for i in range(n):
            myset = set()
            for j in range(i+1, n):
                third = -(nums[i] + nums[j])
                if third in myset:
                    temp = [nums[i], nums[j], third]
                    temp.sort()
                    res.add(tuple(temp))
                else:
                    myset.add(nums[j])
        final = []
        for i in res:
            final.append(list(i))
        return final