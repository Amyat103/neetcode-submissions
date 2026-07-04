class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        string s only "UPPER ENGLISH" 26 uniqyue letters
        can replace each letter k times, k given,
        input: s: str, and k:int
        ask -- any edge? empty string
        return int, longest substring
        #brute, is there brute? cant loop so amny times, dont think so
        #2 approach, sliding window come to mind but thinking about how to anchor on most char
        can keep a count dict, so for right.... dict[right] += 1, if dict[s[rigt]] > mostChar, mostChar = s[right]
        use dict to count, only track num, and have a string s that anchor most char?????
        i thin kthers another way to track, with + or - to track but if interview prob dont say, unless i thoruhg of it
        mock- so conitnue
        ok ill code it up, anything im missing or idk how to ask 
        '''
        #1 try to get all vars i need in 1 go, and meaningul
        count = defaultdict(int) #use this so dont have to if exist create
        left = ans = 0 #initialize left and ans
        most = 0
        # AAABABB, a:4, b:2, 4-

        for right in range(len(s)):
            count[s[right]] += 1
            most = max(most, count[s[right]])
            while ((right - left + 1) - most > k):
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
