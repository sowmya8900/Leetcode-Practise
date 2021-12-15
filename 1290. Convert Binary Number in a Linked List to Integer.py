# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        h = []
        while(head):
            h.append(head.val)
            head = head.next
            
        
        ans = ''.join(str(i) for i in h)
        return(int(ans,2))
