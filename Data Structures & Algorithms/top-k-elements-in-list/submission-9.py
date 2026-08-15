import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqsMap = {}
        for i in nums:
            freqsMap[i] = freqsMap.get(i,0) + 1

        heap = []
        for num,freq in freqsMap.items():
            heapq.heappush(heap,[freq,num])
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        while len(heap):
            res.append(heapq.heappop(heap)[1])
            
        return res
