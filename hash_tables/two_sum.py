def two_sum_slow(nums, target):
     for i in range(len(nums)):
         for j in range(i + 1,len(nums)):
              if nums[i] + nums[j] == target:
                   return nums[i], nums[j]

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
             return [seen[need], i]
        
        seen[num] = i
    return None    

print(two_sum([2, 7, 11, 15], 9))      
print(two_sum([3, 2, 4], 6))           
print(two_sum([1, 2, 3], 100)) 
all = list(range(1, 10))
print(two_sum(all, 5))           
big = list(range(1, 5001))
print(two_sum_slow(big, 9999))   
print(two_sum(big, 9999))        