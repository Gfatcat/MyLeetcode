# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。 
# 
#  如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。 
# 
#  您可以假设除了数字 0 之外，这两个数都不会以 0 开头。 
# 
#  示例： 
# 
#  输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#  
#  Related Topics 链表 数学 
#  👍 4975 👎 0

# Begin  Time: 2020-09-29 17:20:21
# Finish Time:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head
        c = 0
        while l1 is not None or l2 is not None or c != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + c
            c = sum // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            temp.next = ListNode(sum % 10)
            temp = temp.next
        return head.next


# leetcode submit region end(Prohibit modification and deletion)
a = ListNode(5)
# a.next = ListNode(4)
# a.next.next = ListNode(3)
b = ListNode(5)
# b.next = ListNode(6)
# b.next.next = ListNode(4)
print(Solution().addTwoNumbers(a, b))
