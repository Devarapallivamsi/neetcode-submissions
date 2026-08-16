import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        heap = []
        for n in nums:
            heapq.heappush(heap,n)

        maxSeqLen = 1
        # start tracking the longest consequence now.
        curr = heapq.heappop(heap)
        while len(heap):
            nxt = heapq.heappop(heap)
            seqLen = 1
            while curr + 1 == nxt:
                seqLen += 1
                if len(heap) == 0:
                    break
                curr = nxt
                nxt = heapq.heappop(heap)
                while curr == nxt:
                    curr = nxt
                    if len(heap):
                        nxt = heapq.heappop(heap)
                    else:
                        break
                    
            curr = nxt
            maxSeqLen = max(maxSeqLen,seqLen)
        return maxSeqLen
        


        