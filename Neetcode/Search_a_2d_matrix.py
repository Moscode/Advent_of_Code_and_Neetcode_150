class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            mid_point_1 = (lo + hi) // 2
            matrix_value = matrix[mid_point_1]
            l, r = 0, len(matrix_value) - 1
            while l <= r:
                mid_point_2 = (l + r) // 2
                if target < matrix_value[mid_point_2]:
                    r = mid_point_2 - 1
                elif target > matrix_value[mid_point_2]:
                    l = mid_point_2 + 1
                elif target == matrix_value[mid_point_2]:
                    return True
                else:
                    break
            if target < matrix_value[0]:
                hi = mid_point_1 - 1
            elif target > matrix_value[-1]:
                lo = mid_point_1 + 1
            else:
                return False
        return False