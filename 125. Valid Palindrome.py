class Solution(object):
    def isPalindrome(self, s):
        new_str = ""
        for i in range(len(s)):
            if s[i].isalnum():
                new_str+=s[i].lower()
        if new_str == new_str[::-1]:
            return True
        return False