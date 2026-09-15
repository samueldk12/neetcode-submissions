class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        same_letters_s = {}
        same_letters_t = {}

        for i in range(len(s)):
            if s[i] not in same_letters_s:
                same_letters_s[s[i]] = 1
            else:
                same_letters_s[s[i]] += 1
            
            if t[i] not in same_letters_t:
                same_letters_t[t[i]] = 1
            else:
                same_letters_t[t[i]] += 1
        
        if same_letters_s == same_letters_t:
            return True
        else: 
            return False
        
