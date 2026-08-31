import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if len(nums) == 1:
            return nums

        # Stores number: count of it's occurence
        numCounter = {}
        for n in nums:
            numCounter[n] = numCounter.get(n,0) + 1
        
        # Store this numCounter values in the heap but make count as the first \
        # element in the tuple. such that, heap will sort the tuples by the first element \
        # And when we pop from the heap, the minimum counts tuple come out first.
        # The idea is, we keep popping from the heap until the length of the heap is k. 
        # While we are popping, all the lower count nums shall have popped out leaving it \
        # containing the 'k' tuples that have the highest count of occurence in the nums.

        myheap = []
        
        for val,freq in numCounter.items():
            # Here, the tuple (freq,val) is the element to the heap;
            heapq.heappush(myheap,(freq,val))
        
        while len(myheap) > k:
            heapq.heappop(myheap)
        
        res = []
        while myheap:
            val = heapq.heappop(myheap)
            res.append(val[1])
        
        return res
        

        
