# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        # save the linked list elements into an array
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        # checking whether it is a Palindrome
        return vals == vals[::-1]