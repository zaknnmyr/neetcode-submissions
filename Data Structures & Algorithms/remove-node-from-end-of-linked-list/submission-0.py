# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        tmp = head
        count = 1

        while tmp.next:
            tmp = tmp.next
            count += 1

        # if len = 5 and n = 2, then we want to remove index 3
        # len - n = removal index
        removalIndex = count - n
        if removalIndex == 0:
            return head.next

        tmp = head
        for i in range(count - 1):
            if (i + 1) == removalIndex:
                tmp.next = tmp.next.next
                break
            tmp = tmp.next
        return head



        