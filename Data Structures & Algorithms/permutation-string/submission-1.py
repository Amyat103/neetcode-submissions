class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        given, s1,s2, returun true/fase if s1 exist as permutation in string 2
        ex1 "cab" "abc" True, ex2 False, "caab" "abc" not permuation, ebcause extra letter
        empty? or s2 > s1? no not emprt, can be more less ok
        
        Input: s1 = "abc", s2 = "lecabee" -- window size 3
        if s2 < s1, retunr false
        l,r += 1 each time. each time the algo will check s1.sorted == s2.sorted, if out of loop, retunr false
        Time: O(n * n log n) sort?
        2) actually i can make it n*n? faster than n log n, by doing
        each window. put the 2 string into a list [0]* 26, mark index += 1 for eahc letter ord()
        if wind1==wind2 reutnr true
        O(n^2) because loop n times, for eahctime O(n) operation
        sitll too slow
        NO
        26 is the max so constant
        """
        if len(s2) < len(s1):
            return False
        list1 = [0]*26
        list2 = [0]*26

        for l in s1:
            list1[ord(l) - ord("a")] += 1
        
        for i in range(len(s1)):
            list2[ord(s2[i]) - ord("a")] += 1

        left = 0

        for right in range(len(s1), len(s2)):
            print(list1)
            print(list2)
            if list1 == list2:
                return True

            list2[ord(s2[left]) - ord("a")] -= 1
            list2[ord(s2[right]) - ord("a")] += 1

            left += 1

        return list1 == list2