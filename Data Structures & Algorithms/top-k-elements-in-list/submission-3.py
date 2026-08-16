class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [ints,...] retunr k most feq, k = 2, top 2 len(ans) == 2

        constraints -- all ints? yea. can k > len(uniquie nums?) no ok.
        nums empty? no min 1 ok

        1) loop and count, dict to track count
        first pass : count freq and unique nums
        sort it in an array [(freq, num),(freq, num)]
        second pass: for i in range k, ans.append(array[i][1])

        Time: O(n log n) space O(n)

        2) heap n log n, claner?
        first pass counting: 
        heapify the count, then pop base on k
        O(n log n) space O(n)
        """
        res = []

        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        count_array = []
        for key,val in count.items():
            count_array.append((-val, key))
        
        heapq.heapify(count_array)

        for _ in range(k):
            count, num = heapq.heappop(count_array)
            res.append(num)
        
        return res