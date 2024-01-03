class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        least_banana_per_hour, max_banana_per_hour = 1, max(piles)
        total_hours_taken = max_banana_per_hour
        while least_banana_per_hour <= max_banana_per_hour:
            mid_point = (least_banana_per_hour + max_banana_per_hour) // 2
            hours_per_piles = 0
            for pile in piles:
                hours_per_piles += math.ceil(pile/mid_point)
            if hours_per_piles <= h:
                max_banana_per_hour = mid_point - 1
                total_hours_taken = min(mid_point, total_hours_taken)
            else:
                least_banana_per_hour = mid_point + 1
        return total_hours_taken
