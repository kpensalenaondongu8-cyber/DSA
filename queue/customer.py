from collections import deque

def serve_next(line):
<<<<<<< HEAD
    queue = line.popleft()
    return queue, line


line = serve_next(deque(["Alice", "Bob", "Carol"]))
print(line)
=======
    removed = line.popleft()
    return removed, queue

line = serve_next(["Alice", "Bob", "Carol"])
print(line)



>>>>>>> f7323c959c418715342b04bc44a700fdf6998f3a
