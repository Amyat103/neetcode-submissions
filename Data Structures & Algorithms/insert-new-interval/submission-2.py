class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        insert new interval in, need to keep it non overlapping

        1) loop through the intervals
        if overlap
        - new interval start is after curr start but end is before curr end
        (newINterval[0] > curr[0] and new[1] < curr[1])
        merge, newInterval[0] = min(new and curr [0]), newINterval[1] = max(new and curr[1])
        
        keep going

        options
        1) non overlap, continue looping, append curr and kepe check
        2) overlap, make new interval with max,min[] and continue looping
        3) if new < curr, add new before and and rest in
        """
        ans = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #new less than curr, add new, add rest, return
                ans.append(newInterval)
                return ans + intervals[i:]
            elif newInterval[0] > intervals[i][1]: #non overlap
                ans.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        ans.append(newInterval)
        return ans
