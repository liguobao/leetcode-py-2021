# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_head = list1
        second_head = list2
        if first_head is None:
            return second_head
        if second_head is None:
            return first_head
        new_head = None
        if first_head.val <= second_head.val:
            new_head = first_head
            first_head = first_head.next
        else:
            new_head = second_head
            second_head = second_head.next
        merge_head = new_head
        while first_head and second_head:
            if first_head.val <= second_head.val:
                merge_head.next =first_head
                first_head = first_head.next
            else:
                merge_head.next = second_head
                second_head = second_head.next
            merge_head = merge_head.next
        merge_head.next = first_head if first_head else second_head
        return new_head