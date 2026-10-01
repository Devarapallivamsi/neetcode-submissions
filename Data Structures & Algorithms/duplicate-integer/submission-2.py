class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                #  Number is found twice, so duplicates exist;
                return True
            hashSet.add(i)
        # After looping through all the list, no number is 'ALREADY' found to be in the hashSet. So, there are no duplicates;
        return False
