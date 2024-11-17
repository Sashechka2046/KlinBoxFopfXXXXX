# [3, 5, 7, 12, 11, 9, 8]
# class Node:
#     def __init__(self, x):
#         self.value = x
#         self.parent = 0
#         self.left = 0
#         self.right = 0
#
#
# class Tree:
#     def __init__(self):
#         self.root = 0
#         self.size = 0
#
# class Heap:
#     def __init__(self, arr):
#         self.arr = arr
#         self.size = len(arr)
#     def left(self, value, i):
#         if (2*i + 1) < self.size:
#             return self.arr[2*i+1]
#         else:
#             return None
#     def right(self, value, i):
#         if (2*i + 2) < self.size:
#             return self.arr[2*i+2]
#         else:
#             return None
#     def parent(self, i):
#         if ((i-1) // 2) < 0:
#             return None
#         else:
#             return self.arr[(i-1) // 2]
#
#     def SiftDown(self, value, i):
#         right = self.right(i)
#         left = self.left(i)
#         if value > right and value > left:
#             return
#         # if value > right and value < left:
#         #     self.arr[i] = left
#         #   hight:
#                 self.arr[i] = right
#                 self.arr[2*i+2] = value
#                 self.SiftDown(value, 2*i+2)
#     def SiftUp(self, value, i):
