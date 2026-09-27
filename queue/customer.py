from collections import deque

def serve_next(line):
    queue = line.popleft()
    return queue, line


line = serve_next(deque(["Alice", "Bob", "Carol"]))
print(line)
