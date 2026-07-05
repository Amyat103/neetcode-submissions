class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        unsorted array, and k, return kth largest
        cant sort it ned to return kth largest, count k time backward
        can arry be empty? neg? k cant be larger tha len(nums)?
        brute force way is to sort and return, but cant do that
        1) use heap, and pop out max in order and return?
        """
        heap = [-n for n in nums]
        heapq.heapify(heap)

        ans = 0

        for _ in range(k):
            ans = heapq.heappop(heap)
        
        return -ans