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
            # m is the index of middle element
            m = (l + r) // 2
            # so, we have m + 1 (adjusting for 0 based indexing) NUMBER OF ELEMENTS from the left partition.
            # The remainig elements have to come from the other array.
            # To calculate that, take the length of half of total NUMBER OF ELEMENTS, subtract the NUMBER OF ELEMENTS given by the left partition of 1st array (array a), subtract 1 such that, 
            # we get the 'index' of the middle element in array b

            midIndexb = half - (m+1) - 1
            # Here, the if else is checking whether the index is in bounds.
            # if it is overflown to left, it is -inf (coz the array is sorted).
            # similarly, if it is overflown to right , it is +inf.
            aleft = a[m] if m >= 0 else float('-infinity')
            bleft = b[midIndexb] if midIndexb >= 0 else float('-infinity')
            aright = a[m+1] if (m + 1) < n1 else float('infinity')
            bright = b[midIndexb + 1] if (midIndexb + 1) < n2 else float('infinity')
            
            # check if we have reached the appropriate partition (i.e, mid point of the merged array)
            if aleft <= bright and bleft <= aright:
                # Odd cases
                if total % 2 != 0:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft) + min(aright,bright))/2
            # if the contribution from array a is more, move the right pointer to before m
            # so as to search for lesser element from a
            elif aleft > bright:
                r = m - 1
            else:
                l = m + 1



    
        






