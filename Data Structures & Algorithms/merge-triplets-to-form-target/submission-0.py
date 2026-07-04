class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        tirples - 2d arr ints, each elem is [ai,bi,ci] all ints
        wnat to find the target -- also triplet

        given this arry, reach target, can get there by doing a max(trip[i],trip[j])
        need to figure out how to loop,
        need to choose 1 or some triplets that i think can reach it
        loop and merge wont work
        - maybe pre process where i remove triplets that any of the num is > target's num
        becuase ops are all max() so if more cant reach remove form consideration
        - how to find triples to merge, merge all triplets? time consuming -- prob not
        - what if i greedy sort it, max first, nad keep trying in order
        if more> remove consideration, go to next

        SAW ans
        - given triplet, my pre process is actually right, adn remove a lot of extra ops
        - what i missed is that, since its triplet, so exactly 3, i can track. how many of
        the triplet in list have == target, and return if 3
        - this work 1) exactly triplet 2) since op is max() meaning if we dont consider the 
        trip with > target, itll mean we can definately reach it
        algo, i can do 2 ways
        my way
        - 1 O(n) loop keep goog triplet into a new list
        - 1 real loop iwth a check set(), track the index, and if len(set) == 3 return True
        #this is after seeing ans
        """
        check = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue #need to be processed out
            for i in range(len(t)): #or just range(3)
                if t[i] == target[i]: #if that index matches
                    check.add(i)
        
        return len(check) == 3


