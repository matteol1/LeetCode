class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ntocmap = {'2': ['a','b','c'],
        '3': ['d', 'e','f'],
        '4': ['g','h','i'],
        '5': ['j','k','l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w','x','y','z']}

        x = {}
        size = len(digits)
        solutions = set()
        for i, char in enumerate(digits):
             x[i] = ntocmap[char]
        #this creates a map between the index and the domain for that position

        def backtrack(assigned={}):
            if len(assigned) == size:
                return assigned
            for index,char in enumerate(digits):
                if index not in assigned:
                    for value in ntocmap[char]:
                        new_assigned = assigned.copy()
                        new_assigned[index] = value
                        result = backtrack(new_assigned)
                        charlist = [v for k,v in sorted(result.items())]
                        #my_dict = {'b': 2, 'a': 1, 'c': 3}
                        #sorted_dict = dict(sorted(my_dict.items()))
                        print(''.join(charlist))
                        solutions.add(''.join(charlist))
                else:
                    assigned.pop(index)
        a = backtrack()
        print(solutions)

sol = Solution()
sol.letterCombinations('23')
