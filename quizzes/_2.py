"""
    Question: Add two numbers
    Desc:   You are given two non-empty linked lists representing two non-negative integers. 
            The digits are stored in reverse order, and each of their nodes contains a single digit. 
            Add the two numbers and return the sum as a linked list.
            You may assume the two numbers do not contain any leading zero, except the number 0 itself..
    URL: https://leetcode.com/problems/add-two-numbers/
    Resource: Runtime: 72 ms Memory Usage: 13.9 MB
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        node = self
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return str(nodes)

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        sum_two = 0
        carry = 0
        dummy=ListNode()
        rnode=dummy
        while l1 or l2 or carry != 0 :
            sum_two = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            carry  = sum_two // 10
            rnode.next=ListNode(sum_two % 10)
            rnode=rnode.next

        return dummy.next