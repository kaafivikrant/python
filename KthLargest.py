def findKthLargest(nums,k):
	nums.sort()
	return (nums[-k])
print(findKthLargest([3,5,2,4,6,8,9,10,10],3))