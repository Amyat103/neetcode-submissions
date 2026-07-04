class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        input: gas, costt -- [ints..], gas[i] - gas at station, 
        cost[i] gas need to get to i+1 station from i
        car -- unlimited, begin emprt as one of station
        circular road
        1) problem, return a station i such that i can start there
        and go round and reach station i again
        2) constraints: 1 sol exists | empty list? no min 1, mismatch? no len(gas == cost) | no neg gas or cost

        1) brute force, or first algo come up is
        try all index, starting there nad run a drive(gas) if cant reach return faslse
        return the true starting index 
        but let mte see if i can think another algo
        2) greedy? start highest cost? works for 2 examples
        gas = [1,2,3,4], cost = [2,2,4,1] and gas = [1,2,3], cost = [2,3,2]
        this apporch try to get the highest cost out so we can accumulate
        problme is how to always find highest cost? not efficinet
        or actaully i can use a heap, O(n) and ill pre process the ehap using
        (cost, index), so pop out the highest and index
        but n log n, not sure its best, better than brute tho
        saw answer
        3) the problme is greedy too hard to come up with, almost impossible
        wonder if this is a pattern or just come up or not
        algo is that if no exist -1, else at most 1 answer
        this kinda tell (only after seeing ans) that we can cehck
        algo is cehck if possible, total gas > cost,
        if so greed, start from 0, if gas < cost, 
        asn += 1 until gas > cost, then continue, then go until finihs it,
        even tho this ignore previous neg, we dont need it because we removed the -1, at teh start
        only trying to if this can continue till end
        greedy remove
        """
        if sum(cost) > sum(gas):
            return -1
        ans = 0
        total = 0

        for i in range(len(gas)): #use gas can use either
            total += (gas[i] - cost[i])

            if total < 0:
                ans = i + 1
                total = 0 #reset
        
        return ans



