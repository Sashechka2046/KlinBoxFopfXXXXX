class Heap:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def left(self, i):
        if (2*i+1) < self.size:
            return self.arr[2*i+1]
        else:
            return None
    def right(self, i):
        if (2*i+2) < self.size:
            return self.arr[2*i+2]
        else:
            return None
    def parent(self,i):
        if ((i-1)//2) < 0:
            return None
        else:
            return self.arr[(i-1)//2]

    def SiftDown(self, value, i):
        right = self.right(i)
        left = self.left(i)
        if not left and not right:
            return
        if not left:
            if value > right:
                return
            else:
                self.arr[i] = right
                self.arr[2 * i + 2] = value
                self.SiftDown(value, 2 * i + 2)
        elif not right:
            if value > left:
                return
            else:
                self.arr[i] = left
                self.arr[2 * i + 1] = value
                self.SiftDown(value, 2 * i + 1)
        else:
            if value > right and value > left:
                return
            else:
                if right > left:
                    self.arr[i] = right
                    self.arr[2 * i + 2] = value
                    self.SiftDown(value, 2 * i + 2)
                else:
                    self.arr[i] = left
                    self.arr[2 * i + 1] = value
                    self.SiftDown(value, 2 * i + 1)
    def SiftUp(self, value, i):
        parent = self.parent(i)
        if not parent:
            return
        if value > parent:
            self.arr[(i-1)//2] = value
            self.arr[i] = parent
            self.SiftUp(value, (i-1)//2)
        else:
            return
    def add(self, value, i):
        self.arr.append(value)
        self.size += 1
        self.SiftUp(value, i)
    def delete(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.arr.pop()
        self.size -= 1
        if self.size > 0:
            self.SiftDown(self.arr[0], 0)
        else:
            return
