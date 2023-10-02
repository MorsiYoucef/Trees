
class BinarySearchTree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    def add_child(self,data):
        if data == self.data:
            return

        if self.data > data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    def inorder_traversel(self):
        numbers = []
        if self.left:
            numbers += self.left.inorder_traversel()

        numbers.append(self.data)

        if self.right:
            numbers+=self.right.inorder_traversel()

        return numbers
    def binary_search(self,data):

        if self.data == data:
            return True

        if self.data>data:
            if self.left:
                return self.left.binary_search(data)
            else:
                return False

        if self.data<data:

            if self.right:
                return self.right.binary_search(data)
            else:
                return False

def creat_binary_tree(element):
    root = BinarySearchTree(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

if __name__ == "__main__":
    numbers = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    Tree_numbers = creat_binary_tree(numbers)
    print(Tree_numbers.binary_search("Pakistan"))
    print(Tree_numbers.inorder_traversel())

