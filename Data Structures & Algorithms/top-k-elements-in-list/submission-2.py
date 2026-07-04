class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        input [nums, ..] and int k,
        return k most requent elemnts

        if k == 1, reutnr most frequent
        if k == 2, reutnr top 2 most frequent

        brute force
        1) loop and count all, put into dict
        then a second loop to extract, ans = [], for __ in k, extract ans []

        2) heap
        loop and count, put into (count, int) tuples, use heap extract, and pop, put int into ans

        """

        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        
        count_tup = [(-count, num) for num,count in count.items()]

        heapq.heapify(count_tup)

        ans = []

        for _ in range(k):
            count, num = heapq.heappop(count_tup)
            ans.append(num)
        
        return ans
