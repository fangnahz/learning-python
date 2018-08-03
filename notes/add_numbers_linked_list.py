""" You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    carry = 0
    cursor = result
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        num = v1 + v2 + carry
        if num > 9:
            carry = 1
            num = num % 10
        else:
            carry = 0
        cursor.val = num
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if l1 or l2 or carry:
            cursor.next = ListNode(0)
            cursor = cursor.next
    return result


def addTwoNumbers_2(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = ListNode(0)
    carry = 0
    cursor = result
    while l1 and l2:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        num = v1 + v2 + carry
        if num > 9:
            carry = 1
            num = num - 10
        else:
            carry = 0
        cursor.val = num
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        if not l1 and not l2:
            if carry:
                cursor.next = ListNode(1)
            return result
        else:
            cursor.next = ListNode(0)
            cursor = cursor.next
    l = l1 if l1 else l2
    while l:
        num = l.val + carry
        if num < 10:
            cursor.val = num
            cursor.next = l.next
            return result
        else:
            carry = 1
            cursor.val = 0
            l = l.next
            if not l:
                cursor.next = ListNode(1)
                return result
            cursor = cursor.next
