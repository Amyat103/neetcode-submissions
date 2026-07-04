"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        watch vid instantly even though saw in uni course once

        hyppthesis, keep a list of most, so every time overlap, check if can go into one of these, else add room

        watched vid
        input: same as last one, list of intervlas objects
        output: max room needed

        split intervals into their own array, start end

        2 pointsers, and loop, s pointer adn e pointer
        everytime we increment s, which eman a meeting start,
        everytime s > end, can close a meeting, basically ignore the pairs, and count base on room need, and room ended

        """
        ans = 0
        intervals.sort(key=lambda x: x.start)
        starts = []
        ends = []
        for i in range(len(intervals)):
            starts.append(intervals[i].start)

        intervals.sort(key=lambda x:x.end)
        for i in range(len(intervals)):
            ends.append(intervals[i].end)
        
        s=e=0 #initialize it
        #0,5,15
        #10,20,40
        curr = 0

        while s < len(intervals): # start looping we track s cuz thats main one openi
            if starts[s] >= ends[e]:
                curr -= 1
                e+=1
            else:
                curr += 1
                s+=1
            
            ans = max(ans, curr)

        return ans