class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build freq
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # build array to heap and heapify
        heap = []        
        for key,val in freq.items():
            # default min heap so negative for max
            heap.append((-val,key))
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            # no need to abs the freq cuz pnly using num
            frequ, num = heapq.heappop(heap)
            ans.append(num)
        
        return ans