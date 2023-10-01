class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    def print_tree(self):
        espace = " " * self.get_level() * 3
        prifix = "|__"

        print(espace+prifix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()
def create_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("laptop")
    cell_phone = TreeNode("cell phone")
    Tv = TreeNode("Television")
    root.add_child(laptop)
    root.add_child(cell_phone)
    root.add_child(Tv)
    laptop.add_child(TreeNode("macbook"))
    laptop.add_child(TreeNode("thinkpad"))
    laptop.add_child(TreeNode("asus"))
    Tv.add_child(TreeNode("LG"))
    Tv.add_child(TreeNode("samsung"))
    Tv.add_child(TreeNode("iris"))
    cell_phone.add_child(TreeNode("iphone"))
    cell_phone.add_child(TreeNode("nokia"))
    cell_phone.add_child(TreeNode("Galaxy"))
    print(root.get_level())
    print(root.print_tree())
    return root
root = create_tree()
