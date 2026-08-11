import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1
        # Just an empty list
        heap = []
        for val,freq in counts.items():
            # because (min) heap will sort based on frequencies in ascending order
            heapq.heappush(heap,[freq,val])
        
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        while len(heap):
            num = heapq.heappop(heap)[1]
            res.append(num)
        return res