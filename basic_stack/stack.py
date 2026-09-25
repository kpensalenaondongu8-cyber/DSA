def undo_last(actions):
   stack = []
   all = actions.copy()
   stack = stack+all
   rem = stack.pop()
   return f"usual: {actions} updated:{stack} removed: {rem}"



actions = ["type", "delete", "bold"]  
print(undo_last(actions))
