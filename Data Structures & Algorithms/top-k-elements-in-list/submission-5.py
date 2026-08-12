import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqs = [[] for _ in range(n+1)]
        counts = {}
        for n in nums:
            counts[n] = counts.get(n,0) + 1

        for num,freq in counts.items():
            freqs[freq].append(num)
        # print(freqs)
        res = []
        for i in range(len(freqs)-1,-1,-1):
            if len(res) == k:
                break
            # print(i)
            if freqs[i]:
                res.extend([n for n in freqs[i]])

        return res


        




        

