nums = [1,2,3,4,5,6,7,8,9,10]

print(nums[0:3])
print(nums[-4:-1])
start = int((len(nums)/2)-2)
end = int((len(nums)/2)+2)
print(nums[start:end])

for i, num in enumerate(nums):
	if(i%2 == 0):
		print(nums[i+1])
		
for i, num in enumerate(nums):
	if(i%2 == 1):
		print(nums[i-1])
		
print(nums[::-1])