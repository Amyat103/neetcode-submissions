class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        can stones be empty? no min 1, weight all above 0? yes ok
        so since heaviest stone, i need to always get it, i can either sort or heap
        1) sorting, ill need to sort each tiem i smash, cuz adding back in
        O(n ^ n log n)
        2) heap, push and pop heap, n log n time
        just need to return arr[0] at the ened
        """
        heap = []

        for s in stones:
            heapq.heappush(heap, -s)
        
        #smash until len(1)
        while len(heap) > 1:
            stone_one = heapq.heappop(heap)
            stone_two = heapq.heappop(heap)

            new_stone = abs(abs(stone_one) - abs(stone_two))
            heapq.heappush(heap, -new_stone)
        
        #1 remind
        return abs(heap[0])