from typing import List, Optional
import math



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        tmp = []
        current = self
        while current:
            tmp.append(current.val)
            current = current.next
        return "[" + ', '.join([str(x) for x in tmp]) + "]"

    def __repr__(self):
        tmp = []
        current = self
        while current:
            tmp.append(current.val)
            current = current.next
        return "[" + ', '.join([str(x) for x in tmp]) + "]"

def make_linked_list(l: List[int]):
    head = ListNode(l[0])
    current = head
    for x in l[1:]:
        current.next = ListNode(x)
        current = current.next
    return head

def get_middle(head: Optional[ListNode], inclusive_middle: bool = False):
    pointer_low = head
    pointer_high = head
    cntr = 0
    while pointer_high:
        pointer_high = pointer_high.next
        cntr += 1
        if cntr and not cntr % 2:
            pointer_low = pointer_low.next
    if inclusive_middle or not cntr % 2:
        return pointer_low, (cntr // 2) - 1
    else:
        return pointer_low.next, math.ceil(cntr / 2) - 1


def split_at(head: Optional[ListNode], ind: int) -> (Optional[ListNode], Optional[ListNode]):
    assert ind >= 0
    current = head
    prev = None
    cntr = 0
    while current and cntr <= ind:
        prev = current
        current = current.next
        cntr += 1
    prev.next = None
    return head, current


def get_len(head: Optional[ListNode]) -> int:
    l = 1
    current = head
    if not current:
        return 0
    while True:
        if not current or not current.next:
            break
        l += 1
        current = current.next
    return l

def reverse_ll(head: Optional[ListNode]):
    if not head:
        return None
    if not head.next:
        return head
    prev = head
    current = head.next
    head.next = None
    while current:
        tmp = current.next
        current.next = prev
        prev = current
        if not tmp:
            break
        current = tmp
    return current

def removeNthFromEnd(head: Optional[ListNode], n: int):
    l = get_len(head)
    if not l - n:
        return head.next
    prev = None
    current = head
    cntr = 0
    while current:
        if cntr == l - n and prev:
            prev.next = current.next
        else:
            prev = current
        current = current.next
        cntr += 1
    return head


def delete_values_from_ll(head: Optional[ListNode], values: List[int]):
    values = set(values)
    prev = None
    current = head
    while current:
        changed = False
        if current.val in values:
            if current == head:
                head = current.next
            if prev:
                changed = True
                prev.next = current.next
        if not changed:
            prev = current
        current = current.next
    return head