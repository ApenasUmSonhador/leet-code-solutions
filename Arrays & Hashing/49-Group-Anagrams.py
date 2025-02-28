class Solution(object):
    def groupAnagrams(self, strs):
        palindromes = {}
        solution = []
        for new in strs:
            new_dict = {}
            for letter in new:
                if letter in new_dict:
                    new_dict[letter] += 1
                else:
                    new_dict[letter] = 1
            
            i, stop = 0, False
            while i < len(solution) and not stop:
                if palindromes[solution[i][0]] == new_dict:
                    stop = True
                else:
                    i += 1
            if stop:
                solution[i].append(new)
            else:
                palindromes[new] = new_dict
                solution.append([new])
        return solution
        