# I used this implementation to make the tree: https://stackoverflow.com/questions/41760856/most-simple-tree-data-structure-in-python-that-can-be-easily-traversed-in-both

class node(object):
    
    def __init__(self):
        self.data = None
        self.name = None
        self.parent = None
        self.children = []
        self.category = None
        self.isLeaf = False
        self.category = None
    
    def add_child(self, name, threshold, child):
        child.data = threshold
        self.children[name] = child
    