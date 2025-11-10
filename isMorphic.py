# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# solution using python

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths differ, they can never be isomorphic
        if len(s) != len(t):
            return False
        
        # Dictionaries to keep track of mappings from s->t and t->s
        map_s_t = {}
        map_t_s = {}
        
        for ch_s, ch_t in zip(s, t):
            # Check existing mapping from s to t
            if ch_s in map_s_t:
                if map_s_t[ch_s] != ch_t:
                    return False
            else:
                map_s_t[ch_s] = ch_t
            
            # Check existing mapping from t to s (to prevent duplicate mapping)
            if ch_t in map_t_s:
                if map_t_s[ch_t] != ch_s:
                    return False
            else:
                map_t_s[ch_t] = ch_s
        
        return True


# --- Example Usage ---
sol = Solution()

# Example 1
s1 = "egg"
t1 = "add"
print(f"Is '{s1}' and '{t1}' isomorphic? ->", sol.isIsomorphic(s1, t1))  # True

# Example 2
s3="hello"
s4="billion"
print(f"Is '{s3}' and '{s4}' isomorphic? ->", sol.isIsomorphic(s3, s4))  # False