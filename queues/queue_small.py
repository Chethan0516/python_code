# reverse the queue

# from queue import Queue

# def reverse(q):
#     if q.empty():
#         return 
#     data = q.get()
#     reverse(q)
#     q.put(data)

# q = Queue()
# for item in [1, 2, 3, 4, 5]:
#     q.put(item)

# reverse(q)

# result = []
# while not q.empty():
#     result.append(q.get())
# print(result)

# implement Queue using stack

# class Que:

#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
    
#     def enqueue(self, item):
#         self.stack1.append(item)
    
#     def dequeue(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#         if not self.stack2:
#             return "Queue is empty"
#         return self.stack2.pop()

# q = Que()
# q.enqueue(2)
# q.enqueue(3)
# print(q.dequeue())
# print(q.dequeue())    

# First negative integer in every window of size k
# (Given an array and a window size k,
# find the first negative integer in every window of size k.)

# from collections import deque

# def first(arr, k):
#     result = []
#     dq = deque()
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             dq.append(i)
#         if i > k -1:
#             if dq and dq[0] < i - k + 1:
#                 dq.popleft()
#             result.append(arr[dq[0]] if dq else 0)
#     return result
# arr = [12, -1, -7, 8, -15, 30, 16, 28]
# k = 3
# print(first(arr, k))

# Generate Binary Numbers from 1 to N

# from queue import Queue

# def generate(n):
#     q = Queue()
#     q.put("1")
#     result = []

#     for _ in range(n):
#         front = q.get()
#         result.append(front)
#         q.put(front + "0")
#         q.put(front + "1")
#     return result
# n = 5
# print(generate(n))

# Check for Balanced Parentheses Using Queue

# from queue import LifoQueue

# def para(s):
#     stack = LifoQueue
#     for char in s:
#         if char =="(":
#             stack.put(char)
#         elif char == ")":
#             if stack.empty():
#                 return False
#             else:
#                 stack.get()
#     return stack.empty()
# s1 = "(())()"
# s2 = "(()"
# print(para(s1))
# print(para(s2))


# Interleave First Half with Second Half

# from queue import Queue

# def interleave(q):
#     size = q.qsize()
#     first_half = Queue()
#     for _ in range(size // 2):
#         first_half.put(q.get())
#     while not first_half.empty():
#         q.put(first_half.get())
#         q.put(q.get())
# q = Queue()
# for item in [1, 2, 3, 4, 5, 6]:
#     q.put(item)
# interleave(q)
# result = []
# while not q.empty():
#     result.append(q.get())
# print(result)

# Maximum of All Subarrays of Size k

