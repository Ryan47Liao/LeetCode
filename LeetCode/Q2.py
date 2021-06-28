# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __repr__(self):
        S = '['
        while self.next is not None:
            S += str(self.val) + ','
            self = self.next 
        return S + str(self.val)  + ']'
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # print(l1,l2,sep='\n')
        def m10(a,b):
            s = a+b
            if s>=10:
                return (a+b-10,1)
            else:
                return (a+b,0)
        s,carry_over = m10(l1.val,l2.val)
        out = ListNode(s)
        Last = out
        while l1.next is not None or l2.next is not None:
            l1,l2= l1.next,l2.next
            if l1 is None:
                l1 = ListNode(0)
            elif l2 is None:
                l2 = ListNode(0)
            s,carry_over = m10(l1.val+l2.val,carry_over)
            Last.next = ListNode(s)
            Last = Last.next
        #Consider Move ON
        if carry_over > 0:
            Last.next = ListNode(carry_over)
        return out
    
if __name__ == '__main__':
    print("LeetCode Question 2: Sum of two numbers")
    L1s = [ListNode(2,ListNode(4,ListNode(3))),ListNode(0),
           ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))]
    L2s = [ListNode(5,ListNode(6,ListNode(4))), ListNode(0),ListNode(9,ListNode(9,ListNode(9,ListNode(9))))]
    for l1,l2 in zip(L1s,L2s):
        print('l1:',l1)
        print('l2:',l2)
        T = Solution()
        Out = T.addTwoNumbers(l1,l2)
        print(Out)
        print("_______End________")