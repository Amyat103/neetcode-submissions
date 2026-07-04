class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] -= 1
        
        heap = []
        heapq.heapify(heap)

        for key,val in count.items():
            heapq.heappush(heap, (val, key))
        
        ans = []
        
        for _ in range(k):
            _, curr = heapq.heappop(heap)
            ans.append(curr)
        return ans    
