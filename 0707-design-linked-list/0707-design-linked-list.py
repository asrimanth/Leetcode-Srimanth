class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        current_node = self.head
        new_node = ListNode(val)
        
        if index <= 0:
            new_node.next = current_node
            self.head = new_node
        else:
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.size += 1
            

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        current = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)