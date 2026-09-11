class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a = nums1
        b = nums2

        if len(a) > len(b):
            a,b = b,a
        n1 = len(a)
        n2 = len(b)

        total = n1 + n2
        half = total // 2
        
        l = 0
        r = n1 - 1

        while True:
            m = (l + r) // 2
            # (mid+1) -- counting the elements of partition 1
            # -1 at last. coz, adjusting for 0 based indexing
            midIndexb = half - (m+1) - 1
            aleft = a[m] if m >= 0 else float('-infinity')
            bleft = b[midIndexb] if midIndexb >= 0 else float('-infinity')
            aright = a[m+1] if m + 1 < n1 else float('infinity')
            bright = b[midIndexb + 1] if midIndexb + 1 < n2 else float('infinity')

            if aleft <= bright and bleft <= aright:
                # Odd cases
                if total % 2 != 0:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft) + min(aright,bright))/2
            elif aleft > bright:
                r = m - 1
            else:
                l = m + 1



    
        






