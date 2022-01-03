class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if results.get(sorted_word, -1) == -1: # se a palavra não existe, cria a lista
                results[sorted_word] = [word] 
            else: # se essa key ja existir
                inner_list = results[sorted_word]
                inner_list.append(word)
                results[sorted_word] = inner_list
        return list(results.values())
    