class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        ask -- can points be empty? can each points[i], >< x,y? will k alwyas be valid? like non neg or not > len(poitns?)
        k =< len(points), wont be neg or 0 ok, points can negative xy plain
        stack heap, not stack
        heap, (distance, (x,y)), heappop()
        O(n log n)
        O(n) store everything
        """
        heap = []

        for x, y in points:
            #sqrt((x1 - x2)^2 + (y1 - y2)^2)
            distance = math.sqrt((x - 0)**2 + (y - 0)**2)#origin always stay 0,0
            heapq.heappush(heap, (distance, (x,y)))

        ans = []
        for _ in range(k):
            _, (p1, p2) = heapq.heappop(heap)
            ans.append([p1,p2])
        
        return ans