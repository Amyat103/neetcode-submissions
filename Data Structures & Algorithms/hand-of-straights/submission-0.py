class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        hand = [1,2,4,2,3,5,3,4], groupSize = 4
        empty? neg? no, min 1 len, hand is min 0
        1) 2 pointer after sorting
        [1,2,2,3,3,4,4,5]
        no, dont work cuz if len() // group > 2, 2 pointer wont work easily
        2)
        [1,2,2,3,3,4,4,5]
        [1,2,3,4][2,3,4,5]
        hand = [1,2,3,3,4,5,6,7], groupSize = 4
        [1,2,3,3,4,5,6,7] sorted
        [1,3,][2,]
        ans = [[] * len(hand) // 4]
        this way i can append and hceck prev easily and if no mathc reutnr false

        algo
        i = 0
        while i < len() - 1:
            for group in range(len() // groupSize):
                if hand[i] -1 != ans[group][i-1], dont match, return false
                ans[group].append(hand[i])
        very greedy but let me trace

        look ans
        algo is count and put into dict
        loop through the number after sorting
        so we know we using the start
        hand = [1,2,4,2,3,5,3,4], groupSize = 4
        [1,2,2,3,3,4,4,5]
        use 1, and loop gorupSize times, -=1 dict, if dont exist, return false
        else continue and count
        the pattenr is that we are always starting from samllest possible at that time
        adn using dict to -= 1 
        and keep going
        O(n log n)
        O n - space
        """
        if len(hand) % groupSize != 0:
            return False
        count = defaultdict(int)
        for h in hand:
            count[h] += 1
        
        hand.sort()

        for h in hand:
            #cehck fi can use as start
            if count[h]:
                #loop gorup size times
                for num in range(h, h + groupSize):
                    if not count[num]:
                        return False
                    count[num] -= 1
        
        return True
                