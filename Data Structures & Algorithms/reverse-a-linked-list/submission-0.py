# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr: #curr 是 None，循环停下。
            temp = curr.next     # 1. 先记住下一个是谁（不然改了箭头就找不到了）
            curr.next = prev     # 2. 把 curr 的箭头掉头，指向前一个
            prev = curr          # 3. prev 往前走一步
            curr = temp          # 4. curr 往前走一步       
        return prev