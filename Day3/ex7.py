stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)


print("Popped:", stack.pop())
print("After Pop:", stack)


print("Top Element:", stack[-1])


from collections import deque
queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue:", queue)


print("Dequeued:", queue.popleft())
print("After Dequeue:", queue)

print("Front Element:", queue[0])
