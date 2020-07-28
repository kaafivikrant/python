def Second_largest():
	a=list(map(int,input().split()))
	a.sort()
	a.reverse()
	if(len(a)==1):
		return -1
	else:
		for i in range(len(a)-1):
			if(a[i]==a[i+1]):
				continue
			return (a[i+1])
print(Second_largest())