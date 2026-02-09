class DoctorNode:
    def __init__(self, name: str):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def _find_node(self, node, target_name):
        """DFS search to find a node by name."""
        if node is None:
            return None
        if node.name == target_name:
            return node
        left_found = self._find_node(node.left, target_name)
        if left_found:
            return left_found
        return self._find_node(node.right, target_name)

    def insert(self, parent_name: str, employee_name: str, side: str) -> bool:
        """
        Insert employee_name under parent_name on 'left' or 'right'.
        Returns True if inserted, False if invalid parent/side/occupied spot.
        """
        if self.root is None:
            return False

        side = side.lower().strip()
        if side not in ("left", "right"):
            return False

        parent = self._find_node(self.root, parent_name)
        if parent is None:
            return False

        new_node = DoctorNode(employee_name)

        if side == "left":
            if parent.left is not None:
                return False
            parent.left = new_node
            return True
        else:
            if parent.right is not None:
                return False
            parent.right = new_node
            return True

    def preorder(self, node) -> list:
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node) -> list:
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node) -> list:
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


# -------------------- Tests --------------------
if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    # Insert values (matches assignment diagram)
    assert tree.insert("Dr. Croft", "Dr. Goldsmith", "right") is True
    assert tree.insert("Dr. Croft", "Dr. Phan", "left") is True
    assert tree.insert("Dr. Phan", "Dr. Carson", "right") is True
    assert tree.insert("Dr. Phan", "Dr. Morgan", "left") is True

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    # Expected outputs
    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]

    # Edge cases
    assert tree.insert("Dr. NotReal", "Dr. X", "left") is False          # parent missing
    assert tree.insert("Dr. Croft", "Dr. Y", "middle") is False          # bad side
    assert tree.insert("Dr. Croft", "Dr. Z", "left") is False            # already occupied

"""
DESIGN MEMO (200–300 words)

A tree is appropriate for the doctor structure because it naturally represents a hierarchy. Each doctor can manage other doctors, and a binary tree lets us model “reports” as left and right children. This mirrors real organizations where every person (node) has relationships to the people beneath them. Using a tree also makes searching and walking the structure efficient and readable.

Traversal order matters because it changes the meaning of the output. Preorder is useful when you want to process a manager before their reports, such as generating a top-down leadership briefing or printing an org chart starting from the head doctor. Inorder is useful when the structure has an ordering meaning (like a binary search tree), or when you want to list the left side of the organization, then leadership, then the right side. Postorder is useful when you must process all reports before the manager, such as completing evaluations, collecting status updates from subteams first, or safely “closing out” subordinate work before finalizing a supervisor’s summary.

Heaps simulate real-time priority systems well because they keep the most important item at the top with fast inserts and removals. In emergency intake, patients arrive continuously and must be re-ordered immediately by urgency. A min-heap ensures the patient with the lowest urgency score (highest priority) is always served next, while maintaining efficient performance as the queue grows.
"""

