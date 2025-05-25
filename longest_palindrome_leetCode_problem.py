from collections import defaultdict

class Solution:
    def longestPalindrome(self, words):
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        length = 0
        central = False
        
        for word in list(word_count.keys()):
            if word[0] == word[1]:
                # It's a palindrome word like 'gg'
                count = word_count[word]
                pairs = count // 2
                length += pairs * 4
                if count % 2 == 1:
                    central = True
            else:
                # Check for the reverse word
                reversed_word = word[::-1]
                if reversed_word in word_count:
                    min_pairs = min(word_count[word], word_count[reversed_word])
                   
                    if word < reversed_word:
                        length += min_pairs * 4
        if central:
            length += 2
        return length