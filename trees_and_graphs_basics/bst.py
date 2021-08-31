class Node:
    # Implement a node of the binary search tree.
    # Constructor for a node with key and a given parent
    # parent can be None for a root node.
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None  # We will set left and right child to None
        self.right = None
        # Make sure that the parent's left/right pointer
        # will point to the newly created node.
        if parent is not None:
            if key < parent.key:
                assert (parent.left is None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else:
                assert key > parent.key, 'key is same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert (parent.right is None), 'parent already has a right child -- unable to create node'
                parent.right = self

    # Utility function that keeps traversing left until it finds
    # the leftmost descendant
    def get_leftmost_descendant(self):
        if self.left is not None:
            return self.left.get_leftmost_descendant()
        else:
            return self

    # TODO: Complete the search algorithm below
    # You can call search recursively on left or right child
    # as appropriate.
    # If search succeeds: return a tuple True and the node in the tree
    # with the key we are searching for.
    # Also note that if the search fails to find the key
    # you should return a tuple False and the node which would
    # be the parent if we were to insert the key subsequently.
    def search(self, key):
        if self.key == key:
            return True, self
        # your code here
        if key < self.key:
            if self.left is None:
                return False, self
            return self.left.search(key)
        else:
            if self.right is None:
                return False, self
            return self.right.search(key)

    # TODO: Complete the insert algorithm below
    # To insert first search for it and find out
    # the parent whose child the currently inserted key will be.
    # Create a new node with that key and insert.
    # return None if key already exists in the tree.
    # return the new node corresponding to the inserted key otherwise.
    def insert(self, key):
        # your code here
        status, node = self.search(key)
        if status:
            return None
        if key < node.key:
            node.left = Node(key=key)
            node.left.parent = node
            return node.left
        node.right = Node(key=key)
        node.right.parent = node
        return node.right

    # TODO: Complete algorithm to compute height of the tree
    # height of a node whose children are both None is defined
    # to be 1.
    # height of any other node is 1 + maximum of the height
    # of its children.
    # Return a number that is th eheight.
    def height(self):
        # # your code here
        if self is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.right is None:
            return self.left.height() + 1
        elif self.left is None:
            return self.right.height() + 1
        return max(self.right.height(), self.left.height()) + 1

    # TODO: Write an algorithm to delete a key in the tree.
    # First, find the node in the tree with the key.
    # Recommend drawing pictures to visualize these cases below before
    # programming.
    # Case 1: both children of the node are None
    #   -- in this case, deletion is easy: simply find out if the node with key is its
    #      parent's left/right child and set the corr. child to None in the parent node.
    # Case 2: one of the child is None and the other is not.
    #   -- replace the node with its only child. In other words,
    #      modify the parent of the child to be the to be deleted node's parent.
    #      also change the parent's left/right child appropriately.
    # Case 3: both children of the parent are not None.
    #    -- first find its successor (go one step right and all the way to the left).
    #    -- function get_leftmost_descendant may be helpful here.
    #    -- replace the key of the node by its successor.
    #    -- delete the successor node.
    # return: no return value specified

    def delete(self, key):
        (found, node_to_delete) = self.search(key)
        assert (found == True), f"key to be deleted:{key}- does not exist in the tree"
        # your code here
        # case 1
        if node_to_delete.right is None and node_to_delete.left is None:
            if node_to_delete.parent.left == node_to_delete:
                node_to_delete.parent.left = None
            else:
                node_to_delete.parent.right = None
            del node_to_delete
        # case 2
        # this is xor
        elif bool(node_to_delete.left is not None) != bool(node_to_delete.right is not None):
            if node_to_delete.left is not None:
                node_to_delete.left.parent = node_to_delete.parent
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = node_to_delete.left
                else:
                    node_to_delete.parent.right = node_to_delete.left
                del node_to_delete
            else:
                node_to_delete.right.parent = node_to_delete.parent
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = node_to_delete.right
                else:
                    node_to_delete.parent.right = node_to_delete.right
                del node_to_delete
        # case 3
        else:
            successor = node_to_delete.right.get_leftmost_descendant()
            node_to_delete.key = successor.key
            if successor.parent.left == successor:
                successor.parent.left = None
            else:
                successor.parent.right = None
            del successor
