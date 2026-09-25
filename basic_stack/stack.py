def undo_last(actions):
   stack = []
   all = actions.copy()
   stack = stack+all
   rem = stack.pop()
   return rem, stack



actions = ["type", "delete", "bold"]  
undone, remaining = undo_last(actions)
print(undone)
print(remaining)
