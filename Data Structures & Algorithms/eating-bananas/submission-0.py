class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = 0
        min_eat = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours = hours + math.ceil(i / k)
            if hours <= h:
                min_eat = min(min_eat, k)
                r = k - 1
            else:
                l = k + 1
        return min_eat
