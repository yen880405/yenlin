class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        
        
        for word in queries:
            index = 0
            take_word = True
            
            
            for letter in word:
                if (index < len(pattern) and letter == pattern[index]):
                    index += 1
                elif ('A' <= letter <= 'Z'):
                    take_word = False
                    break
                else:
                    pass
                
            if (take_word):
                if (index != len(pattern)):
                    ret.append(False)
                else:
                    ret.append(True)
            else:
                ret.append(False)
                    
        return ret
