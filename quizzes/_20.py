"""
    Question: Valid Parentheses
    Desc: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

            An input string is valid if:

            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.
    URL: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def check_valid_parentheses(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ")" and stack[-1] != "(":
                    return False
                if c == "}" and stack[-1] != "{":
                    return False
                if c == "]" and stack[-1] != "[":
                    return False
                stack.pop()
        return len(stack) == 0
