nums = [5, 4, 2, 1, 7, 4, 20]
print(nums)
nums_2 = nums.copy()

nums.insert(2, 20)
print(nums)
nums.remove(7)
print(nums)
nums.pop()
print(nums)
print(nums.index(4))
print(50 in nums)
print(nums.count(4))
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.clear()
print(nums)
print(nums_2)
print("_" * 20)

list_1 = [4, 6, 7, 2, 7, 4, 3, 6, 3, 7, 30]
print(list_1)
list_2 = []
for number in list_1:
    if number not in list_2:
        list_2.append(number)
print(list_2)