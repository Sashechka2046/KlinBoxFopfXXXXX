class Tree:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)
        self.main = 0
        self.i_main = 0
        self.right = []
        self.left =[]

    def SiftDown(self, value):
        if self.arr == []:
            self.main = value
            self.i_main = 0
        if value > self.main:
            if not self.right:
                self.right.append(value)
            else:
                tr
    def find_p(self, value):


l = 9 # int(input())
a = list(map(int, '7 3 2 1 9 5 4 6 8'.split()))

mons = Tree([])

for i in a:
    Tree.Siftdown(i)

print(mons.tree)
