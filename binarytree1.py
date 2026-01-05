class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree(self):
        space = " " * self.get_level()
        prefix = space + "|__" if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        level = 1
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
        
def buit_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))

    phone = TreeNode("Phone")
    phone.add_child(TreeNode("Nokia"))
    phone.add_child(TreeNode("Samsung"))
    phone.add_child(TreeNode("iPhone"))

    root.add_child(laptop)
    root.add_child(phone)

    return root





if __name__ == "__main__":
    root = buit_tree()
    root.print_tree()
    