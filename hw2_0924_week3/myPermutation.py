import random
def perm(n): 
	p = []
	q = [] 
	max = 0
	# print(p,',',q)
	# print(n)
	p = [0] * n 
	for m in range(n):
		p[m] = (m+1)*random.randint(1, 100)
		# print('p[',m,']:',p[m])
		# print(p)
		if max < p[m]:
			max = p[m]
	# print('n:',n,',p:',p,',q',q)
	return permNext(n, p, q)

def permNext(n, p, q): 
	i = len(q)
	if i == n:
		print(q)  
		return
	for x in range(n): 
		# print(p)
		# print('p[',x,']:',p[x])
		if not p[x] in q: 
			# print('1',p,q)
			q.append(p[x])
			# print('2',p,q)    
			permNext(n, p, q)
			# print('3',p,q)
			q.pop() 
			# print('4',p,q)      

n = int(input("enter a number:"))
# print(n)
perm(n)
x = 1
for i in range(n):
    x=x*(i+1)
print("有",x,"種排列組合")