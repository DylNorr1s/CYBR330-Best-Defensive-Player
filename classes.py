class DoublyLinkedBase:

    class Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self.Node(None, None, None)
        self._trailer = self.Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        newest = self.Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, Node):
        predecessor = Node._prev
        successor = Node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = Node._element
        Node._prev = Node._next = Node._element = None
        return element

    def print_list(self):
        current = self._header._next
        while current is not self._trailer:
            print(current._element, end=" ")
            current = current._next

    def locate_mid(self):
        if self.is_empty():
            raise Exception("Empty")

        slow_pointer = self._header
        fast_pointer = self._header

        while fast_pointer is not None and fast_pointer._next is not None:
            slow_pointer = slow_pointer._next
            fast_pointer = fast_pointer._next._next

        print(f'\nMiddle Node: {slow_pointer._element}')


class PositionalList(DoublyLinkedBase):

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            # Returns element stored at this position
            return self._node._element

        def __eq__(self, other):
            # Return true if other is a position representing the same location
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            # Returns true if other does not represent the same location
            return not (self == other)

    def _validate(self, p):
        # Returns position's node or raise appropriate error if invalid
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        # Returns Position instance for given node (or None if sentinel)
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        # Return first position in the list
        return self._make_position(self._header._next)

    def last(self):
        # Return last position in the list
        return self._make_position(self._trailer._prev)

    def before(self, p):
        # Return the Position just before Position p
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        # Return the Position just after Position p
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        # Generates a forward iteration of the elements of the list
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

# --------------- Exercise 7C ---------------
    def __reversed__(self):
        # Should generate a backwards iteration of the elements
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def print_list(self):
        current = self._header._next
        while current is not self._trailer:
            print(current._element, end=" ")
            current = current._next

# ---------------- Exercise 7B -----------------
    def find(self, e):
        current = self._header._next
        index = 0
        while current is not self._trailer:
            if current._element == e:
                position = self._make_position(current)
                print(f'\nFound {e} at position {index}')
                return position
            current = current._next
            index += 1
        else:
            print(f'\n{e} is not in the list')
            return None


class PriorityQueueBase:
    # Abstract base class
    class _Item:
        # Lightweight composite to store priority queue items
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key       # compare items based on keys

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def _find_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def _find_max(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        large = self._data.first()
        walk = self._data.after(large)
        while walk is not None:
            if walk.element() > large.element():
                large = walk
            walk = self._data.after(walk)
        return large

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return item._key, item._value


class SortedPriorityQueue(PriorityQueueBase):

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return item._key, item._value

    # Added a class to remove the elements at the end of the sorted priority queue
    def remove_end(self):
        if self.is_empty():
            raise Exception('Priority queue is empty')
        item = self._data.delete(self._data.last())
        return item._key, item._value
