"""
707:design-linked-list 设计链表
难度：中等
标签：链表
评价：中等难度题目中较简单的题目，虽然我写出来了，但是代码不够简练，参考了官方题解给出优化后的代码；还看到有人使用list保存链表的，而且耗时更短。
"""

class ListNode(object):
    def __init__(self, value = -1):
        self.val = value
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(0)
        self.length = 0


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index >= self.length or index < 0:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val


    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.length, val)


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            inedx = 0

        if index > self.length:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next
        new_node = ListNode(val)
        new_node.next = curr.next
        curr.next = new_node

        self.length += 1


    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return

        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.length -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)