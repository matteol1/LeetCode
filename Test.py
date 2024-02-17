# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()
        current = l3
        carry = 0
        loop=0
        while (l1 != None and l2 != None):
            current.val = (l1.val + l2.val + carry) % 10
            print(current.val)
            carry = (l1.val + l2.val + carry) // 10
            print(carry)
            # Move list pointers forward
            if l1.next != None:
                l1 = l1.next
            else:
                l1=None
            if l2.next != None:
                l2 = l2.next
            else:
                l2 = None
            if (l1 or l2) or carry:
                current.next = ListNode()
                current = current.next
            #l1 longer
            loop+=1
            print(f"Loop: {loop}")
        while l1 != None:
            current.val = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            # Move list pointers forward
            if l1.next != None:
                l1 = l1.next
            else:
                l1=None
            if l1 or carry:
                current.next = ListNode()
                current = current.next
                    #l1 longer
        while l2 != None:
            current.val = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            # Move list pointers forward
            if l2.next != None:
                l2 = l2.next
            else:
                l2=None
            if l2 or carry:
                current.next = ListNode()
                current = current.next
        if carry == 1:
            current.val = 1
        return l3
    

a1 = ListNode(1)
a1.next = ListNode(8)
a2 = ListNode(0)

sol = Solution()
a3 = sol.addTwoNumbers(a1,a2)
print(a3.val)
print(a3.next.val)