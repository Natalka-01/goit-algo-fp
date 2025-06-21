class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # Delete the first node with the given key (data)
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur:
            prev.next = cur.next

    # Search for a node containing the given data
    def search_element(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    # Print all elements of the list
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" ")
            cur = cur.next
        print()

    # Task 1: Reverse the linked list by changing node links
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse link
            prev = current            # Move prev forward
            current = next_node       # Move current forward
        self.head = prev

    # Task 2: Sort the linked list using merge sort
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return
        self.head = self._merge_sort_recursive(self.head)

    # Recursive merge sort function
    def _merge_sort_recursive(self, head):
        if not head or not head.next:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None  # Split list into two halves

        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        return self._sorted_merge(left, right)

    # Utility function to find the middle of the list
    def _get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # Merge two sorted linked lists
    def _sorted_merge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

    # Task 3: Merge two sorted linked lists into one sorted list
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        a = list1.head
        b = list2.head

        # Compare elements from both lists and link the smaller one
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        # Attach remaining elements (if any)
        tail.next = a if a else b

        # Return the merged list
        result = LinkedList()
        result.head = dummy.next
        return result


# Create a linked list and insert some elements
ll = LinkedList()
for val in [30, 10, 50, 20, 40]:
    ll.insert_at_end(val)

# Print the original list
print("Original list:")
ll.print_list()

# Test reversing the list
ll.reverse()
print("After reversing:")
ll.print_list()

# Test sorting the list using merge sort
ll.merge_sort()
print("After sorting:")
ll.print_list()

# Create two sorted linked lists for merging
ll1 = LinkedList()
ll2 = LinkedList()

# Insert elements into the first sorted list
for val in [1, 3, 5]:
    ll1.insert_at_end(val)

# Insert elements into the second sorted list
for val in [2, 4, 6]:
    ll2.insert_at_end(val)

# Print both lists before merging
print("First sorted list:")
ll1.print_list()

print("Second sorted list:")
ll2.print_list()

# Merge the two sorted lists
merged = LinkedList.merge_sorted_lists(ll1, ll2)

# Print the merged sorted list
print("Merged sorted list:")
merged.print_list()
