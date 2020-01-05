class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        ans = []
        
        while i < len(s):
            if i+2 < len(s) and s[i+2] == '#':
                number = int(s[i:i+2])
                ans.append(chr(number + ord('a') - 1))
                i += 3
            
            else:
                number = int(s[i])
                ans.append(chr(number + ord('a') - 1))
                i += 1
        
        return ''.join(ans)

'''
class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapper = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i',
                 '10#': 'j', '11#': 'k', '12#': 'l', '13#': 'm', '14#': 'n', '15#': 'o', 
                 '16#': 'p', '17#': 'q', '18#': 'r', '19#': 's', '20#': 't', '21#': 'u',
                 '22#': 'v', '23#': 'w', '24#': 'x', '25#': 'y', '26#': 'z'}
        
        length = len(s)-1
        ans = str()
        keep_word = str()
        
        while length >= 0:
            keep_word += s[length]
            if keep_word[::-1] in mapper:
                ans += mapper[keep_word[::-1]]
                keep_word = str()
            
            length -= 1
            
        return ans[::-1]
'''
        