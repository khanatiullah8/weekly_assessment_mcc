#1: Two Sum

#nums = [2,7,11,15]; target = 9
#nums = [3,2,4]; target = 6
nums = [3,3]; target = 6

for i in range(len(nums)):
	for j in nums[i+1:]:
		if nums[i] + j == target:
			print([i,nums.index(j, i+1)])
			break

# ===================================================

#2: Valid Parentheses

#str1 = "()[]{}"
#d = {"(":1, ")":-1, "{":1, "}":-1, "[":1, "]":-1}
#result = 0

#for i in str1:
#	result += d[i]
#print("true") if result == 0 else print("false")

# ===================================================

#3: Compare the Triplets

#a = [5,6,7]
#b = [3,6,10]

#alice_score = 0
#bob_score = 0

#result = ['a' if a[i]>b[i] else 'b' if a[i]<b[i] else '' for i in #range(len(a))]

#print([result.count('a'),result.count('b')])


# ===================================================

#4: Excel sheet Column Number

#col_dict = {chr(x): key+1 for key,x in enumerate(range(65,91))}

#columnTitle = "AB"
#columnNumber = 0

#for col in columnTitle:
#	columnNumber = columnNumber * 26 + col_dict[col]

#print(columnNumber)



# ===================================================

#5: Convert 12-Hour AM/PM Time to 24-Hour Military Time

#s = "07:05:45PM"
#s = "12:05:45AM"

#t = s[:-2].split(":")

#if s.endswith("PM") and int(t[0]) < 12:
#	t[0] = str(int(t[0]) + 12)
#elif s.endswith("AM") and int(t[0]) > 11:
#	t[0] = '0' + str(int(t[0]) - 12)

#output = ":".join(t)
#print(output)




