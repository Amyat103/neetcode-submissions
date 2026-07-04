"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        did not watch sol, but done 2 medium intervals so wan tot ry
        input: list of intervals object, which have .start .end, 
        return if a person can take everything, without conflcit, num==num not conflict
        no course limit, and already sorted

        ask -- ok is there any edge cases, empty, or neg since they are sorted 
        ok intervals can be empty i see and intervals number cant be neg ok

        #1 lookin gat this im thinking cuz its already sroted, go through ecach one start 1, index, inf conflcit
        return false
        else true

        and this algo will need a edge case cehck of empty or 1
        """
        # wait it never said sorted but so nede to sort
        intervals.sort(key=lambda x:x.start)
        #edge case since for loop dont handle
        if len(intervals) <=1:
            return True #cuz 0 courses can satisfy? and 1 course also, no conflict

        #main loopp
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

        #check