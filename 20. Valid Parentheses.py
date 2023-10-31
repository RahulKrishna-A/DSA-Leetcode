class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in s:
            if i == '{' or i == '[' or i == '(':
                st.append(i)
            else:
                if len(st) == 0:
                    return False
                last = st[-1]
                st.pop()
                if (i == '}' and last == '{') or (i == ']' and last == '[') or (i == ')' and last == '('):
                    continue
                else:
                    return False
        return len(st) == 0
