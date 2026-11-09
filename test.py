class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        
        res = ''
        d = [None] * 10
        
        for i in A:
            
            
            ele = str(i)
            
            if d[int(ele[0])] is not None:
                d[int(ele[0])].insert(ele)
            else:
                d[int(ele[0])] = LinkedList(head=Node(ele))
            
            
        
        for i in range(9, -1, -1):
            if d[i] is not None:
                res += d[i].gather()
        
        return res
                
class LinkedList:
    
    def __init__(self, head):
        self.head = head
    
    def insert(self, v):
        
        prev = None
        curr = self.head
        ele = Node(v)
        
        while curr:
            if int(curr.val+v) < int(v+curr.val):
                ele.next = curr
                break
            prev = curr
            curr = curr.next
        if prev:
            prev.next = ele
        else:
            self.head = ele
    
    def gather(self):
        
        curr = self.head
        s = ''
        
        while curr:
            s += curr.val
            curr = curr.next
            
        return s

class Node:
    def __init__(self, v):
        self.val = v
        self.next = None
        
if __name__ == "__main__":
	obj = Solution()
	print(obj.largestNumber([8,89]))
