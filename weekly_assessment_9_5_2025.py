# 1. move zeroes

nums = [0, 1, 0, 3, 12]

for i in range(len(nums)):
	if nums[i] == 0:
		nums.append(nums.pop(i))

print(nums)

# ===================================================

# 2. find all permutations

#from itertools import permutations

#input = "abc"

#result = ["".join(s) for s in permutations(input)] 
#print(result)

# ===================================================

# 3. check if a matrix is Toeplitz

#matrix = [
#	[1, 2, 3, 4],
#	[5, 1, 2, 3],
#	[9, 5, 1, 2]
#	]

#row = len(matrix)
#col = len(matrix[0])
#output = False

#for i in range(row-1):
#	for j in range(col-1):
#		if matrix[i][j] == matrix[i+1][j+1]:
#			output = True
#		else:
#			output = False
#			break

#print(output)

# ===================================================

# 4. Check if Array Can Form an Arithmetic Progression

#arr = [3, 5, 1]
#count = 1
#diff_value = 0
#output = False

#while True:
#	for i in range(len(arr)-1):
#		temp = arr[i] - arr[i+1]
#		if temp != diff_value:
#			diff_value = temp
#			output = False
#		else:
#			output = True

#	if output or not count:
#		break
#	else:
#		arr.sort()
#	count -= 1

#print(output)

# ===================================================

# 5. Kth Smallest Element in Matrix

#matrix = [
#	[1, 5, 9],
#	[10, 11, 13],
#	[12, 13, 15]
#	]

#k = 8

#result = sorted(sum(matrix, []))
#print(result[k-1])




