class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freqsMap = {}
        for i in nums:
            freqsMap[i] = freqsMap.get(i,0) + 1

        freqsArray = [[] for _ in range(n+1)]

        for num,freq in freqsMap.items():
            freqsArray[freq].append(num)

        res = []
        last = n - 1

        while len(res) < k:
            if len(freqsArray[last]) != 0:
                res.extend(freqsArray[last])
            last -= 1
        return res
