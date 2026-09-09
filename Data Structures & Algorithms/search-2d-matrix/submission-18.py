class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        # find candidate row
        top, bottom = 0, len(matrix) - 1
        row = -1
        while top <= bottom:
            mid_row = (top + bottom) // 2
            if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
                row = mid_row
                break
            if matrix[mid_row][0] > target:
                bottom = mid_row - 1
            else:
                top = mid_row + 1

        if row == -1:
            return False

        # binary search inside the row
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            if val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False



        


        

