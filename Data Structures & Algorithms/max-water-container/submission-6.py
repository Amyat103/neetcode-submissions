class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        ok need to find 2 index to store max water, some algo:
        2 pointers, greedy (since its  not sorted or indicated cant really say sliding window cuz no pattern or constraints)
        so 2 pointers or greedy...

        brute will be n^2 go though all possibility, double loop, for i (0..n), for j (i..n)
        
        but def sth else
        greedy, 2 pointer keep moinv forward, not sure if i can, maybe left, right, if right > left, left = right, but might loose it,
        unless canculate, then move left = right

        or 2 pointer greedy -- left = 0 right = n, if left < right -> left += 1, if right < left ,right -= 1
        this i feel good because the amount of water, width matter
        """

        ans = left = 0
        right = len(heights) - 1

        while left < right:
            curr = min(heights[left], heights[right]) * (right - left)
            ans = max(curr, ans)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
   
        return ans