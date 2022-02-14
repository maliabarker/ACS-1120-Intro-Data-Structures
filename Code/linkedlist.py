#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        node = self.head
        while node != None:
            count += 1
            node = node.next
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail
        node = Node(item)
        if self.is_empty() == True:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        node = Node(item)
        if self.is_empty():
            self.tail = node
        else:
            node.next = self.head
            
        self.head = node

    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        for node in self.items():
            if item == node:
                return True
        return False


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        # declaring start for loop
        node = self.head
        # declaring variables for previous node and if found
        previous = None
        found = False
        # looping through nodes, starting with head node
        while node != None:
            # print(f'current node {node}')
            # print(f'previous node {previous}')
            if node.data == item:
                # set found to true so no assertion error
                found = True

                # if this is head node then replace head node with next node
                if node == self.head:
                    # if there is no following nodes aka only node in list, delete it all!
                    if node.next == None:
                        self.head = None
                        self.tail = None
                    else:
                        self.head = node.next
                # if this is tail node replace tail with previous node and make next node
                # aka node after previous none
                elif node == self.tail:
                    previous.next = None
                    self.tail = previous
                # if this is node sandwiched between two other nodes
                else:
                    previous.next = node.next
                    # previous = None
                    
            # assign previous node as this node before moving on
            previous = node
            # assign current node to next node in orde to move on
            node = node.next

        if found == False:
            raise ValueError('Item not found: {}'.format(item))


if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)

    


