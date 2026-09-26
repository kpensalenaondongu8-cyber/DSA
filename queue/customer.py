from collections import deque

def serve_next(line):
    removed = line.popleft()
    return removed, queue

line = serve_next(["Alice", "Bob", "Carol"])
print(line)



