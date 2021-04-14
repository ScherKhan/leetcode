"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before 
nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # need this for assertion to work
    def __eq__ (self, other):
        return self.val == other.val and self.next == other.next



def partition(head: ListNode, x: int) -> ListNode:
    lefthead = ListNode()
    righthead = ListNode()

    left = lefthead
    right = righthead
    # expand the linked list and separate the two wings according to its value
    while head:
        if head.val < x:
            left.next = head
            left = head
        else:
            right.next = head
            right = head

        # go to the next element in list
        head = head.next
    # combine two wings together
    # but not forget that first element are 0 for every wing
    left.next = righthead.next
    right.next = None

    return lefthead.next


def partition1(head: ListNode, x: int) -> ListNode:
    left, right = [], []
    while head:
        left.append(head.val) if head.val < x else right.append(head.val)
        head = head.next
    a = left + right
    # reconstruct one-linked list
    tail = None
    for el in a[::-1]:
        tail = ListNode(el, tail)
        
    return tail


def main():
    #Input: head = [1,4,3,2,5,2], x = 3
    #Output: [1,2,2,4,3,5]
    assert partition(ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3) == ListNode(1, ListNode(2, ListNode(2, ListNode(4, ListNode(3, ListNode(5))))))
    assert partition(ListNode(2, ListNode(1)), 2) == ListNode(1, ListNode(2))
    print('All tests passed')


if __name__ == '__main__':
    main()