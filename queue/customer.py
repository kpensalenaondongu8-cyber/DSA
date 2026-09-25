from collections import deque

def serve_next(line):
    queue = deque()
    queue.append(line[0])
    queue.append(line[1])
    queue.append(line[2])

    removed = queue.popleft()
    return removed, queue

line = serve_next(["Alice", "Bob", "Carol"])
print(line)