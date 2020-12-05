from .linked_list import LinkedList

def kth_to_last(ll, k):
    runner = current = ll.head
    for _ in range(k):
        if not runner:
            return
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))
