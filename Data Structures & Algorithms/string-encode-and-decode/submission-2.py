class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for word in strs:
            need = 3 - len(str(len(word)))
            num = (need * "0") + str(len(word))
            ans.append(num + word)
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        left = 0
        print(s)
        # 0 <= strs[i].length <= 200
        # l                                     
        # 002we003say001:003yes010!@#$%^&*()
        while left < len(s):
            length = int(s[left:left+3])
            right = left + length + 2
            ans.append(s[left + 3: right + 1])
            left = right + 1
        return ans
