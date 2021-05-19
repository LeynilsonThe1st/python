"""
Unlike stacks, queues are first in/first out (FIFO) data structures.
Queues <=> filas
"""
import queue

MyQueue = queue.Queue(3)
print("Queue empty: ", MyQueue.empty())
MyQueue.put(1)
MyQueue.put(2)
MyQueue.put(3)
print("Queue full: ", MyQueue.full())
print("Popping: ", MyQueue.get())
print("Queue full: ", MyQueue.full())
print("Popping: ", MyQueue.get())
print("Popping: ", MyQueue.get())
print("Queue empty: ", MyQueue.empty())
