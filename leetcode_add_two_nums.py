# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # l1 represents the head of the lisnked list1
        dummy_head = ListNode(0)
        head = dummy_head
        rest = 0

        while l1 or l2 or rest != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            summ = (l1Val + l2Val + rest) % 10
            rest = (l1Val + l2Val + rest) // 10
            new_node = ListNode(summ)
            head.next = new_node
            head = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next

# # in case you dont understand the first code. this is another code writen in a simple and easy way
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # l1 represents the head of the lisnked list1
#         dummy_head = ListNode(0)
#         head = dummy_head
#         rest = 0
#
#         while l1 and l2:
#             summ = (l1.val + l2.val + rest) % 10
#             rest = (l1.val + l2.val + rest) // 10
#             new_node = ListNode(summ)
#             head.next = new_node
#             head = new_node
#             l1 = l1.next
#             l2 = l2.next
#         while l1:
#             summ = (l1.val + rest) % 10
#             rest = (l1.val + rest) // 10
#             new_node = ListNode(summ)
#             head.next = new_node
#             head = new_node
#             l1 = l1.next
#         while l2:
#             summ = (l2.val + rest) % 10
#             rest = (l2.val + rest) // 10
#             new_node = ListNode(summ)
#             head.next = new_node
#             head = new_node
#             l2 = l2.next
#         if rest != 0:
#             new_node = ListNode(rest)
#             head.next = new_node
#             head = new_node
#         return dummy_head.next



