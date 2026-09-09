class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merArr = []
        n1 = len(nums1)
        n2 = len(nums2)
        
        i = 0
        j = 0
        while i < n1 and j < n2:
            
            if nums1[i] <= nums2[j]:
                merArr.append(nums1[i])
                i += 1
            else:
                merArr.append(nums2[j])
                j += 1

        while i < n1:
            merArr.append(nums1[i])
            i += 1

        while j < n2:
            merArr.append(nums2[j])
            j += 1

        print(merArr)
        # even
        mid1 = (n1 + n2)//2
        if len(merArr) % 2 == 0:
            mid2 = mid1 - 1
            return (merArr[mid1]+merArr[mid2]) / 2
        else:
            return merArr[mid1]






