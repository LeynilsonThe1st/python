class BinaryTree:
    """
    Building a tree works much like building a tree in the physical world.
    Each item you add to the tree is a node. Nodes connect to each other using
    links. The combination of nodes and links forms a structure that looks
    much like a tree.

    Tree <==> Arvore

                --------ROOT---------
                |                   |
            BRANCH-A            BRANCH-B
            ____|____           ____|____
            |       |           |       |
        LEAF-C    LEAF-D     LEAF-E    LEAF-F
    """

    def __init__(self, node_data, left_node=None, right_node=None):
        self.node_data = node_data
        self.left_node = left_node
        self.right_node = right_node

    def __str__(self):
        root_node = str(self.node_data)
        if not self.linked(both=True):
            left = self.left_node
            right = self.right_node
        else:
            left = self.left_node.node_data
            right = self.right_node.node_data

        return f"\nNode_data: {root_node}\nLeft_node: {left}\nRigthNode: {right}\n"

    def linked(self, both=False):
        if both:
            if self.left_node is None and self.right_node is None:
                return False
            else:
                return True
        else:
            if self.left_node is None or self.right_node is None:
                return False
            else:
                return True

    def link(self, branch_data):
        if not self.linked():
            if self.left_node is None:
                branch = BinaryTree(branch_data)
                self.left_node = branch
                return True
            else:
                branch = BinaryTree(branch_data)
                self.right_node = branch
                return True
        else:
            return False

    def traverse(self):
        if self.left_node is not None:
            self.left_node.traverse()
        if self.right_node is not None:
            self.right_node.traverse()
        print(self.node_data)
        if "branch" in self.node_data:
            print('-'*17)


root = BinaryTree("I'm the root")

print(root)
print(root.linked())

root.link("I'm the A branch")
root.link("I'm the B branch")
print(root)

# Left node of leafs A
root.left_node.link("I'm The leaf A1")
root.left_node.link("I'm The leaf A2")
print(root.left_node)

# Right node of leafs B
root.right_node.link("I'm The leaf B1")
root.right_node.link("I'm The leaf B2")
print(root.right_node)

# Left node of leafs A
root.left_node.left_node.link("I'm The final leaf A1-1")
root.left_node.left_node.link("I'm The final leaf A1-2")
print(root.left_node.left_node)

# Left node of leafs A
root.left_node.right_node.link("I'm The final leaf A2-1")
root.left_node.right_node.link("I'm The final leaf A2-2")
print(root.left_node.right_node)

# Right node of leafs B
root.right_node.left_node.link("I'm The final leaf B1-1")
root.right_node.left_node.link("I'm The final leaf B1-2")
print(root.right_node.left_node)

# Right node of leafs B
root.right_node.right_node.link("I'm The final leaf B2-1")
root.right_node.right_node.link("I'm The final leaf B2-2")
print(root.right_node.right_node)

root.traverse()

# root.left_node.left_node.traverse()
# root.right_node.traverse()
