def is_balanced(s):
   stack = []
   for all in s:
      if all == "(":
         stack.append(all)
      elif all == ")":
          if stack == []:
             return False         
          else:
             stack.pop()

   if stack == []:
    return True
   else:
    return False
             

print(is_balanced("(())"))   
print(is_balanced("(()"))    
print(is_balanced(")("))     
print(is_balanced("()()"))           