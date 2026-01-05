class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def print_tree_name(self):
        spaces = "  " * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        for key in self.data.keys():
            print(prefix, key)
        if self.children:
            for child in self.children:
                child.print_tree_name()
    
    def print_tree_desg(self):
        space = "  " * self.get_level()
        prefix = space + "|__" if self.parent else ""
        for value in self.data.values():
            print(prefix, value)
        
        if self.children:
            for child in self.children:
                child.print_tree_desg()

    def print_tree(self):
        space = "  " * self.get_level()
        prefix = space + "|__" if self.parent else ""
        for key, value in self.data.items():
            print(prefix, key, "(", value, ")")
        
        if self.children:
            for child in self.children:
                child.print_tree()

    def get_level(self):
        level = 1
        p = self.parent
        while p:
            p = p.parent
            level += 1
        
        return level

def create_tree():
    ceo = TreeNode({"Nilupul":"CEO"})
    cto = TreeNode({"Chinmay":"CTO"})
    ih = TreeNode({"Vishwa":"Infrastruture Head"})
    cm = TreeNode({"Dhaval":"Cloud Maneger"})
    am = TreeNode({"Abhijeet":"App Maneger"})
    ah = TreeNode({"Aamir":"Application Head"})
    hr = TreeNode({"Gels":"HR Head"})
    rm = TreeNode({"Peter":"Recrutment Maneger"})
    pm = TreeNode({"Waqas":"Policy Maneger"})

    ceo.add_child(cto)
    ceo.add_child(hr)

    cto.add_child(ih)
    cto.add_child(ah)

    ih.add_child(cm)
    ih.add_child(am)

    hr.add_child(rm)
    hr.add_child(pm)

    return ceo


if __name__ == "__main__":
    ceo = create_tree()
    ceo.print_tree_name()
    ceo.print_tree_desg()
    ceo.print_tree()