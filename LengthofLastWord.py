class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        words = s.strip().split()
        if len(words) == 0:
            return 0
        else:
            return len(words[len(words)-1])
