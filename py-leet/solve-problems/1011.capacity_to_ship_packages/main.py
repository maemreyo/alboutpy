from typing import List


class Solution:
    @staticmethod
    def shipWithinDays(weights: List[int], days: int) -> int:
        max_weight, total_weight = -1, 0
        for weight in weights:
            max_weight = max(max_weight, weight)
            total_weight += weight
        left, right = max_weight, total_weight
        while left < right:
            mid = (left + right) // 2
            days_needed, curr_weight = 1, 0
            for weight in weights:
                if curr_weight + weight > mid:
                    days_needed += 1
                    curr_weight = 0
                curr_weight += weight
            if days_needed > days:
                left = mid + 1
            else:
                right = mid
        return left
