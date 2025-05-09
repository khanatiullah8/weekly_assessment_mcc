# ===== 1: best time to buy & sell stock

prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]

min_price = prices[0]
max_profit = 0

for price in prices[1:]:
	min_price = min(price, min_price)
	profit = price - min_price
	max_profit = max(profit, max_profit)

print("max profit ->", max_profit)


# ===== 2: squares of sorted array

nums = [-4,-1,0,3,10]

left = 0
right = len(nums)-1
index = len(nums)-1
output = []

while left <= right:
	left_sq = abs(nums[left])**2
	right_sq = abs(nums[right])**2
	
	if left_sq > right_sq:
		output[:0] = [left_sq]
		left += 1
	else:
		output[:0] = [right_sq]
		right -= 1
	index -= 1

print("squares of sorted array ->", output)


# ===== 3: find the word with the highest average ascii value	

str1 = "hello zoo sun"

def highest_average(lst):
  ascii_average = 0
  output = ""

  if len(lst) == 1:
    return lst[0]

  for word in lst:
    sum = 0
    for char in word:
      sum += ord(char)
    avg = sum/len(word)
    if avg > ascii_average:
      ascii_average = avg
      output = word

  return output

print("highest average ascii value:", highest_average(str1.split(" ")))
			
# ===== 4: count number of capital and small letters without using isupper()/islower()

str1 = "HelloWorld"
capital = 0
small = 0

for i in str1:
	if ord(i) >= 97 and ord(i) <= 122:
		small += 1
	elif ord(i) >= 65 and ord(i) <= 90:
		capital += 1

print("small:",small,"capital:",capital)



