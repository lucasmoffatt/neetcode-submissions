# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = -1
        node_num = 0
        visited = {}

        while head is not None:
            if head in visited:
                index = visited[head]
                return True
                break
            else:
                visited[head] = node_num
                node_num += 1
                head = head.next
        
        return False