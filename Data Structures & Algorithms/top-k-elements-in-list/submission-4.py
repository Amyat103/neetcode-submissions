class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        init dict, use heap, heapq.heappush...
        1st loop count
        2nd loop add heap
        third loop build res
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        heap = []
        
        for key,val in count.items():
            heapq.heappush(heap, (-val, key))

        res = []
        
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res